import os
import time
import shutil
import getpass

from datetime import datetime

from studio_usd_pipe import resource
from studio_usd_pipe.core import asset
from studio_usd_pipe.core import preference


class Connect(object):
    
    def __init__(self, subfield, **kwargs):
        self.subfiled = subfield            
        self.bundle = kwargs
        self.publish_path = self.get_pulish_path()     
        pref = preference.Preference()
        input_dirname = pref.get()            
        self.show_path = input_dirname['show_directory']
        self.mayapy_path = input_dirname['mayapy_directory']            
        self.register_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        self.stamped_time = time.time()
        self.my_asset = asset.Asset(subfiled=self.subfiled)        
        
    def pack(self):
        self.my_asset.pack(self.packed_bundle)

    def release(self):        
        self.my_asset.release(self.packed_bundle, self.stamped_time)
        
    def collect_packed(self):
        self.packed_bundle = {
            'caption': self.bundle['caption'],
            'version': self.bundle['version'],
            'type': self.bundle['type'],
            'tag': self.bundle['tag'],
            'subfield': self.subfiled,
            'user': getpass.getuser(),
            'date': self.register_date,
            'source_file': self.bundle['source_file'],
            'show_path': self.show_path,
            'mayapy': self.mayapy_path,
            'publish_path': self.publish_path        
            }
        return self.packed_bundle

    def get_pulish_path(self):
        package_path = os.path.join(
            self.show_path,
            self.subfiled,
            self.bundle['caption'],
            self.bundle['subfield'],
            self.bundle['version']
            )
        return package_path
