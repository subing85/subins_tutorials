import os
import json
import warnings

from PySide import QtGui

from studioPipe import resources
from studioPipe.modules import studioImage
from studioPipe.modules import studioDataBase


class Connect(object):

    def __init__(self):
        '''
        Description -API operate on read and write shows informations.
            : __init__() <None>.       
        '''
        self.icon_format = '.png'
        self.db_type = 'pipe_db'
        self.studio_db = os.path.join(
            '/home/shreya/Documents/studio_pipe', self.db_type)
        self.module = 'shows'
        self.tag = 'pipe_shows'
        self.width, self.height = 256, 144
        self.cursor = studioDataBase.Connect(
            db_dirname=self.studio_db, tag=self.tag, localhost='shows', name='show_inputs')

    def hasShow(self, show_name):
        '''
        Description -function set for validate the show.
            :paran show_name <str> example 'my_super_hero'
            :return <bool>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.hasShow('my_super_hero')
        '''
        self.cursor.rollback()
        if show_name in self.cursor.rollback_data:
            return True
        return False

    def getInputData(self):
        '''
        Description -function set for get the show input data.
            :paran <None>
            :return (<dict>, <list>)
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getInputData('my_super_hero')
        '''
        input_file = os.path.join(resources.getInputPath(), 'show.json')
        read_db = studioDataBase.Connect(full_path=input_file)
        input_data = read_db.getData()
        sort_input_data = read_db.sort_input_data(input_data)
        return input_data, sort_input_data

    def get(self, show_name=None):
        '''
        Description -function set for get exists show or shows data.
            :paran show_name <str> exmple 'my_super_hero'
            :return <dict>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.get('my_super_hero')
        '''
        data = self.cursor.getContents()
        if not show_name:
            return data['data']
        self.cursor.rollback()
        if show_name in self.cursor.rollback_data:
            show_index = self.cursor.rollback_data[show_name]
            current_show = data['data'][show_index]
            print json.dumps(current_show, indent=4)
            return current_show

    def getShows(self):
        '''
        Description -function set for get show list.
            :paran <None> 
            :return <list>
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.getShows()
        '''
        data = self.cursor.getContents()
        sort_data = self.cursor.sort_db_data(data['data'])
        return sort_data

    def create(self, **kwargs):
        '''
        Description - Creates and edit the exists show this function set to operate        
            :param na <str> exmple 'my_super_hero'
            :param dn <str> exmple 'My Super Hero'
            :param sn <str> exmple 'MSH'
            :param tp <str> exmple 'My Super Hero'
            :param ic <str> exmple '/tmp/hero.png'            
            :example
                from studioPipe.api import studioShows
                ss = studioShows.Shows()
                ss.create(na='my_super_hero',
                    dn = 'My Super Hero',
                    sn = 'MSH',
                    tp = 'My Super Hero',
                    ic = '/tmp/hero.png'
                    )
        '''
        icon_path = os.path.join(
            self.studio_db, self.module, '%s%s' % (kwargs['na'], self.icon_format))
        input_datas = {
            'show_name': kwargs['na'],
            'display_name': kwargs['dn'],
            'short_name': kwargs['sn'],
            'tooltip': kwargs['tp'],
            'show_icon': icon_path,
        }
        if not os.path.isfile(kwargs['ic']):
            warnings.warn('not found file %s' % kwargs['ic'], Warning)
            return
        studio_image = studioImage.ImageCalibration(imgae_file=kwargs['ic'])
        q_image, q_image_path = studio_image.setStudioSize(
            width=self.width, height=self.height)
        self.cursor.execute('update', {kwargs['na']: input_datas})
        q_image.save(icon_path)
