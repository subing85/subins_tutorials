import json

from studio_usd_pipe.api import studioUsd
from studio_usd_pipe.api import studioModel
from studio_usd_pipe.api import studioShader
from studio_usd_pipe.api import studioNurbscurve

reload(studioUsd)
reload(studioModel)
reload(studioShader)
reload(studioNurbscurve)


class Create(object):
    
    def __init__(self, path):
        self.path = path
        self.studio_data = self.read_json(path)

       
    def model(self, replace=True):
        # create polygon mesh
        smodel = studioModel.Model()
        model_data = self.studio_data['mesh']
        model_nodes = smodel.sort_dictionary(model_data)
        for node in model_nodes:
            node_contents = model_data[node]
            dagpath_name = node.split('|')[-1]
            smodel.create_model(dagpath_name, node_contents, replace=replace)
            
            
        return
            

            
        # create nurbs curve
        scurve = studioNurbscurve.Nurbscurve()
        curve_data = self.studio_data['curve']
        curve_nodes = scurve.sort_dictionary(curve_data)
        for node in curve_nodes:
            node_contents = curve_data[node]
            dagpath_name = node.split('|')[-1]
            scurve.create_kcurve(dagpath_name, node_contents)
        
        # create groups        
        locations = model_nodes + curve_nodes        
        for location in locations:
            nodes = location.split('|')[1:]            
            for node in nodes:
                if smodel.object_exists(node):
                    continue
                #children = smodel.get_children(node)
                #for x in range(children.length()):
                #    smodel.unparent(children[x])
                #smodel.remove_node(node)
                smodel.create_group(node)

        # create hierarchy
        stack = []
        for location in locations:
            nodes = location.split('|')[1:]
            for x in range(len(nodes)):
                if len(nodes)==x+1:
                    continue
                if [nodes[x+1], nodes[x]] in stack:
                    continue                    
                smodel.set_parent(nodes[x+1], nodes[x])
                stack.append([nodes[x+1], nodes[x]])

    
    def uv(self, replace=False):
        pass
    
    
    def surface(self, replace=False):
        pass
    
    
    def puppet(self, replace=False):
        pass
    

        
        
    def read_json(self, path):
        data = None
        with open(path, 'r') as file:
            data = json.load(file)
        return data
        