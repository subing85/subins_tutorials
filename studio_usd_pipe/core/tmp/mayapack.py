import os
import json
import time

from datetime import datetime

from maya import OpenMaya

from studio_usd_pipe import resource
from studio_usd_pipe.core import image
from studio_usd_pipe.api import studioUsd
from studio_usd_pipe.api import studioMaya
from studio_usd_pipe.api import studioModel
from studio_usd_pipe.api import studioShader
from studio_usd_pipe.api import studioNurbscurve

reload(studioUsd)
reload(studioMaya)
reload(studioModel)
reload(studioShader)
reload(studioNurbscurve)


class Pack(studioMaya.Maya):
    
    def __init__(self):
        # studioMaya.Maya.__init__(self)  
        super(Pack, self).__init__()
              
        self.model = studioModel.Model()
        self.shader = studioShader.Shader()
        self.nurbscurve = studioNurbscurve.Nurbscurve()   
        self.nested_bundle = {}
        self.flatted_bundle = {}
    
    def has_validate_model(self, node):  
        top_nodes = self.extract_top_transforms()
        if top_nodes.length() == 1:
            if top_nodes[0].partialPathName() != node:
                return False
            return True        
        return False        
        
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
        if os.path.exists(path):      
            if not force:
                return True          
            os.chmod(path, 0777)
            try:
                os.remove(path)
                return True
            except Exception as error:
                return False
        else:
            return True
        
    def create_model(self, inputs, force=False):        
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
                'slocation': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'sdescription': 'test publish',
                'node': 'model',
                'world': 'world'
                }                       
            mpack.create_model(inputs)      
        ''' 
        # make asset id
        input_data = self.make_packing_arguments(inputs)
        if not force:
            valid = self.has_validate_model(inputs['node'])
            if valid:                
                node_mobject = self.get_mobject(inputs['node'])
                self.create_maya_id(node_mobject, input_data)
                return
            
        # remove depend nodes
        depend_nodes = self.extract_depend_nodes(default=False)
        for x in range(depend_nodes.length()):
            self.remove_node(depend_nodes[x]) 
        self.remove_nodes(depend_nodes)                
        # make model group             
        mesh_mobjects = self.extract_transform_primitive(OpenMaya.MFn.kMesh, shape=False)
        
        model_dag_node = self.create_group(inputs['node'])        
        # make geometry hierarchy  
        for x in range (mesh_mobjects.length()):
            self.set_locked(mesh_mobjects[x].node(), attributes=None, locked=False)
            self.disconnect_chanelbox(mesh_mobjects[x].node())
            self.set_parent(mesh_mobjects[x], model_dag_node.object())
            # assigin default shader
            self.shader.assign_shading_engine(mesh_mobjects[x], shading_group=None)  
        # remove unwanted dag nodes    
        trans_dagpath_array = self.extract_top_transforms(default=False)
        for x in range (trans_dagpath_array.length()):
            if trans_dagpath_array[x].node() == model_dag_node.object():
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
        # create asset id
        input_data = self.make_packing_arguments(inputs)
        self.create_maya_id(model_dag_node.object(), input_data)
        # OpenMaya.MGlobal.selectByName(model_dag_node.fullPathName())
        OpenMaya.MGlobal.clearSelectionList()
        self.set_perspective_view()
    
    def create_thumbnail(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            
            input_data = {
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'thumbnail': '/local/references/images/batman_art.jpg',
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
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        
        if inputs['thumbnail']:        
            #if inputs['standalone']:
                     
            image.image_resize(
                inputs['thumbnail'],
                output_path,
                inputs['width'],
                inputs['height'],
                )             
        else:
            OpenMaya.MGlobal.clearSelectionList()
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
                'force': True       
                }     
            mpack.create_studio_model(inputs)    
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.model'.format(inputs['caption'])
            )                 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)    
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.model.get_model_data(mobject)
        curve_data = self.nurbscurve.get_curve_data(mobject)
        transform_data = self.model.get_transform_data(mobject)
        final_data = {
            'mesh': mesh_data,
            'curve': curve_data,
            'transform': transform_data
            } 
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
        return output_path       

    def create_studio_uv(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/uv/0.0.0/',
                'caption': 'batman',
                'force': True
                }     
            mpack.create_studio_uv(inputs)    
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.uv'.format(inputs['caption'])
            ) 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.model.get_uv_data(mobject)
        final_data = {
            'mesh': mesh_data,
            }      
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
        return output_path   
    
    def create_studio_surface(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/surface/0.0.0/',
                'caption': 'batman',
                'force': True
                }     
            mpack.create_studio_surface(inputs)    
        '''            
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.shader'.format(inputs['caption'])
            )         
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path) 
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.shader.get_surface_data(mobject)
        final_data = {
            'surface': mesh_data,
            }  
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
        return output_path
    
    def create_source_images(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'publish_directory': '/venture/shows/my_hero/assets/batman/surface/0.0.0/',
                'output_directory': '/usr/tmp/studio_asset'
                'caption': 'batman',
                'force': True       
                }     
            mpack.create_source_images(inputs)          
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.sourceimage'.format(inputs['caption'])
            )  
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        temp_source_image_path = os.path.join(
            inputs['output_directory'], 'source_images')                       
        source_image_path = os.path.join(
            inputs['publish_directory'], 'source_images')
        mobject = self.get_mobject(inputs['node'])
        input_data = self.shader.get_source_image_data(mobject)
        output_data = self.shader.set_source_images(input_data, temp_source_image_path, source_image_path)
        lowres_data = self.shader.create_lowres_source_images(input_data, temp_source_image_path)  
        final_data = {
            'input': input_data,
            'output': output_data,
            'lowres': lowres_data
            } 

        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
        source_images = []        
        for node in output_data:
            for attribute in output_data[node]:
                source_images.append(output_data[node][attribute]['temp_value'])
        for node in lowres_data:
            for attribute in lowres_data[node]:
                source_images.append(lowres_data[node][attribute]['value']) 
        return output_path, source_images
    
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
                'force': True
                }     
            mpack.create_maya(input_data)        
        '''                
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.ma'.format(inputs['caption'])
            ) 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        
        print  '\nsubin', inputs['node']               
        self.export_selected(inputs['node'], output_path, force=inputs['force'])
        return output_path
    
    
    def create_surface_maya(self, inputs):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            input_data = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'force': True
                }     
            mpack.create_surface_maya(input_data)        
        '''                
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.ma'.format(inputs['caption'])
            ) 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        
        mobject = self.shader.get_mobject(inputs['node'])
        
        shading_engines = self.shader.get_scene_shading_engines(mobject)
        
        print 'shading_engines\t', shading_engines
        
                  
        self.export_selected(shading_engines, output_path, force=inputs['force'])
        return output_path
    
    
    
    def get_asset_id_data(self, root, ids):
        data = {}
        if not ids:
            return data
        for index, id in enumerate(ids):
            mplug = self.get_mplug('{}.{}'.format(root, id))
            id_value = mplug.asString()
            data[id] = {
                'order': index,
                'value': id_value
            }
        return data
    
    def create_model_usd(self, inputs, asset_ids=None):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/model/0.0.0/',
                'caption': 'batman',
                'force': True                
                }     
            mpack.create_model_usd(inputs)       
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.usd'.format(inputs['caption'])
            )         
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path) 
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.model.get_model_data(mobject)
        curve_data = self.nurbscurve.get_curve_data(mobject)
        asset_ids = self.get_asset_id_data(inputs['node'], asset_ids)
        final_data = {
            'mesh': mesh_data,
            'curve': curve_data,
            'asset_id': asset_ids
            }        
        susd = studioUsd.Susd(path=output_path)                
        susd.create_model_usd(inputs['node'], final_data)
        return output_path    

    def create_uv_usd(self, inputs, asset_ids=None):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/uv/0.0.0/',
                'caption': 'batman',
                'force': True                
                }     
            mpack.create_uv_usd(inputs)       
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.usd'.format(inputs['caption'])
            )         
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path) 
        mobject = self.get_mobject(inputs['node'])
        mesh_data = self.model.get_uv_data(mobject)
        asset_ids = self.get_asset_id_data(inputs['node'], asset_ids)
        final_data = {
            'mesh': mesh_data,
            'asset_id': asset_ids
            }        
        susd = studioUsd.Susd(path=output_path)                
        susd.create_uv_usd(inputs['node'], final_data)
        return output_path
        
    def create_surface_usd(self, inputs, asset_ids=None):
        '''
            import time
            from studio_usd_pipe.core import mayapack
            reload(mayapack)
            mpack = mayapack.Pack()
            inputs = {
                'node': 'model',
                'output_directory': '/venture/shows/my_hero/assets/batman/surface/0.0.0/',
                'caption': 'batman',
                'force': True                
                }     
            mpack.create_surface_usd(inputs)       
        '''
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.usd'.format(inputs['caption'])
            )         
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path) 
        mobject = self.get_mobject(inputs['node'])
        surface_data = self.shader.get_surface_data(mobject)
        asset_ids = self.get_asset_id_data(inputs['node'], asset_ids)
        final_data = {
            'surface': surface_data,
            'asset_id': asset_ids            
            }       
        susd = studioUsd.Susd(path=output_path)                
        susd.create_surface_usd(inputs['node'], final_data)
        return output_path

    def create_manifest(self, inputs):
        output_path = os.path.join(
            inputs['output_directory'],
            '{}.manifest'.format(inputs['caption'])
            )                 
        premission = self.pack_exists(output_path, inputs['force'])
        if not premission:
            raise IOError('Cannot save, already file found <%s>' % output_path)
        inputs['date'] = time.strftime(
            '%Y/%d/%B - %I/%M/%S/%p', time.gmtime(inputs['time_stamp']))
        data = {}
        inputs.pop('output_directory')
        inputs.pop('time_stamp')        
        final_data = {
            "created_by": "subin gopi",
            "author": "Subin. Gopi (subing85@gmail.com)",
            "#copyright": "(c) 2019, Subin Gopi All rights reserved.",
            "last_modified": inputs['date'],
            "description": "publish manifest",
            "warning": "# WARNING! All changes made in this file will be lost!",
            "enable": True,
            "type": "manifest",
            'data': inputs
            }        
        with (open(output_path, 'w')) as content:
            content.write(json.dumps(final_data, indent=4))
        return output_path

    

