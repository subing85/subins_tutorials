import os
import shutil

from studio_usd_pipe.api import studioImage


class Asset(object):
    
    def __init__(self, subfield=None):
        
        self.subfield = subfield
        self.width, self.height = 640, 400
    
    def pack(self, bundle):        
        self.source_maya = bundle['source_file']
        self.publish_path = bundle['publish_path']
        self.caption = bundle['caption']        
        self.thumbnail = bundle['thumbnail']
        
        self.make_root(self.publish_path)
        
        self.make_maye()
        self.make_thumbnail()
        
        if self.subfield=='model':
            self.make_model()
            self.make_model_usd()
            self.make_model_active_usd()
            
        if self.subfield=='uv':
            self.make_uv()
            self.make_uv_usd()
            self.make_uv_active_usd()
            
        if self.subfield=='surface':
            self.make_surface()
            self.make_surface_usd()
            self.make_surface_active_usd()  
                      
        if self.subfield=='puppet':
            self.make_puppet()
            self.make_puppet_usd()
            self.make_puppet_active_usd()
                    
    def release(self, bundle, stamped_time):
        pass    
    
    def make_maye(self):
        target_path = self.copy_to(self.source_maya)
        return target_path
    
    def make_thumbnail(self):
        image = studioImage.ImageCalibration(imgae_file=self.thumbnail)
        image, image_path = image.set_studio_size(
            output_path=self.thumbnail,
            width=self.width,
            height=self.height
            )
        self.time_stamp(image_path)
        return image_path

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
        self.time_stamp(self.publish_path)
        return self.publish_path    

    def reomve_dirname(self, dirname):
        if not os.path.isdir(dirname):
            return
        os.chmod(dirname, 0777)
        try:
            shutil.rmtree(dirname)
        except Exception as OSError:
            print OSError

    def time_stamp(self, path):
        if not os.path.exists(path):
            return
        os.utime(path, (self.stamped_time, self.stamped_time)) 
              
    def copy_to(self, source):
        format = os.path.splitext(source)[-1]        
        target_path = os.path.join(
            self.publish_path, '{}{}'.format(self.caption, format))
        shutil.copy2(source, target_path)
        self.time_stamp(target_path)
        return target_path
          
