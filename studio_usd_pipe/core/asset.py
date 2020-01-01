import os
import shutil


from studio_usd_pipe.api import studioImage
from studio_usd_pipe.core import mayapack
from studio_usd_pipe.core import preference


class Asset(object):
    
    def __init__(self, subfield=None):       
        
        self.standalone = False
        
        self.subfield = subfield
        self.width, self.height = 640, 400
        self.entity = 'assets'
        
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
            'version': '0.0.0',
            'caption': 'batman',
            'thumbnail': '/local/references/images/btas_batmodel_03.jpg',
            'time_stamp': time.time()
            }        
        asset.pack(bundle)          
        '''
             
        self.source_maya = bundle['source_file']
        self.caption = bundle['caption']
        self.version = bundle['version'] 
        self.thumbnail = bundle['thumbnail']
        self.time_stamp = bundle['time_stamp']
        self.type = bundle['time_stamp']
        self.tag = bundle['tag']
        self.description = bundle['description']        
        
        self.publish_path = os.path.join(
            self.show_path,
            self.entity,
            self.caption,
            self.subfield,
            self.version
            )        
        self.make_root()
        
        if self.subfield == 'model':
            self.make_maya_model()
            self.make_thumbnail()
            self.make_studio_model()                       
            self.make_model_usd()
            self.make_model_active_usd()
            self.make_model()
            
        if self.subfield == 'uv':
            self.make_maya_model()
            self.make_thumbnail()            
            self.make_uv()
            self.make_uv_usd()
            self.make_uv_active_usd()
            
        if self.subfield == 'surface':
            self.make_maya_model()
            self.make_thumbnail()            
            self.make_surface()
            self.make_surface_usd()
            self.make_surface_active_usd()  
                      
        if self.subfield == 'puppet':
            self.make_maya_model()
            self.make_thumbnail()            
            self.make_puppet()
            self.make_puppet_usd()
            self.make_puppet_active_usd()

                    
    def release(self, bundle, stamped_time):
        pass    
    
    
    def make_maya_model(self):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()        
            model_id_data = {
                'sentity': 'asset',
                'scaption': 'batman',
                'stype': 'intractive',
                'stag': 'character',
                'sversion': '0.0.0',
                'smodified': time.time(),
                'spath': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'sdescription': 'test publish'
                }                       
            mpack.create_model(model_id_data)        
        '''
        input_data = {
            'sentity': self.entity,
            'scaption': self.caption,
            'stype': self.type,
            'stag': self.tag,
            'sversion': self.version,
            'smodified': self.time_stamp,
            'spath': self.publish_path,
            'sdescription': self.description
            }        
        self.mpack.create_model(input_data)
         
    def make_thumbnail(self):
        input_data = {
            'standalone': self.standalone,            
            'publish_path': self.publish_path,
            'caption': self.caption,
            'thumbnail': self.thumbnail,
            'time_stamp': self.time_stamp,
            'width': 1024,
            'height': 1024
            } 
        self.thumbnail = self.mpack.create_thumbnail(input_data)     

    def make_studio_model(self):
        input_data = {
            'publish_path': self.publish_path,
            'caption': self.caption,
            'time_stamp': self.time_stamp,
            }       
        self.studio_model = self.mpack.create_studio_model(input_data)
 
    
    def make_maye(self):
        target_path = self.copy_to(self.source_maya)
        return target_path
    

        
        
         
    


    def make_source_images(self):
        pass
    
    def make_model(self):
        pass
    
    def make_uv(self):
        pass
    
    def make_surface(self):
        pass
    
    def make_puppet(self):
        pass
    
    def make_model_usd(self):
        pass
    
    def make_uv_usd(self):
        pass
        
    def make_surface_usd(self):
        pass  
    
    def make_puppet_usd(self):
        pass    
    
    def make_model_active_usd(self):
        pass

    def make_uv_active_usd(self):
        pass
        
    def make_surface_active_usd(self):
        pass  
    
    def make_puppet_active_usd(self):
        pass
    
    def make_root(self):
        if os.path.isdir(self.publish_path):
            self.reomve_dirname(self.publish_path)            
        os.makedirs(self.publish_path, 0755)
        self.set_time_stamp(self.publish_path)
        return self.publish_path    

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
          
