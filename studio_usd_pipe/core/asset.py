import os
import time
import shutil
import tempfile

import json

from studio_usd_pipe.core import mayapack
from studio_usd_pipe.core import database
from studio_usd_pipe.core import preference

reload(mayapack)
reload(database)
reload(preference)


class Asset(object):
    
    def __init__(self, subfield=None):       
        
        self.standalone = False
        self.data = {}
        
        self.subfield = subfield
        self.width, self.height = 640, 400
        self.entity = 'assets'         
        self.temp_entity = 'studio_asset'       
        
        self.asset_ids = [
            'sentity',      
            'scaption',
            'stype',
            'stag',
            'sversion',
            'smodified',
            'spath',
            'sdescription'
            ]        
    
        self.mpack = mayapack.Pack()
        
        self.set_inputs()
        
    def set_inputs(self):
        pref = preference.Preference()
        self.input_data = pref.get()        
        self.db_directory = self.input_data['database_directory']   
        self.show_icon = self.input_data['show_icon']
        self.mayapy = self.input_data['mayapy_directory']
        self.show_path = self.input_data['show_directory']
    
    def pack(self, bundle):
        '''
            import time
            from studio_usd_pipe.core import asset
            reload(asset)        
            asset = asset.Asset(subfield='model')        
            bundle = {
                'source_file': '/venture/shows/my_hero/dumps/batman_finB.ma',
                'caption': 'batman',
                'version': '0.0.0',
                'thumbnail': '/local/references/images/btas_batmodel_03.jpg',
                'type': 'interactive',
                'tag': 'character',
                'description': 'test publish',
                'time_stamp': time.time()
                }        
            asset.pack(bundle)         
        '''
             
        self.source_maya = bundle['source_file']
        self.caption = bundle['caption']
        self.version = bundle['version'] 
        self.thumbnail = bundle['thumbnail']
        self.type = bundle['type']
        self.tag = bundle['tag']
        self.description = bundle['description']   
        self.time_stamp = bundle['time_stamp']        
        
        self.publish_path = os.path.join(
            self.show_path,
            self.entity,
            self.caption,
            self.subfield,
            self.version
            )
          
        # self.make_root()
        self.temp_pack_path = self.make_temp_root()
        
        if self.subfield == 'model':
            self.make_maya_model(force=True)
            self.make_thumbnail()
            self.make_studio_model()                       
            self.make_model_usd()
            self.make_maya()
            self.make_manifest()
            
        if self.subfield == 'uv':
            self.make_maya_model(force=False)
            self.make_thumbnail()            
            self.make_studio_uv()
            self.make_uv_usd()
            self.make_maya()
            
        if self.subfield == 'surface':
            self.make_maya_model(force=False)
            self.make_thumbnail()            
            self.make_source_images()
            self.make_studio_surface()            
            # self.make_surface_usd()
            self.make_maya()
                     
        if self.subfield == 'puppet':
            self.make_maya_model(force=False)
            self.make_thumbnail()
            # self.make_source_images()                     
            # self.make_puppet_usd()            
            self.make_maya()

        for each in sum(self.data.values(), []): # time stamp
            os.utime(each, (self.time_stamp, self.time_stamp))

    def release(self):        
        result = self.move_to_publish()        
        if not result:
            return
        
        data = time.strftime('%Y/%d/%B - %I/%M/%S/%p', time.gmtime(self.time_stamp))
        kwargs = {
                'caption': {
                    'value': self.caption,
                    'order': 0
                    },
                'version': {
                    'value': self.version,
                    'order': 1
                    },
                'subfield': {
                    'value': self.subfield,
                    'order': 2
                    },
                'type': {
                    'value': self.type,
                    'order': 3
                    },
                'tag': {
                    'value': self.tag,
                    'order': 4
                    },
                'date': {
                    'value': data,
                    'order': 5
                    },
                'path': {
                    'value': self.publish_path,
                    'order': 6
                    }
                }                
        dbs = database.DataBase(self.entity)
        dbs.create(kwargs)
        
    
    def move_to_publish(self):   
        temp_pack_path = os.path.join(
            tempfile.gettempdir(), self.temp_entity)             
        self.make_root()        
        for each in sum(self.data.values(), []):
            path = each.replace(temp_pack_path, self.publish_path)
            if os.path.isdir(each):
                if not os.path.isdir(path):
                    os.makedirs(path)
                    self.set_time_stamp(path)
            if os.path.isfile(each):                 
                if not os.path.isdir(os.path.dirname(path)):
                    os.makedirs(os.path.dirname(path))
                try:            
                    shutil.copy2(each, path)
                except Exception as IOError:
                    print IOError
                    return False
        return True

    

    def make_maya_model(self, force=False):
        '''
            import time
            from studio_usd_pipe.core import asset
            reload(asset)        
            asset = asset.Asset(subfield='model')        
            bundle = {
                'source_file': '/venture/shows/my_hero/dumps/batman_finB.ma',
                'caption': 'batman',
                'version': '0.0.0',
                'thumbnail': '/local/references/images/btas_batmodel_03.jpg',
                'type': 'interactive',
                'tag': 'character',
                'description': 'test publish',
                'time_stamp': time.time()
                }        
            asset.pack(bundle)        
        '''
        inputs = {
            self.asset_ids[0]: self.entity,
            self.asset_ids[1]: self.caption,
            self.asset_ids[2]: self.type,
            self.asset_ids[3]: self.tag,
            self.asset_ids[4]: self.version,
            self.asset_ids[5]: self.time_stamp,
            self.asset_ids[6]: self.publish_path,
            self.asset_ids[7]: self.description,
            'node': 'model',
            'world': 'world'
            }        
        self.mpack.create_model(inputs, force=force)  
         
    def make_thumbnail(self):
        inputs = {
            'standalone': self.standalone,
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'thumbnail': self.thumbnail,
            'time_stamp': self.time_stamp,
            'width': 512,
            'height': 512,
            'force': True
            } 
        thumbnail = self.mpack.create_thumbnail(inputs)
        self.data['thumbnail'] = [thumbnail]
                         
    def make_maya(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,            
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        maya_file = self.mpack.create_maya(inputs)
        self.data['maya_file'] = [maya_file]
        
    def make_studio_model(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,            
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_model = self.mpack.create_studio_model(inputs)
        self.data['studio_model'] = [studio_model]    
 
    def make_studio_uv(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,            
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_uv = self.mpack.create_studio_uv(inputs)
        self.data['studio_uv'] = [studio_uv] 
        
    def make_source_images(self): 
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,
            'publish_directory': self.publish_path,       
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': False
            }
        souce_data, source_images = self.mpack.create_source_images(inputs)
        self.data['source_image_data'] = [souce_data]
        self.data['source_images'] = source_images
        self.data['source_images_directory'] = [os.path.join(
            self.temp_pack_path, 'source_images')]   
       
                
    def make_studio_surface(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }       
        studio_surface = self.mpack.create_studio_surface(inputs)
        self.data['studio_surface'] = [studio_surface]     
 
    def make_model_usd(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        usd = self.mpack.create_model_usd(inputs, asset_ids=self.asset_ids)
        self.data['model_usd'] = [usd]    
        
    def make_uv_usd(self):   
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,            
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        usd = self.mpack.create_uv_usd(inputs, asset_ids=self.asset_ids)
        self.data['uv_usd'] = [usd]
        
    def make_surface_usd(self):
        inputs = {
            'node': 'model',
            # 'output_directory': self.publish_path,
            'output_directory': self.temp_pack_path,            
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            'force': True
            }        
        usd = self.mpack.create_surface_usd(inputs, asset_ids=self.asset_ids)
        self.data['uv_usd'] = [usd]
        
    def make_manifest(self):
        
        
        self.source_maya = bundle['source_file']
        self.caption = bundle['caption']
        self.version = bundle['version'] 
        self.thumbnail = bundle['thumbnail']
        self.type = bundle['type']
        self.tag = bundle['tag']
        self.description = bundle['description']   
        self.time_stamp = bundle['time_stamp']        
        
        self.publish_path = os.path.join(
            self.show_path,
            self.entity,
            self.caption,
            self.subfield,
            self.version
            )
        
                
        print self.data
        
        pass
    
    def make_root(self):
        if os.path.isdir(self.publish_path):
            self.reomve_dirname(self.publish_path)            
        os.makedirs(self.publish_path, 0755)
        self.set_time_stamp(self.publish_path)
        return self.publish_path
    
    def make_temp_root(self):        
        temp_pack_path = os.path.join(
            tempfile.gettempdir(), self.temp_entity)
        if os.path.isdir(temp_pack_path):
            self.reomve_dirname(temp_pack_path)           
        os.makedirs(temp_pack_path, 0755)
        self.set_time_stamp(temp_pack_path)
        return temp_pack_path
        
    def reomve_dirname(self, dirname):
        if not os.path.isdir(dirname):
            return
        os.chmod(dirname, 0777)
        try:
            shutil.rmtree(dirname)
        except Exception as OSError:
            print OSError

    def set_time_stamp(self, path):
        if not os.path.exists(path):
            return
        os.utime(path, (self.time_stamp, self.time_stamp)) 
              
    def copy_to(self, source):
        format = os.path.splitext(source)[-1]        
        target_path = os.path.join(
            self.publish_path, '{}{}'.format(self.caption, format))
        shutil.copy2(source, target_path)
        self.set_time_stamp(target_path)
        return target_path
    
    def at(self):
        
        import json
        from pymel import core
        
        attribute = core.PyNode('model.USD_UserExportedAttributesJson')
        
        data = {
            "scaption": {
                "usdAttrType": "primvar",
                "usdAttrName": "scaption",
                "interpolation": "uniform"
            },
            "hello": {
                "translateMayaDoubleToUsdSinglePrecision": True,
                "usdAttrType": "primvar",
                "usdAttrName": "hello",
                "interpolation": "uniform"
            }
        }

        attribute.set(json.dumps(data))        
          
