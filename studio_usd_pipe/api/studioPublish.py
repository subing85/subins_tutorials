import json

import os
import time
import shutil
import getpass

from datetime import datetime
from distutils import version


from studio_usd_pipe import resource
from studio_usd_pipe.core import asset
from studio_usd_pipe.core import preference

reload(asset)


class Publish(object):
    
    def __init__(self, mode, **kwargs):
        '''
        assetPublish > 
            asset > self.my_asset
                mayapack > self.mpack
                mayarelease
        from studio_usd_pipe.api import studioPublish
        reload(studioPublish)
        pub = studioPublish.Publish(
            'asset',
            subfield='model',
            type = 'intarctive',
            tag = 'character',
            source_file = '/venture/shows/my_hero/dumps/batman_finB.ma',
            caption = 'batman',
            version = '0.0.0',
            thumbnail = '/local/references/images/btas_batmodel_03.jpg',
            description = 'test publish'
            )
        pub.pack()                  

        '''
        self.mode = mode        
        pref = preference.Preference()
        input_dirname = pref.get() 
        self.show_path = input_dirname['show_directory']
        self.mayapy_path = input_dirname['mayapy_directory']  
        self.stamped_time = time.time()
        self.publish_path = None
        
        # self.get_pulish_path()
       
        self.valid_modes = {
            'asset': {
                'subfield': ['model', 'uv', 'surface', 'puppet'],
                'tag': ['character', 'prop', 'environment'],
                'type': ['interactive', 'non-interactive']
                },                
            'shot': {
                'subfield': ['primarylayout', 'secondarylayout', 'animation', 'lighting', 'compositing']
                }
            }
        
        self.valid_publish_keys = {
            'asset': [
                'subfield', 'caption', 'type', 'tag', 'thumbnail', 'description', 'next_version'
                ],
            'shot': [
                'subfield', 'tag', 'type', 'caption', 'thumbnail', 'description', 'next_version'
                ]
            }
        
        self.my_step = None
        
        if self.mode=='asset_push' or self.mode=='asset_pull':
            self.my = asset.Asset()
            
        if self.mode=='shot':
            pass
           
               
        
    def has_valid_publish(self):
        if self.mode in self.valid_modes:
            return True
        return False
        
    def has_valid_subfield(self, subfield):
        if self.has_valid_publish():
            if subfield in self.valid_modes[self.mode]['subfield']:
                return True
        return False
        
    def pack(self):
        '''
        :example        
            from studio_usd_pipe.api import studioPublish
            reload(studioPublish)
            pub = studioPublish.Publish(
                'asset',
                subfield='model',
                type = 'intarctive',
                tag = 'character',
                source_file = '/venture/shows/my_hero/dumps/batman_finB.ma',
                caption = 'batman',
                version = '0.0.0',
                thumbnail = '/local/references/images/btas_batmodel_03.jpg',
                description = 'test publish'
                )
            pub.pack()
            pub.release()
        '''        
        self.collect_packed()
        if self.mode=='asset':
            self.my.subfield = self.bundle['subfield']
            # my_asset = asset.Asset(subfield=self.bundle['subfield']) 
            self.my.pack(self.packed_bundle)
            
    def release(self): 
        if self.mode=='asset':
            self.my.release()
            #self.packed_bundle, self.stamped_time)
            
    def collect_packed(self):        
        if not self.publish_path:
            self.publish_path = self.get_pulish_path()
        self.packed_bundle = {
            'caption': self.bundle['caption'],
            'version': self.bundle['version'],
            'type': self.bundle['type'],
            'tag': self.bundle['tag'],
            'subfield': self.bundle['subfield'],
            'thumbnail': self.bundle['thumbnail'],
            'description': self.bundle['description'],
            'time_stamp': self.stamped_time,
            'user': getpass.getuser(),
            # 'date': time.strftime('%Y/%d/%B - %I/%M/%S/%p', time.gmtime(self.stamped_time)),
            'source_file': self.bundle['source_file'],
            'show_path': self.show_path,
            'mayapy': self.mayapy_path,
            'publish_path': self.publish_path        
            }
        return self.packed_bundle

    def get_pulish_path(self):
        package_path = os.path.join(
            self.show_path,
            self.mode,
            self.bundle['caption'],
            self.bundle['subfield'],
            self.bundle['version']
            )
        return package_path
    
    def get(self):
        data = self.my.get()
        return data
    
    def get_subfields(self, caption):
        subfield_data = self.my.get_subfields(caption)
        return subfield_data
    
    def get_version_data(self, caption, subfield):
        version_data = self.my.get_version_data(caption, subfield)
        return version_data
    
    def get_versions(self, caption, subfield):
        version_data = self.my.get_version_data(caption, subfield)
        versions = version_data.keys()        
        versions.sort(key=version.StrictVersion)
        versions.reverse()    
        return versions

    def get_data(self, caption, subfield, version):        
        data = self.my.get_asset_data(caption, subfield, version)
        return data
    
    def get_latest_version(self, caption, subfield, version_data=None):
        if not version_data:
            version_data = self.get_versions(caption, subfield)
        versions = version_data.keys()        
        versions.sort(key=version.StrictVersion)
        versions.reverse()
        if not versions:
            return None
        return versions[0]
    
    def get_next_version(self, latest_version, index):
        '''
            index 0, 1, 2 = MAJOR0, MINOR, PATCH
        '''
        n_version = '0.0.0'
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
