import os
import logging
import warnings
import sqlite3

from pprint import pprint

from crowd import resource
from crowd import utils


reload(utils)


class Connect(object):

    def __init__(self, db=None, table=None):
        self.db = db
        self.table = table
        if not self.db:
            label, root = resource.getDatabaseDirectory()
            self.db = os.path.join(root, '%s.db' % label)
        self.default_column = [
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
        self.create()

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
            warnings.warn('TypeError: Table is not defind!...', Warning)
            return
        if not os.path.isdir(os.path.dirname(self.db)):
            os.makedirs(os.path.dirname(self.db))
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        key_container = []
        for key in self.default_column:
            key_container.append('{} {} '.format(key, self.key_types[key]))
        column = ', '.join(key_container)
        result = None
        try:
            cursor.execute(
                'CREATE TABLE if not exists {} ({})'.format(self.table, column))
            result = 'DataBase initialized table called <%s>!...' % self.table
        except Exception as error:
            result = 'OperationalError: {}'.format(str(error))
        finally:
            connect.commit()
            connect.close()
        logging.info(result)

    def add_column(self, column):
        ''''
            :description Adding a new columns without a row value
            :param column <list> example ['name', 'id']
        '''
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        column_keys = '\'{}\''.format('\' \''.join(column))
        try:
            cursor.execute(
                'ALTER TABLE {} ADD COLUMN {}'.format(self.table, column_keys))
            logging.info(
                'added new columns <%s> to table <%s> successfully!...' % (column, self.table))
        except Exception as error:
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
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
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)

        finally:
            connect.commit()
            connect.close()
        return count

    def get_latestID(self):
        contents = self.select()
        if not contents:
            return 0
        return contents[-1][0]

    def get_nextID(self):
        latestID = self.get_latestID()
        return latestID + 1

    def get_ID(self, tag):
        tag_data = self.select()
        for each_tags in tag_data:
            if each_tags[1] != tag:
                continue
            id = each_tags[0]
            return id
        if not id:
            warnings.warn(
                '#DBReadError: Not able to find <%s> ID directory' % tag)
            return None

    def is_tables(self, input):
        exist_tables = self.get_columns()
        print '\n\texists tables', exist_tables
        print '\t input tables', input.keys()
        for each in input:
            if each in exist_tables:
                continue
            print '#Value error: Not found %s in the table' % each
            return False
        return True

    def is_tag_id(self, tag):
        tag_data = self.select()
        for each_tags in tag_data:
            if each_tags[1] != tag:
                continue
            id = each_tags[0]
            return True, id
        if not id:
            warnings.warn(
                '#DBReadError: Not able to find <%s> ID directory' % tag)
            return False, None

    def configure_table_values(self, id, input):
        columns = []
        column_values = []
        if 'id' in input:
            input.pop('id')
        if 'date' in input:
            input.pop('date')
        if 'user' in input:
            input.pop('user')
        for k, v in input.items():
            columns.append(k)
            column_values.append(v)
        current_time = utils.get_datetime()
        current_user = utils.get_user()
        columns = ['id', 'date', 'user'] + columns
        column_values = [id, current_time, current_user] + column_values
        entities = ['?' for x in range(len(column_values))]
        return columns, entities, column_values

    def insert(self, id=None, **kwargs):
        ''''
            :description Inserts an ID with a specific value in to the column
        '''
        if not self.is_tables(kwargs):
            raise Exception(
                'ValueError: not found column in the table!...')
        if not id:
            id = self.get_nextID()
        columns, entities, column_values = self.configure_table_values(
            id, kwargs)
        column = ', '.join(columns)
        entitie = ', '.join(entities)

        result = True, 'Success!...'
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute('INSERT INTO {}({}) VALUES({})'.format(
                self.table, column, entitie), column_values)
            result = True, 'Success!...'
            logging.info('Insert the values successfully!...')
        except Exception as error:
            result = False, '%s!...' % str(error)
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()
        return result

    def overwrite(self, **kwargs):
        ''''
            :description overwrite/replace the exists tag
        '''
        if not self.is_tables(kwargs):
            raise Exception(
                'ValueError: not found column in the table!...')

        id = self.get_ID(tag=kwargs['tag'])
        column, entities, value_data = self.configure_table_values(id, kwargs)
        # example column = [id, date, user, tag, manifest]
        # example entities = ?, ?, ?, ?, ?
        # example value_data = [6, '2019/30/June - 07:14:39:PM', 'shreya',
        # 'man', '/home/']
        result = True, 'Success!...'
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            for index in range(1, len(column)):
                print column[index]
                print value_data[index], '\n\n'
                cursor.execute('UPDATE {} SET {}=\"{}\" WHERE id={}'.format(
                    self.table, column[index], value_data[index], id))
        except Exception as error:
            result = False, '%s!...' % str(error)
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()
        return result

    def select(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        contents = None
        try:
            cursor.execute(
                'SELECT *FROM {}'.format(self.table))
            contents = cursor.fetchall()
        except Exception as error:
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)

        finally:
            connect.commit()
            connect.close()
        return contents

    def update(self, id, column, column_value):
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
                self.table, column, column_value, id))
        except Exception as error:
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()

    def delete(self, id):
        '''
            :param id <str> example 0, 1, 2
        '''
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute(
                'DELETE FROM {} WHERE id = {}'.format(self.table, id))
        except Exception as error:
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()

    def delete_table(self):
        connect = sqlite3.connect(self.db)
        cursor = connect.cursor()
        try:
            cursor.execute('DROP table if exists {}'.format(self.table))
        except Exception as error:
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
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
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()
        return columns

    def get_values(self, key):
        tables = self.get_columns()
        contents = self.select()
        if key not in tables:
            warnings.warn(
                'ValueError: not found key<%s> in the table' % key, Warning)
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
            warnings.warn('OperationalError: {}'.format(str(error)), Warning)
        finally:
            connect.commit()
            connect.close()
        return tables
