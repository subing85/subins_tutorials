import copy

from pprint import pprint
from maya import OpenMaya
from maya import OpenMayaAnim

import studioMaya

from smartDeform.modules import studioMaya
reload(studioMaya)


class Skincluster(studioMaya.Maya):

    def __init__(self, **kwargs):
        self.source_geometry = None
        self.target_geometrys = None
        self.source_deformers = None
        self.target_deformers = None

        if 'source_geometry' in kwargs:
            self.source_geometry = kwargs['source_geometry']
        if 'target_geometrys' in kwargs:
            self.target_geometrys = kwargs['target_geometrys']
        if 'source_deformers' in kwargs:
            self.source_deformers = kwargs['source_deformers']
        if 'target_deformers' in kwargs:
            self.target_deformers = kwargs['target_deformers']

    def create(self, name, clear=False):
        name = name.split('|')[-1]
        if clear:
            OpenMaya.MGlobal.clearSelectionList() 
            
        mcommand_result = OpenMaya.MCommandResult()
        OpenMaya.MGlobal.executeCommand('joint -p 0 0 0 -n %s' % name, mcommand_result, True, True)
        OpenMaya.MGlobal.clearSelectionList()
        result = []
        mcommand_result.getResult(result)        
        return result[0].encode()         
          
            
        '''          
        mfn_dag_node = OpenMaya.MFnDagNode()
        mfn_dag_node.create('joint')
        mfn_dag_node.setName(name)
        joint_dag_path = OpenMaya.MDagPath()
        mfn_dag_node.getPath(joint_dag_path)
        return joint_dag_path, joint_dag_path.fullPathName().encode()
        '''
    

    def get_weight(self, joint_dag_path):        
        m_skinclusters = self.getDependences(joint_dag_path, OpenMaya.MFn.kSkinClusterFilter)        
        skin_cluster_data = {}
        
        for index in range (m_skinclusters.length()):      
            m_dag_path, weights, memberships = self.read_weight(m_skinclusters[index], joint_dag_path)            
            weight = {}
            weight['weights'] = weights
            weight['memberships'] = memberships            
            skin_cluster_data.setdefault(m_dag_path.fullPathName(), weight)
        
        x, y, z = self.getJointPosition(joint_dag_path) 
        plug = self.getPlug(joint_dag_path.fullPathName(), 'liw')
        
        data = {}
        data['geometry'] = skin_cluster_data
        data['position'] = [x, y, z]
        data['locked'] = plug.asBool()
  
        return data            

    def get_weights(self, joints):
        skincluster_weights = {}        
        for each_dag_path in joints:       
            data  = self.get_weight(each_dag_path)            
            joint_handle = each_dag_path.fullPathName().encode()            
            skincluster_weights.setdefault(joint_handle, data)       
        return skincluster_weights

    def set_weight(self, joint_dag_path, joint_data):        
        geometry_data = joint_data['geometry']
        position = joint_data['position']
        locked = joint_data['locked']           
        
        plug = self.getPlug(joint_dag_path.fullPathName(), 'liw') 
        plug.setBool(False) 
        self.write_weight(joint_dag_path, geometry_data)
        
        if locked:        
            plug.setBool(locked) 

    def set_weights(self, data):        
        for each_joint, joint_data in data.items(): 
            joint_dag_path = self.getDagPath(each_joint)            
            self.set_weight(joint_dag_path, joint_data)

    def read_weight(self, m_skincluster, joint_dag_path):
        '''       
        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skincluster) 
               
        selection_list = OpenMaya.MSelectionList()
        m_float_array = OpenMaya.MFloatArray()        
        mfn_skincluster.getPointsAffectedByInfluence(joint_dag_path, selection_list, m_float_array)
        
        m_dag_path = OpenMaya.MDagPath()
        selection_list.getDagPath(0, m_dag_path)
        
        return m_dag_path, m_float_array
        '''

        mfn_skincluster = OpenMayaAnim.MFnSkinCluster(m_skincluster)        
        selection_list = OpenMaya.MSelectionList()
        m_float_array = OpenMaya.MFloatArray() 
        mfn_skincluster.getPointsAffectedByInfluence(joint_dag_path, selection_list, m_float_array)   
        
        deformer_set = mfn_skincluster.deformerSet()
        mfn_set = OpenMaya.MFnSet(deformer_set)
        mfn_set.getMembers(selection_list, True)

        m_object = OpenMaya.MObject()
        m_dag_path = OpenMaya.MDagPath()        
        selection_list.getDagPath(0, m_dag_path, m_object)
        
        # joint_index = mfn_skincluster.indexForInfluenceObject(joint_dag_path)
        joint_index = self.findxIndexFromSkincluster(mfn_skincluster, joint_dag_path)        
        
        mit_geometry = OpenMaya.MItGeometry(m_dag_path)
        membership_list = []
        weight_list = []
        
        while not mit_geometry.isDone():
            component = mit_geometry.currentItem()
            float_array = Openclear=FalseMaya.MFloatArray()            
            membership = self.hasMembership(m_skincluster, m_dag_path, component)
                        
            if not m_float_array:
                float_array = [0, 0, 0]
            else:
                if membership:
                    mfn_skincluster.getWeights(m_dag_path, component, joint_index, float_array)
                else:
                    float_array = [0, 0, 0]
                                
            membership_list.append(membership)
            weight_list.append(float_array[0])   
                     
            mit_geometry.next()        
        return m_dag_path, weight_list, membership_list
    
    def write_weight(self, joint_dag_path, geometry_data):        
        for each_geometry,  geometrys in geometry_data.items():            
            weights = geometrys['weights']
            # memberships = geometrys['memberships']
            
            geometry_dag_path = self.getDagPath(each_geometry)
            skincluster_mobjects = self.getDeformerNodes(geometry_dag_path, OpenMaya.MFn.kSkinClusterFilter)
            
            if not skincluster_mobjects:
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find skincluster \"%s\"' % each_geometry.encode())                
                continue
            
            if not skincluster_mobjects.length():
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find skincluster \"%s\"' % each_geometry.encode())                
                continue
                        
            mit_mesh_vertex = OpenMaya.MItMeshVertex(geometry_dag_path.node())
            vertexs = range (mit_mesh_vertex.count())
                                                  
            self.setSkinclusterWeights(skincluster_mobjects[0], joint_dag_path, geometry_dag_path, vertexs, weights)
            # print       joint_dag_path.fullPathName()

    def combine_weights(self, joint_dag_paths):
        weights_data = {}
        memberships_data = {}  
        for each_joint in joint_dag_paths:      
            weight_data = self.get_weight(each_joint)
            
            for each_geometry, geometry_data in weight_data['geometry'].items():
                weights = geometry_data['weights']
                memberships = geometry_data['memberships'] 
                
                weights_data.setdefault(each_geometry, []).append(weights)
                memberships_data.setdefault(each_geometry, []).append(memberships)

        geometry_data = {}                
        for index in range (len(weights_data)):            
            geometry = weights_data.keys()[index]         
            weights = {'weights': weights_data[geometry]}
            memberships = {'memberships': memberships_data[geometry]}            
            geometry_data.setdefault(geometry, weights)
            geometry_data[geometry].update(memberships)
         
        combine_data = {}                
        for each_geometry, geometry_weights in geometry_data.items():            
            empty_weights, empty_memberships = self.createEmptyWeights(each_geometry)
                      
            for index in range(len(geometry_weights['weights'])):
                current_weights = geometry_weights['weights'][index]
                current_memberships = geometry_weights['memberships'][index]      
                                    
                for x in range (len(current_weights)):                                        
                    if current_weights[x]>1:
                        empty_weights[x] = 1                        
                    empty_weights[x] += current_weights[x]                    
                    if current_memberships[x]:                        
                        empty_memberships[x] = True
            
            combine_weights = {'weights': empty_weights}            
            combine_memberships = {'memberships': empty_memberships}                          
            combine_data.setdefault(each_geometry, combine_weights)
            combine_data[each_geometry].update(combine_memberships)              
        
        position = self.getCenterPosition(joint_dag_paths, 'skincluster')        
        joint_dag_path = self.create('combine_joint')
        self.setJointPosition(joint_dag_path, position)
         
        combine_datas = {}
        combine_datas['geometry'] = combine_data
        combine_datas['position'] = position
        combine_datas['locked'] = False

        self.addInfluence(joint_dag_path, combine_data.keys())
        
        self.set_weight(joint_dag_path, combine_datas) 

    def copy_weight(self, source_joint, target_joint):
        pass
    
    def copy_weights(self, source_joint, target_joint):       
        weight_data = self.get_weight(source_joint)  
        self.set_weight(target_joint, weight_data)        
    
    def create_mirror_flip(self, joint_dag_paths, axis, tag):
        for index in range (joint_dag_paths.length()):            
            position = self.getJointPosition(joint_dag_paths[index])            
            weight_data = self.get_weight(joint_dag_paths[index])

            mirror_position = position[0]*axis[0], position[1]*axis[1],  position[2]*axis[2]
            symmetry_weights = self.get_flip_weights(weight_data, axis)
               
            joint_dag_path = self.create('%s_joint' % tag)            
            target_position = mirror_position
            
            if tag == 'mirror':
                proxy_position = [1, 1, 1]
                proxy_position[axis.index(-1)] = 0             
                target_position = [mirror_position[0]*proxy_position[0], mirror_position[1]*proxy_position[1],
                                   mirror_position[2]*proxy_position[2]] 
                
            self.setJointPosition(joint_dag_path, target_position)
            
            target_weights = symmetry_weights
            if tag == 'mirror':
                target_weights = self.merge_weights(weight_data['geometry'], symmetry_weights)
            
            print target_weights
            
            target_datas = {}
            target_datas['geometry'] = target_weights
            target_datas['position'] = mirror_position
            target_datas['locked'] = False
            
            self.addInfluence(joint_dag_path, target_weights.keys())
            self.set_weight(joint_dag_path, target_datas)            
                
    def get_flip_weights(self, geometry_data, axis):
        symmetry_weights = copy.deepcopy(geometry_data['geometry'])        
        for each_geometry, weights_data in geometry_data['geometry'].items():            
            geometry_dag_path = self.getDagPath(each_geometry)          
            memberships = weights_data['memberships']
            weights = weights_data['weights']
            for index in range(len(weights)):               
                symmetry_vertex_id = self.get_symmetry_vertex(geometry_dag_path, index, axis)
                symmetry_weights[each_geometry]['weights'][symmetry_vertex_id] = weights[index]
                symmetry_weights[each_geometry]['memberships'][symmetry_vertex_id] = memberships[index]

        return symmetry_weights
    
    def merge_weights(self, weight_a, weight_b):        
        merge_weight_data = copy.deepcopy(weight_a)        
        for each_geometry, geometry_data in weight_a.items():    
            weights_a = geometry_data['weights']
            memberships_a = geometry_data['memberships']
            
            for index in range (len(weights_a)):       
                weight_index_b = weight_b[each_geometry]['weights'] 
                membership_index_b = weight_b[each_geometry]['memberships'] 
                
                merge_weight = weights_a[index] + weight_index_b[index]
                if merge_weight>1:
                    merge_weight = 1
                
                current_memberships = True                    
                if not memberships_a[index] and not membership_index_b[index]:    
                    current_memberships = False
                    
                merge_weight_data[each_geometry]['weights'][index] = merge_weight     
                merge_weight_data[each_geometry]['memberships'][index] = current_memberships
                
        return merge_weight_data  

    def soft_selection(self):
        dag_paths, memberships, weights = self.getWeightsFromSelection()        
        if not dag_paths:
            return
        
        if not self.target_deformers:
            x, y, z = self.get_center_of_selection()
            joint = self.create('soft_selection_joint', clear=True)
            self.setJointPosition(joint, [x, y, z])            
            self.addInfluence(joint, self.target_geometrys)            
            self.target_deformers = [joint]            
    
        for each_joint in self.target_deformers:  
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(each_joint, each_geometry, weights[0])
                

    def blend_shape(self):
        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])        
        for index in range(loop):
            weights = self.getWeightsFromEnvelope(self.source_geometry, self.source_geometry, self.source_deformers[index])            
            _targt_deformers = self.target_deformers[index]
            if not self.target_deformers[index]:
                x, y, z = self.get_center_of_weights(self.source_geometry, weights)
                name = '%s_blend_shape_joint' % self.source_deformers[index].replace('.', '_')                
                joint = self.create(name, clear=True)
                self.setJointPosition(joint, [x, y, z])            
                self.addInfluence(joint, self.target_geometrys)            
                _targt_deformers = joint               
            for each_geometry in self.target_geometrys:
                self.setSkinclusterWeights(_targt_deformers, each_geometry, weights)                   

    def wire(self):
        self.to_specific_deformer('wire')

    def lattice(self):
        self.to_specific_deformer('lattice')

    def cluster(self):
        self.wire()

    def to_skincluster(self):
        pass
    
    def to_specific_deformer(self, tag):
        if not self.target_deformers:
            self.target_deformers = []
            for x in range(len(self.source_deformers)):
                self.target_deformers.append(None)
        loop = min([len(self.target_deformers), len(self.source_deformers)])
        source_deformer_dag_path = OpenMaya.MDagPathArray()
        
        for index in range(loop):
            source_dag_path = self.getDagPath(self.source_deformers[index])
            source_deformer_dag_path.append(source_dag_path)
            
        for index in range(source_deformer_dag_path.length()):
            source_dag_path = source_deformer_dag_path[index]
            if source_dag_path.hasFn(OpenMaya.MFn.kCurve):  # to check to curve
                curve_weights = self.getWeightsFromCurve(source_dag_path, self.source_geometry)
                for k, v in curve_weights.items():
                    name = '%s_%s_%s_joint' % (self.source_deformers[index], k, tag)
                    joint = self.create(name, clear=True)
                    self.setJointPosition(joint, v['position'])
                    self.addInfluence(joint, self.target_geometrys)            
                    for each_geometry in self.target_geometrys:                    
                        self.setSkinclusterWeights(joint, each_geometry, v['weights'])                   

            elif source_dag_path.hasFn(OpenMaya.MFn.kTransform) or source_dag_path.hasFn(OpenMaya.MFn.kJoint):
                _targt_deformers = self.target_deformers[index]
                
                if source_dag_path.hasFn(OpenMaya.MFn.kJoint):
                    children = self.getChildren(source_dag_path)
                elif source_dag_path.hasFn(OpenMaya.MFn.kTransform):
                    children = self.getChildren(source_dag_path, mfn_shape=OpenMaya.MFn.kCluster)
                    
                for cindex in range(children.length()):
                    self.unParent(children[cindex])                    
                if not self.target_deformers[index]:
                    name = '%s_%s_joint' % (self.source_deformers[index], tag)
                    joint = self.create(name, clear=True)
                    x, y, z = self.getJointPosition(self.source_deformers[index])                    
                    if source_dag_path.hasFn(OpenMaya.MFn.kTransform):
                        x, y, z = self.getClusterPosition(self.source_deformers[index])                        
                    self.setJointPosition(joint, [x, y, z])
                    self.addInfluence(joint, self.target_geometrys)            
                    _targt_deformers = joint                    
                    
                attribute = '{}.translateX'.format(self.source_deformers[index])
                weights = self.getWeightsFromEnvelope(self.source_geometry, self.source_geometry, attribute)
                
                for each_geometry in self.target_geometrys:                    
                    self.setSkinclusterWeights(joint, each_geometry, weights)
                    # plug = self.getPlug(joint, 'liw')
                    # plug.setBool(False)                    
                
                for rindex in range(children.length()):
                    self.parentTo(children[rindex], source_dag_path)
            else:
                OpenMaya.MGlobal.displayWarning('Your select is wrong!...')
    