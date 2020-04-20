import os
import re
import getpass
import logging
import sqlite3

from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import preferences


class DataBase(object):
    
    def __init__(self, pipe):        
        self.pipe = pipe
        self.pref = preferences.Preferences()
        pref_data = resource.getPreferenceData(path=self.pref.preference_path)
        self.db = os.path.join(
            pref_data['database_directory'], '{}.db'.format(self.pipe))
        self.table_prefix = 'table'
        self.initialize(force=False)
        
    def initialize(self, force=False):
        if not self.pipe:
            return
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
        except Exception as IOError:
            logging.info(IOError)
            
    def connect(self):
        '''
            Make connection to an SQLite database file
        '''
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        return conn, cursor

    def close(self, conn):
        '''
            Commit changes and close connection to the database
        '''
        conn.commit()
        conn.close()
    
    def create(self, kwargs):
        '''
        :description create table if not found and inserts an column id with a specific value
        :param kwargs <dict>
        :parem current_table <str> example 'table_0'        
        :example            
            kwargs = {
                'caption': {'value': 'batman_01', 'order': 0},
                'version': {'value': '0.1.1', 'order': 1},
                'subfield': {'value': 'model', 'order': 2 },
                'type': {'value': 'inractive', 'order': 3},
                'tag': {'value': 'character', 'order': 4},
                'modified': {'value': '01-01-2110', 'order': 5},
                'location': {'value': '/show/assets/batman/0.0.0', 'order': 6}
                }         
            dbs = DataBase('asset')
            dbs.create(kwargs)            
        '''
        #kwargs['user'] = {
        #    'order': len(kwargs),
        #    'value': getpass.getuser()
        #    }
        headers = self.sort_dictionary(kwargs)
        values = [kwargs[header]['value'] for header in headers]
        current_table = self.next_table()
        if not self.has_table(current_table):
            self.create_table(current_table, headers)        
        placeholders = ['?' for x in range(len(headers))]
        placeholder = ', '.join(placeholders)
        cloumns = ', '.join(headers)  
        connect, cursor = self.connect()  # connect to sqlite3
        try:
            cursor.execute('INSERT INTO {}({}) VALUES({})'.format(
                current_table, cloumns, placeholder), values)
            result = True, 'Success!...'
        except Exception as error:
            result = False, 'OperationalError: %s!...' % str(error)
        finally:
            self.close(connect)
        logging.info('database insert {}'.format(result[1]))
        return result
    
    def update(self, table, kwargs):
        '''
        :description updates the newly inserted or pre-existing entry.   
        :param table <int> example 0, 1, 2
        :param kwargs <dict> 
        :example            
            kwargs = {
                'caption': 'batman_01',    
                'version': '1.1.1',
                'subfield': 'model',
                'type': 'inractive',
                'tag': 'character',
                'modified':'01-01-2110',
                'location': '/venture/test_show/assets/batman/0.0.0',
                }
            dbs = DataBase('asset')                  
            dbs.update(1, kwargs)       
        '''
        current_table = '{}_{}'.format(self.table_prefix, table)
        kwargs['modified'] = datetime.now().strftime('%Y/%d/%B - %I/%M/%S/%p')
        if not self.has_table(current_table):
            logging.warn('Not found such column <{}>'.format(table))
            return 
        connect, cursor = self.connect()  # connect to sqlite3        
        columns = self.get_columns(current_table)
        try:
            for k, v in kwargs.items():
                if k not in columns:
                    logging.warn('Not found such column <{}>'.format(k))
                    continue
                cursor.execute(
                    'UPDATE {} set {}=\"{}\" where {}={}'.format(current_table, k, v, k, k))
            result = True, 'Success!...'                
        except Exception as error:
            result = False, 'OperationalError:%s!...' % str(error)
        finally:
            self.close(connect)
        logging.warn('database updates {}'.format(result[1]))
        return result
             
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
            data.setdefault(table, colum_data)
        return data  
        
    def select(self, table):
        '''
            Value of a particular column for rows that match a certain value in column
        '''
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
    
    def create_table(self, table, headers):
        connect, cursor = self.connect()  # connect to sqlite3
        headers_data = ', '.join(headers)
        try:
            cursor.execute(
                'CREATE TABLE if not exists {} ({})'.format(table, headers_data))
            result = 'DataBase initialized table called <%s>!...' % table
        except Exception as error:
            result = 'OperationalError: {}'.format(str(error))
        finally:
            self.close(connect)
        logging.info(result)       
        
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
        
    def next_table(self):
        tables = self.get_tables()
        table = '{}_0'.format(self.table_prefix)
        if not tables:
            return table
        index = map(int, re.findall(r'\d+', tables[-1]))[-1]
        table = '{}_{}'.format(self.table_prefix, index + 1)
        return table   
    
    def has_table(self, table):
        tables = self.get_tables()
        print tables
        if not table:
            return False
        if table in tables:
            return True
        return False

    def delete_table(self, table):
        connect, cursor = self.connect()
        try:
            cursor.execute('DROP table if exists {}'.format(table))
        except Exception as error:
            logging.warn('OperationalError: {}'.format(str(error)))
        finally:
            self.close(connect)
    
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
            
    def sort_dictionary(self, dictionary):
        sorted_data = {}
        for contents in dictionary:
            sorted_data.setdefault(
                dictionary[contents]['order'], []).append(contents)
        order = sum(sorted_data.values(), [])
        return order  
    
