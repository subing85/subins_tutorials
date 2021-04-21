
# sfrom pymel import core


from maya import OpenMaya

from renderLibrary.api import mayaRender




def create_render_layer(data):
    mr = mayaRender.Connect()
    layers = {}
    for name, v in data.items():
        layer = mr.createRenderLayer(name)
        for attribute, contents in v.items():
            mr.setAttributeValue(layer, attribute, contents['typed'], contents['value'])
        layers[name] = layer
    
    return layers


def create_aovs(data, remove=False):    
    mr = mayaRender.Connect()
    
    _aovs = {}
    
    for node, contents in data.items():   
        if remove:     
            if mr.objectExists(node):
                mr.removeNode(node)
        aov = mr.createAov(node, contents['attributes']['name']['value'])
        # set attributes
        if contents.get('attributes'):
            mr.setAttributes(aov, contents['attributes'])
            
        #=======================================================================
        # if contents.get('outputs'):
        #     mr.setConnections(node, contents['outputs'], typed='input')
        #=======================================================================        
        

  
def set_override(data):    
    
    for node, attribute in data.items():
        print node
