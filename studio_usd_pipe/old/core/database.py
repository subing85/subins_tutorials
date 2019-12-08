import os
import re
import json
import logging
import sqlite3

from distutils import version

from studio_usd_pipe import utils
from studio_usd_pipe import resources


class Connect(object):

    def __init__(self, parent):
        self.db = os.path.join(self.get_db_dirname(), parent)
        self.initialize(force=False)

    def initialize(self, force=False):
        if force:
            self.remove_db()
        if not os.path.isdir(os.path.dirname(self.db)):
            os.makedirs(os.path.dirname(self.db))
        return

    def remove_db(self):
        if not os.path.isfile(self.db):
            return
        try:
            os.remove(self.db)
        except Exception as error:
            logging.info(error)

    def get_db_dirname(self):
        preference_path = resources.getPreferencesPath()
        with (open(preference_path, 'r')) as open_data:
            data = json.load(open_data)
            if not data['enable']:
                return None
            return data['data']['database_directory']

    def connect(self):
        """ Make connection to an SQLite database file """
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        return conn, cursor

    def close(self, conn):
        """ Commit changes and close connection to the database """
        conn.commit()
        conn.close()

    def config_column(self, inputs):  # make columns string
        key_container = []
        self._columns = sorted(inputs.keys())
        # self._columns.extend(['user', 'date'])
        for key in self._columns:
            if key == 'caption':
                key_container.append('{} {} '.format(key, 'text PRIMARY KEY'))
            else:
                key_container.append('{} {} '.format(key, 'text'))
        self.column_data = ', '.join(key_container)

    def has_table(self, table):
        tables = self.get_tables()
        if not table:
            return False
        if table in tables:
            return True
        return False

    def db_register(self, **kwargs):
        '''
            dbs = Connect('asset')
            dbs.create(caption = 'bat',
                version = '0.1.0',
                # subfield = 'model',    
                # subfield = 'surfacing',
                # subfield = 'puppet',
                # tag = 'character',
                tag = 'prop',    
                path = '/venture/test_show/assets/batman/batman_0.0.2.mb'
                )        
        '''
        if not os.path.isdir(os.path.dirname(self.db)):
            os.makedirs(os.path.dirname(self.db))
        self.config_column(kwargs)
        table = self.next_table()
        
        
        print 'hello table', table
        
        print 'self.has_table(table)', self.has_table(table)
        
        if not self.has_table(table):
            self.create_table(table)
            
            
        # kwargs.setdefault('user', utils.get_user())
        # kwargs.setdefault('date', utils.get_datetime())
        bundles = [kwargs[column] for column in self._columns]
        print '\n\n', table, '\n', bundles
        self.insert(table, bundles)

    def create_table(self, table):
        
        print 'ggggggggggggggggggggggg'
        
        print json.dumps(self.column_data, indent=4)
        connect, cursor = self.connect()  # connect to sqlite3
        #try:
        cursor.execute(
            'CREATE TABLE if not exists {} ({})'.format(
                table, self.column_data))
        result = 'DataBase initialized table called <%s>!...' % table
        #except Exception as error:
        #    result = 'OperationalError: {}'.format(str(error))
        #finally:
        self.close(connect)
        logging.info(result)

    def insert(self, table, bundles):
        ''''
            :description Inserts values to specific value to table under the column
        '''
        entities = ['?' for x in range(len(bundles))]
        entitie = ', '.join(entities)
        column = ', '.join(self._columns)

        connect, cursor = self.connect()  # connect to sqlite3
        # try:
        cursor.execute('INSERT INTO {}({}) VALUES({})'.format(
            table, column, entitie), bundles)
        result = True, 'Success!...'
        logging.info('Insert the values successfully!...')
        #-------------------------------------------- except Exception as error:
            #----------------------------- result = False, '%s!...' % str(error)
            #----------- logging.warn('OperationalError: {}'.format(str(error)))
        #-------------------------------------------------------------- finally:
        self.close(connect)
        logging.info(result)

    def select(self, table):
        connect, cursor = self.connect()
        contents = None
        try:
            cursor.execute('SELECT *FROM {}'.format(table))
            contents = cursor.fetchall()
            if contents:
                contents = contents[0]
        except Exception as error:
            logging.warn('OperationalError: {}'.format(str(error)))
        finally:
            self.close(connect)
        return contents

    def delete_table(self, table):
        connect, cursor = self.connect()
        try:
            cursor.execute('DROP table if exists {}'.format(table))
        except Exception as error:
            logging.warn('OperationalError: {}'.format(str(error)))
        finally:
            self.close(connect)

    def get_tables(self):
        connect, cursor = self.connect()
        tables = None
        try:
            cursor.execute(
                'SELECT name from sqlite_master where type= "table"')
            tables = list(map(lambda x: x[0], cursor.fetchall()))
        except Exception as error:
            logging.warn('OperationalError: {}'.format(str(error)))
        finally:
            self.close(connect)
        return tables

    def get_columns(self, table):
        connect, cursor = self.connect()
        columns = None
        try:
            cursor.execute('SELECT *FROM {}'.format(table))
            columns = list(map(lambda x: x[0], cursor.description))
        except Exception as error:
            logging.warn('OperationalError: {}'.format(str(error)))
        finally:
            self.close(connect)
        return columns

    def get(self):
        tables = self.get_tables()
        data = {}
        for index, table in enumerate(tables):
            columns = self.get_columns(table)
            values = self.select(table)
            colum_data = {}
            for x, column in enumerate(columns):
                if x < len(values):
                    colum_data.setdefault(column, values[x])
                else:
                    colum_data.setdefault(column, None)
            data.setdefault(index, colum_data)
        return data

    def next_table(self):
        tables = self.get_tables()
        table = 'table_0'
        if not tables:
            return table
        index = map(int, re.findall(r'\d+', tables[-1]))[-1]
        table = 'table_{}'.format(index + 1)
        return table

    def get_versions(self, caption, subfield, tag):
        '''
            :param subfield <str> example 'model'
            :param tag <str> example 'character'
            :param name <str> example 'batman'
            :example            
                db = Connect('asset')
                versions = db.get_versions('character', 'batman', 'model')            
        '''
        data = self.get()
        versions = []
        for table, contents in data.items():
            if caption != contents['caption']:
                continue
            if subfield != contents['subfield']:
                continue
            if tag != contents['tag']:
                continue

            if contents['version'] in versions:
                continue
            versions.append(contents['version'])
        versions.sort(key=version.StrictVersion)
        versions.reverse()
        return versions

    def get_latest_version(self, caption, subfield, tag):
        versions = self.get_versions(caption, subfield, tag)
        if not versions:
            return None
        return versions[0]

    def get_next_version(self, index, caption, subfield, tag):
        '''
            index 0, 1, 2 = MAJOR0, MINOR, PATCH
        '''
        n_version = '0.0.0'
        latest_version = self.get_latest_version(caption, subfield, tag)
        if not latest_version:
            return n_version
        major, minor, patch = latest_version.split('.')
        if index == 0:
            n_version = '{}.{}.{}'.format(int(major) + 1, 0, 0)
        if index == 1:
            n_version = '{}.{}.{}'.format(major, int(minor) + 1, 0)
        if index == 2:
            n_version = '{}.{}.{}'.format(major, minor, int(patch) + 1)
        return n_version

    def get_captions(self):
        data = self.get()
        captions = []
        for contents in data:
            if data[contents]['caption'] in captions:
                continue
            captions.append(data[contents]['caption'])
        captions.sort()
        return captions

'''
dbs = Connect('asset')

dbs.db_register(
    caption = 'batman',
    version = '0.1.1',
    subfield = 'model',
    type = 'inractive',
    tag = 'character',
    path = '/venture/test_show/assets/batman/batman_0.0.2.mb'
    )

dbs.db_register(
    caption='batman',
    version = '0.1.1',
    subfield='model',
    type='inractive',
    tag='character',
    #user='sgopi',
    date='01-01-2110',
    path='/venture/test_show/assets/batman/0.0.0'
    )

"caption text PRIMARY KEY ,
path text , subfield text ,
tag text , type text , version text , user text , date text "

#data = dbs.get_captions()
#print '\n\n', '#'*50, '\n', json.dumps(data, indent=4), '\n', '#'*50

# print dbs.get_tables()
'''