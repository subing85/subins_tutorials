import os
import json
import time
import shutil
import tempfile

from datetime import datetime

from studio_usd_pipe import utils
from studio_usd_pipe import resources
from studio_usd_pipe.core import subshell
from studio_usd_pipe.core import database
from studio_usd_pipe.api import studioImage


class Publish(database.Connect):
    
    def __init__(self, parent, **kwargs):
        super(Publish, self).__init__(parent)
        
        self.parent = parent
        self.packed_data = None
        
        input_dirname  = resources.getInputDirname()
        self.show_path = input_dirname['shows_directory']
        self.mayapy_path = input_dirname['mayapy_directory']

        self.standalone = True
        if 'standalone' in kwargs:
            self.standalone = kwargs['standalone']
        
        self.register_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        self.stamped_time = time.time()
        
        self.sem_versions = ['major', 'minor', 'patch']
        self.publish_types = ['versions', 'variations']
        
        self.node = 'Hires_Geo_Group'

        
                
                

    def pack(self, bundle):
        if self.parent=='asset':
            self.packed_data = self.asset_pack(bundle)
        if self.parent=='scene':
            self.packed_data = self.scene_pack(bundle)
        return self.packed_data     
    
    def release(self, data=None):
        if not data:
            data = self.packed_data
        print json.dumps(data, indent=4)
        self.db_register(
            caption = data['caption'],
            subfield = data['subfield'],
            type = data['type'],            
            tag = data['tag'],
            version = data['version'],                   
            user = data['user'],
            date = data['date'],
            path = data['path']
            )
        return True

    def asset_pack(self, bundle):
        dirname_to = self.make_root(bundle)
        maya_file = self.make_maya_file(dirname_to, bundle['source_file'], bundle['caption'])
        thumbnail = self.make_thumbnail(dirname_to, bundle['thumbnail'], bundle['caption'])        
        source_images_path = self.make_source_images(maya_file, dirname_to)

        static_usd = self.make_static_usd(bundle['source_file'], dirname_to, bundle['caption'])
        active_usd = self.make_active_usd(bundle['source_file'], dirname_to, bundle['caption'])
        
        bundle['maya_file'] = maya_file
        bundle['thumbnail'] = 'image_file'
        bundle['maya_used_file'] = static_usd
        bundle['maya_puppet_usd_file'] = active_usd
        bundle['source_images_path'] = source_images_path
        bundle['thumbnail'] = thumbnail
        
        manifest_file = self.make_manifest(dirname_to, bundle)
        
        self.packed_data = {
            'caption': bundle['caption'],
            'version': bundle['version'],
            'subfield': bundle['subfield'],
            'type': bundle['type'],
            'tag': bundle['tag'],          
            'user': utils.get_user(),
            'date': self.register_date,
            'path': dirname_to            
            }        
        return self.packed_data
       
    def scene_pack(self, bundle):
        pass    
    
    
    
    def make_root(self, bundle):
        package_path = os.path.join(
            self.show_path,
            bundle['category'],
            bundle['caption'],            
            bundle['subfield'],
            bundle['version'])
        if os.path.isdir(package_path):
            self.reomve_dirname(package_path)            
        os.makedirs(package_path, 0755)
        self.time_stamp(package_path)
        return package_path
    
    def make_maya_file(self, dirname, maya_file, caption):
        format = os.path.splitext(maya_file)[-1]        
        target_path = os.path.join(dirname, '{}{}'.format(caption, format))
        shutil.copy2(maya_file, target_path)       
        self.time_stamp(target_path)
        return target_path
        
    def make_thumbnail(self, dirname, image_file, caption):
        s_image = studioImage.ImageCalibration(imgae_file=image_file)
        target_path = os.path.join(
            dirname, '{}.{}'.format(caption, s_image.format))
        image, image_path = s_image.set_studio_size(
            output_path=target_path,width=256, height=180)
        self.time_stamp(image_path)
        return image_path 
    
    def get_studio_usd_package(self):
        current_path = os.path.dirname(__file__)
        
    def make_source_images(self, source_file, dirname_to):
        source_images_path_to = os.path.join(dirname_to, 'source_images')
        self.reomve_dirname(source_images_path_to)
        os.makedirs(source_images_path_to, 0755)
        self.time_stamp(source_images_path_to)        
        source_script = resources.getScriptSourceScripts('export_source_images')
        if self.standalone:
            subshell.sub_process(
                self.mayapy_path,
                source_script,
                args = [
                    source_file.encode(), 
                    source_images_path_to.encode(),
                    self.stamped_time
                    ]
                )
        else:
            from studio_usd_pipe.core import smaya
            from studio_usd_pipe.core import export            
            export.pack_source_images(dirname_to, stamped_time=self.stamped_time)
            smaya.save_file(source_file, stamped_time=self.stamped_time)
        return source_images_path_to
    
    def make_static_usd(self, source_file, dirname_to, maya_file, caption):
        source_usd_path_to = os.path.join(dirname_to, 'source_usd')
        self.reomve_dirname(source_usd_path_to)
        os.makedirs(source_usd_path_to, 0755)
        self.time_stamp(source_usd_path_to) 
                
        if self.standalone:
            pass
        
        else:
            from studio_usd_pipe.core import export 
            from studio_usd_pipe.core import compositing            
                       
            uds_paths = export.pack_static_usd(
                self.node, source_usd_path_to, stamped_time=self.stamped_time)
            
            compositing.reference(uds_paths)
            
            
            
        target_path = os.path.join( 
            dirname_to, '{}.{}'.format(caption, 'usd'))
        return target_path
    
    def make_active_usd(self, source_file, dirname_to, caption):
        target_path = os.path.join(
            dirname_to, '{}.{}'.format(caption, 'usda'))
        return target_path
    
    
    
    
    def make_manifest(self, dirname, bundle):
        target_path = os.path.join(dirname, '.manifest')
        bundle_data = {
            'comment': 'subin gopi tool kits',
            'created_date': self.register_date,
            'author': 'Subin Gopi',
            'copyright': '(c) 2019, Subin Gopi All rights reserved.',
            'warning': 'WARNING! All changes made in this file will be lost!',
            'description': 'This data contain publish information',
            'type': '{}_publish'.format(bundle['category']),
            'enable': True,
            'user': utils.get_user(),
            'data': bundle}      
        with (open(target_path, 'w')) as open_data:
            open_data.write(json.dumps(bundle_data, indent=4))
            return target_path
        return None
    
    def time_stamp(self, path):
        if not os.path.exists(path):
            return
        os.utime(path, (self.stamped_time, self.stamped_time))          

    def reomve_dirname(self, dirname):    
        if not os.path.isdir(dirname):
            return
        os.chmod(dirname, 0777)
        try:
            shutil.rmtree(dirname)
        except Exception as OSError:
            print OSError

#===============================================================================
# bundle = {
#     "category": "asset", 
#     "caption": "batman",
#     "type": "intractive", 
#     "tag": "character", 
#     "version": "2.1.0", 
#     "source_file": "/venture/test_show/assets/batman/batman_0.0.2.mb", 
#     "subfield": "model", 
#     "thumbnail": "/mnt/bkp/reference/august2627.png", 
#     "description": "test publish"
# }
# publish = Publish('asset')
# data = publish.pack(bundle)
#===============================================================================
# publish.release(data)
