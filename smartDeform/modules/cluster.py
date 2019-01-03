import copy
from pprint import pprint
from maya import OpenMaya
from maya import OpenMayaAnim


import studioMaya

from smartDeform.modules import studioMaya
reload(studioMaya)


class Cluster(studioMaya.Maya):

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

    def create(self, name):
        from maya import cmds
        # cmds.select(cl=True)
        name = name.split('|')[-1]
        OpenMaya.MGlobal.clearSelectionList()
        cluster, clusterHandle = cmds.cluster(n=name)
        # cluster, clusterHandle = OpenMaya.MGlobal.executeCommand('cluster -n %s' % name, True, False)
        return cluster, clusterHandle

    def get_weight(self, cluster_handle):
        cluster = self.getDependences(cluster_handle, OpenMaya.MFn.kClusterFilter)
        
        if not cluster:
            raise ValueError('can not find the cluster node!...')
        weights = self.read_weight(cluster[0])
        x, y, z = self.getClusterPosition(cluster_handle)
        data = {}
        data['geometry'] = weights
        data['position'] = [x, y, z]

        return data

    def get_weights(self, cluster_handles):
        cluster_weights = {}
        for each_handle in cluster_handles:
            data = self.get_weight(each_handle)
            cluster_handle = each_handle.fullPathName().encode()
            cluster_weights.setdefault(cluster_handle, data)
        return cluster_weights

    def set_weight(self, mcluster, geometry_data):
        self.write_weight(mcluster, geometry_data)

    def set_weights(self, data):
        for each_handle, each_data in data.items():
            geometry_data = each_data['geometry']
            position = each_data['position']

            cluster, clusterHandle = self.create(each_handle)
            self.setClusterPosition(clusterHandle, position)
            cluster_mobject = self.getMObject(cluster.encode())

            self.set_weight(cluster_mobject, geometry_data)

    def softSelection(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        if not self.target_deformers:
            # cluster, clustserHandle = self.create()
            # self.target_defomrer = clusterHandle
            pass

        dag_paths, indexs, weights = self.getWeightsFromSelection()
        if not dag_paths:
            return

        for each_cluster in self.target_deformers:
            tc_mobject = self.getDependences(
                each_cluster, OpenMaya.MFn.kClusterFilter)
            tm_dag_paths = OpenMaya.MDagPathArray()

            for each_target in self.target_geometrys:
                tm_dag_path = self.getDagPath(each_target)
                tm_dag_paths.append(tm_dag_path)

            self.setWeightsToSelection(
                tc_mobject[0], tm_dag_paths, indexs, weights)

    def blendShape(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):
            cluster_mobject = self.getDependences(
                self.target_deformers[index], OpenMaya.MFn.kClusterFilter)
            weights = self.getWeightsFromEnvelope(
                source_mobject, source_mobject, self.source_deformers[index])
            self.setClusterWeights(
                self.target_geometrys[0], cluster_mobject[0], weights)

    def wire(self):
        print '\n', self.source_geometry
        print self.target_geometrys
        print self.source_deformers
        print self.target_deformers, '\n\n'

        source_mobject = self.getMObject(self.source_geometry)
        for index in range(len(self.source_deformers)):
            attribute = '{}.translateX'.format(self.source_deformers[index])
            cluster_mobject = self.getDependences(
                self.target_deformers[index], OpenMaya.MFn.kClusterFilter)
            weights = self.getWeightsFromEnvelope(
                source_mobject, source_mobject, attribute)
            self.setClusterWeights(
                self.target_geometrys[0], cluster_mobject[0], weights)

    def lattice(self):
        self.wire()

    def skinCluster(self):
        self.wire()

    def read_weight(self, mcluster):
        mfn_weight_filter = OpenMayaAnim.MFnWeightGeometryFilter(mcluster)
        dag_paths = self.getDagPathMembers(mcluster)

        weights = {}
        for index in range(dag_paths.length()):
            mit_geometry = OpenMaya.MItGeometry(dag_paths[index])
            membership_list = []
            weight_list = []
            while not mit_geometry.isDone():
                component = mit_geometry.currentItem()
                float_array = OpenMaya.MFloatArray()

                membership = self.hasMembership(
                    mcluster, dag_paths[index], component)

                if membership:
                    mfn_weight_filter.getWeights(
                        dag_paths[index], component, float_array)
                else:
                    float_array = [0, 0, 0]

                membership_list.append(membership)
                weight_list.append(float_array[0])
                mit_geometry.next()

            weight = {}
            weight['weights'] = weight_list
            weight['memberships'] = membership_list

            geometry = dag_paths[index].fullPathName().encode()
            weights.setdefault(geometry, weight)
            
        return weights

    def write_weight(self, cluster_mobject, geometry_data):
        for each_geometry, each_data, in geometry_data.items():
            # redu
            try:
                dag_path = self.getDagPath(each_geometry)
            except:
                OpenMaya.MGlobal.displayWarning(
                    '\nCan not find object called \"%s\"' % each_geometry)
                continue

            dag_path = self.getDagPath(each_geometry)

            weights = each_data['weights']
            memberships = each_data['memberships']
            mfloat_array = OpenMaya.MFloatArray()
            mscript_util = OpenMaya.MScriptUtil()
            mscript_util.createFloatArrayFromList(weights, mfloat_array)

            self.setClusterWeights(dag_path, cluster_mobject, mfloat_array)
            self.setMembership(dag_path, cluster_mobject, memberships)

    def combine_weights(self, cluster_dag_paths):
        weights_data = {}
        memberships_data = {}  
        for each_handle in cluster_dag_paths:      
            weight_data = self.get_weight(each_handle)
            
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
        
        position = self.getCenterPosition(cluster_dag_paths, 'cluster')        
        cluster, clusterHandle = self.create('combine_cluster')
        self.setClusterPosition(clusterHandle, position)        
        m_cluster = self.getMObject(cluster)       
        self.set_weight(m_cluster, combine_data)
    
    #===========================================================================
    # def copy_weights(self, source_handle, target_handle):        
    #     weight_data = self.get_weight(source_handle)        
    #     for index in range (target_handle.length()):
    #         m_cluster = self.getDependences(target_handle[index], OpenMaya.MFn.kClusterFilter)            
    #         self.set_weight(m_cluster[0], weight_data['geometry'])
    #===========================================================================


    def copy_weight(self, source_handle, target_handle):        
        weight_data = self.get_weight(source_handle)
        m_cluster = self.getDependences(target_handle, OpenMaya.MFn.kClusterFilter) 
        self.set_weight(m_cluster[0], weight_data['geometry'])    
     
    def copy_weights(self, source_handle, target_handles):        
        weight_data = self.get_weight(source_handle)        
        for index in range (target_handles.length()):
            self.copy_weight(source_handle, target_handles[index])
   
    def create_mirror_flip(self, cluster_dag_paths, axis, tag):
        for index in range (cluster_dag_paths.length()):            
            position = self.getClusterPosition(cluster_dag_paths[index])            
            weight_data = self.get_weight(cluster_dag_paths[index])

            mirror_position = position[0]*axis[0], position[1]*axis[1],  position[2]*axis[2]
            symmetry_weights = self.get_flip_weights(weight_data, axis)
               
            cluster, clusterHandle = self.create('%s_cluster' % tag)            
            target_position = mirror_position
            
            if tag == 'mirror':
                proxy_position = [1, 1, 1]
                proxy_position[axis.index(-1)] = 0             
                target_position = [mirror_position[0]*proxy_position[0], mirror_position[1]*proxy_position[1],
                                   mirror_position[2]*proxy_position[2]] 
                
            self.setClusterPosition(clusterHandle, target_position)
            mirror_m_cluster = self.getMObject(cluster)
            
            target_weights = symmetry_weights
            if tag == 'mirror':
                target_weights = self.merge_weights(weight_data['geometry'], symmetry_weights)
                
            self.set_weight(mirror_m_cluster, target_weights)            
                

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
