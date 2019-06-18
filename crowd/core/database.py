import os
import logging
import sqlite3
import getpass

from datetime import datetime

from crowd import resource


class Database(object):

    def __init__(self, db=None, table=None):
        self.db = db
        self.table = table
        if not self.db:
            label, root = resource.getDatabaseDirectory()
            self.db = os.path.join(root, '%s.db' % label)
        self.default_keys = [
            'id',
            'tag',
            'user',
            'date',
            'manifest'
        ]
        self.key_types = {
            'id': 'integer PRIMARY KEY',
            'tag': 'text',
            'user': 'text',
            'date': 'text',
            'manifest': 'text'
        }

    def open(self, force=False):
        '''
            :description Connecting to an SQLite database
        '''
        if not os.path.isdir(os.path.dirname(self.db)):
            os.makedirs(os.path.dirname(self.db))
        try:
            conn = sqlite3.connect(self.db)
            conn.close()
            logging.info('Opened database successfully!...')
            return True
        except Exception as error:
            logging.warning(str(error))
            return False

    def create(self):
        ''''
            :description Creating a new SQLite table with default columns
                default columns are tag, user, data, manifest
        '''
        if not self.table:
            logging.warning('TypeError: Table is not defind!...')
            return
        if not os.path.isdir(os.path.dirname(self.db)):
            os.makedirs(os.path.dirname(self.db))
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        key_container = []
        for key in self.default_keys:
            key_container.append('{} {} '.format(key, self.key_types[key]))
        keys = ', '.join(key_container)
        try:
            cursor.execute(
                'CREATE TABLE if not exists {} ({})'.format(self.table, keys))
            logging.info('Created table <%s> successfully!...' % self.table)
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()
        logging.info('Table %s created successfully!...' % self.table)

    def add_column(self, keys):
        ''''
            :description Adding a new columns without a row value
            :param keys <list> example ['name', 'id']
        '''
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        column_keys = '\'{}\''.format('\' \''.join(keys))
        try:
            cursor.execute(
                'ALTER TABLE {} ADD COLUMN {}'.format(self.table, column_keys))
            logging.info(
                'added new columns <%s> to table <%s> successfully!...' % (keys, self.table))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()

    def rowcount(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        count = 0
        try:
            cursor.execute('SELECT * FROM {}'.format(self.table))
            count = len(cursor.fetchall())
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()
        return count

    def insert(self, **kwargs):
        ''''
            :description Inserts an ID with a specific value in to the column
        '''
        exist_tables = self.get_columns()
        for each in kwargs:
            if each in exist_tables:
                continue
            raise Exception(
                'ValueError: not found key <%s> in the table!...' % each)

        key_data = []
        value_data = []

        if 'id' in kwargs:
            kwargs.pop('id')
        if 'date' in kwargs:
            kwargs.pop('date')
        if 'user' in kwargs:
            kwargs.pop('user')

        for k, v in kwargs.items():
            key_data.append(k)
            value_data.append(v)

        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM {}'.format(self.table))
        current_time = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        key_data = ['id', 'date', 'user'] + key_data
        value_data = [
            len(cursor.fetchall())+1, current_time, getpass.getuser()
        ] + value_data
        keys = ', '.join(key_data)
        entities = ', '.join(['?' for x in range(len(value_data))])
        try:
            cursor.execute('INSERT INTO {}({}) VALUES({})'.format(
                self.table, keys, entities), value_data)
            logging.info('Insert the values successfully!...')
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()

    def select(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        contents = None
        try:
            cursor.execute(
                'SELECT *FROM {}'.format(self.table))
            contents = cursor.fetchall()
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()
        return contents

    def update(self, id, key, value):
        '''
            :description Updates the inserted or pre-existing entry 
            :param id <int> example 1, 2
            :param key <str> example 'tag', 'user'
            :param value <str> example 'biped', 'sachin'
        '''
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute('UPDATE {} SET {}=\"{}\" WHERE id={}'.format(
                self.table, key, value, id))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()

    def delete(self, id, key):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute(
                'DELETE FROM {} WHERE id = {}'.format(self.table, id))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()

    def delete_table(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute('DROP table if exists {}'.format(self.table))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()

    def get_columns(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        columns = None
        try:
            cursor.execute(
                'SELECT *FROM {}'.format(self.table))
            columns = list(map(lambda x: x[0], cursor.description))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()
        return columns

    def get_values(self, key):
        tables = self.get_columns()
        contents = self.select()
        if key not in tables:
            logging.warning('ValueError: not found key<%s> in the table' % key)
            return
        index = tables.index(key)
        values = []
        for each in contents:
            values.append(each[index])
        return values

    def get_tables(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        tables = None
        try:
            cursor.execute(
                'SELECT name from sqlite_master where type= "table"')
            tables = list(map(lambda x: x[0], cursor.fetchall()))
        except Exception as error:
            logging.warning('OperationalError: {}'.format(str(error)))
        finally:
            connect.commit()
            connect.close()
        return tables
