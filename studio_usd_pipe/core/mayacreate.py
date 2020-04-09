import json

from maya import OpenMaya

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
        
        contents = {}
        for node in model_nodes:
            node_contents = model_data[node]
            mfn_mesh = smodel.create_model(node, node_contents, replace=replace)
            contents.setdefault(node.split('|')[-1], mfn_mesh.parent(0))

        # create nurbs curve
        scurve = studioNurbscurve.Nurbscurve()
        curve_data = self.studio_data['curve']
        curve_nodes = scurve.sort_dictionary(curve_data)
        for node in curve_nodes:
            node_contents = curve_data[node]
            mfn_curve = scurve.create_curve(node, node_contents, replace=replace)
            contents.setdefault(node.split('|')[-1], mfn_curve.parent(0))
 
        # create transform
        transform_data = self.studio_data['transform']
        for node, node_contents in transform_data.items():
            mfn_transform = smodel.create_transform(node, node_contents, replace=replace)
            contents.setdefault(node.split('|')[-1], mfn_transform.object())
        
        # create hierarchy 
        locations = model_nodes + curve_nodes + transform_data.keys()
        stack = []
        for location in locations:
            nodes = location.split('|')[1:]
            for x in range(len(nodes)):
                if len(nodes)==x+1:
                    continue
                if [nodes[x+1], nodes[x]] in stack:
                    continue
                mfndag_child = OpenMaya.MFnDagNode(contents[nodes[x+1]])
                mfndag_parent = OpenMaya.MFnDagNode(contents[nodes[x]])
                smodel.set_parent(mfndag_child.fullPathName(), mfndag_parent.fullPathName())
                stack.append([nodes[x+1], nodes[x]])
    
    def uv(self, replace=True):
        smodel = studioModel.Model()
        uv_data = self.studio_data['mesh']
        for node, contenst in uv_data.items():
            mfn_mesh = smodel.create_uv(node, contenst)
    
    def surface(self, replace=False):
        '''
            from studio_usd_pipe.core import mayacreate
            path = '/venture/shows/batman/assets/batman/surface/1.0.0/batman.shader'
            mcreate = mayacreate.Create(path)
            mcreate.surface()
        '''     
        
        sshader = studioShader.Shader()
        surface_data = self.studio_data['surface']
        for node, contenst in surface_data.items():
            mfn_mesh = sshader.create_shadernet(node, contenst, replace=replace)        
    
    def puppet(self, replace=False):
        pass
    

        
        
    def read_json(self, path):
        data = None
        with open(path, 'r') as file:
            data = json.load(file)
        return data
        