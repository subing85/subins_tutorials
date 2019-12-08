
from studio_usd_pipe.module import publish

reload(publish)

class Connect(object):
    
    def __init__(self, caption, **kwargs):
        self.caption = caption
        self.kwargs = kwargs        
        
    def pack(self, type):
        pass

    def model(self):           
        path, bundles = self.pack('model')   
        release = publish.model()        
        release.relase(path, bundles)
    
    def uv(self):
        publish.uv()
    
    def surface(self):
        publish.surface()
    
    def primary_layout(self):
        publish.layout()        
    
    def layout(self):
        publish.layout()
    
    def animation(self):
        publish.animation()
    
    def render(self):
        publish.render()
    
    def composting(self):
        publish.composting()
