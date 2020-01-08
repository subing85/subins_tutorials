import math
import json

import os

from datetime import datetime

from maya import OpenMaya


from studio_usd_pipe import resource


# from studio_usd_pipe.api import studioMaya
from studio_usd_pipe.api import studioModel
from studio_usd_pipe.api import studioShader
from studio_usd_pipe.api import studioNurbscurve
from studio_usd_pipe.api import studioUsd

from studio_usd_pipe.core import image
from __builtin__ import True

reload(studioModel)
reload(studioShader)
reload(studioNurbscurve)
reload(studioUsd)


class Pack(studioModel.Model):
    
    def __init__(self):
        studioModel.Model.__init__(self)
        self.shader = studioShader.Shader()
        self.nurbscurve = studioNurbscurve.Nurbscurve()        
        
        
        self.nested_bundle = {}
        self.flatted_bundle = {}
        
    def make_packing_arguments(self, arguments):
        input_data = resource.getAssetIDData()        
        for k, v in input_data.items():            
            if k not in arguments:
                continue            
            if k == 'smodified':
                continue
            input_data[k]['value'] = arguments[k]         
        dt_object = datetime.fromtimestamp(arguments['smodified'])
        input_data['smodified']['value'] = dt_object.strftime('%Y:%d:%B-%I:%M:%S:%p')          
        return input_data
    
    def pack_exists(self, path, force):    
        if os.path.isfile(path):      
            if not force:
                return False          
            os.chmod(path, 0777)
            try:
                os.remove(path)
                return True
            except Exception as error:
                return False
        else:
            return True    
               
        
    def create_model(self, inputs):        
        '''
        :example
            import time
            from studio_usd_pipe.core import mayapack
            mpack = mayapack.Pack()        
            inputs = {
                'sentity': 'asset',
                'scaption': 'batman',
                'stype': 'intractive',
                'stag': 'character',
                'sversion': '0.0.0',
                'smodified': time.time(),
                'spath': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'sdescription': 'test publish'
                'node': 'model',
                'world': 'world'
                }                       
            mpack.create_model(inputs)      
        '''     
        # remove depend nodes
        depend_nodes = self.extract_depend_nodes(default=False)
        for x in range(depend_nodes.length()):
            self.remove_node(depend_nodes[x]) 
        self.remove_nodes(depend_nodes)
        
        # make model group             
        mesh_mobjects = self.extract_transform_primitive(OpenMaya.MFn.kMesh)
        model_dag_node = self.create_group(inputs['node'])        
        # make geometry hierarchy  
        for x in range (mesh_mobjects.length()):
            print mesh_mobjects[x].fullPathName()
            self.set_locked(mesh_mobjects[x].node(), attributes=None, locked=False)
            
            self.disconnect_chanelbox(mesh_mobjects[x].node())
            self.set_parent(mesh_mobjects[x], model_dag_node.object())
            # assigin default shader
            self.shader.assign_shading_engine(mesh_mobjects[x], shading_group=None)  
               
        # remove unwanted dag nodes    
        trans_dagpath_array= self.extract_top_transforms(default=False)
        for x in range (trans_dagpath_array.length()):
            if trans_dagpath_array[x].node()==model_dag_node.object():
                continue                       
            self.remove_node(trans_dagpath_array[x].node())
        # self.remove_nodes(transform_mobjects)        
            
        # reset transforms
        for x in range (mesh_mobjects.length()):
            self.delete_history(mesh_mobjects[x])
            self.freeze_transformations(mesh_mobjects[x])
            self.set_default_position(mesh_mobjects[x].node())
            
        # create world control   
        world_dependency_node = self.nurbscurve.create_world(model_dag_node, parent=True) 
        # set the name
        model_dag_node.setName(inputs['node'])
        world_dependency_node.setName(inputs['world'])
        # make asset id
        input_data = self.make_packing_arguments(inputs)
        self.create_maya_id(model_dag_node.object(), input_data)
        # OpenMaya.MGlobal.selectByName(model_dag_node.fullPathName())
        self.set_perspective_view()
        OpenMaya.MGlobal.clearSelectionList()
        
    
    def create_thumbnail(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            
            input_data = {
                'standalone': False,            
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'thumbnail': '/local/references/images/batman_art.jpg',
                'time_stamp': time.time(),
                'width': 1024,
                'height': 1024.
                'force': True
                }     
            mpack.create_thumbnail(input_data)         
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.png'.format(inputs['caption'])
            )
        
        print   '\t',    inputs['force'], 
        premission = self.pack_exists(output_path, inputs['force'])
        print   '\t',    premission, 
       
        if not premission:
            raise IOError('Cannot save, already file found <%s>'%output_path)          
        if inputs['standalone']:            
            image.image_resize(
                inputs['thumbnail'],
                output_path,
                inputs['width'],
                inputs['height'],
                )             
        else:
            output_path, w, h = self.vieport_snapshot(
                output_path=output_path,
                width=inputs['width'],
                height=inputs['height'],
                )            
        return output_path
        
    def create_studio_model(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'time_stamp': time.time(),
                }     
            mpack.create_studio_model(inputs)    
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.model'.format(inputs['caption'])
            ) 
                
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>'%output_path)    
                       
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.get_data(mobject)
        curve_data = self.nurbscurve.get_data(mobject)
        final_data = {
            'mesh': mesh_data, 
            'curve': curve_data
            }      
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
            os.utime(output_path, (inputs['time_stamp'], inputs['time_stamp']))           
        return output_path        

    def create_model_usd(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            
            inputs = {
                ''node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'time_stamp': time.time(),
                }     
            mpack.create_model_usd(inputs)       
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.usd'.format(inputs['caption'])
            )         
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>'%output_path) 
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.get_data(mobject)
        curve_data = self.nurbscurve.get_data(mobject)
        final_data = {
            'mesh': mesh_data, 
            'curve': curve_data
            }        
        susd = studioUsd.Susd(path=output_path)                
        susd.create_model_usd(inputs['node'], final_data, inputs['time_stamp'])
        return output_path    
    
    def create_maya(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            
            input_data = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'force': True,
                'time_stamp': time.time(),
                }     
            mpack.create_maya(input_data)        
        '''                
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.ma'.format(inputs['caption'])
            ) 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>'%output_path)                 
        self.export_selected(inputs['node'], output_path, force=inputs['force'])
        return output_path


















                   
       



