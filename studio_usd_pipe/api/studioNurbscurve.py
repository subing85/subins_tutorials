from maya import OpenMaya

from studio_usd_pipe import resource

from studio_usd_pipe.api import studioMaya
reload(resource)


class Nurbscurve(studioMaya.Maya):
    
    def __init__(self):
        # studioMaya.Maya.__init__(self)  
        super(Nurbscurve, self).__init__()
       
    def get_kcurve(self, mobject):
        mfn_curve = OpenMaya.MFnNurbsCurve(mobject)                
        cvs_array = OpenMaya.MPointArray()        
        mfn_curve.getCVs(cvs_array, OpenMaya.MSpace.kObject)
        knots_array = OpenMaya.MDoubleArray()
        mfn_curve.getKnots(knots_array)        
        knots_array = [int(knots_array[x]) for x in range(knots_array.length())]
        
        bounding_box = mfn_curve.boundingBox()
        min_mpoint = bounding_box.min()
        max_mpoint = bounding_box.max()
        bounding_value = {
            'min': [min_mpoint.x, min_mpoint.y, min_mpoint.z],
            'max': [max_mpoint.x, max_mpoint.y, max_mpoint.z]
            }
                
        vertices = []
        for x in range(cvs_array.length()):
            array = [
                cvs_array[x].x,
                cvs_array[x].y,
                cvs_array[x].z,
                cvs_array[x].w
            ]            
            vertices.append(array)

        transform_data = self.get_ktransform(mobject, world=True)
            
        data = {
            'points': vertices,
            'knots': list(knots_array),
            'degree': mfn_curve.degree(),
            'form': mfn_curve.form(),
            'name': mfn_curve.name(),
            'num_cvs': mfn_curve.numCVs(),
            'bounding': bounding_value,
            'translate': transform_data['translate'],
            'rotate': transform_data['rotate'],
            'scale': transform_data['scale']            
            }        
        return data    

    def create_world(self, mfn_dag_node, parent=False):
        parent_node = OpenMaya.MFnDependencyNode(mfn_dag_node.object())
        mplug_x = parent_node.findPlug('boundingBoxMaxX')
        mplug_z = parent_node.findPlug('boundingBoxMaxZ')        
        radius = max([mplug_x.asFloat(), mplug_z.asFloat()])
        world_data = resource.getWroldData()
        world_node = self.create_kcurve('world', world_data, radius=radius + 0.5) 
        if parent:
            children = OpenMaya.MObjectArray()
            for x in range (mfn_dag_node.childCount()): 
                children.append(mfn_dag_node.child(x))                
            for x in range(children.length()):                
                self.set_parent(children[x], world_node.object())   
            self.set_parent(world_node.object(), mfn_dag_node.object())
        return world_node
    
    def validate_curve(self, mfn_curve, knots, num_cvs):
        knots = OpenMaya.MDoubleArray()
        mfn_curve.getKnots(knots)        
        m_knots = [int(knots[x]) for x in range(knots.length())]        
        m_num_cvs = mfn_curve.numCVs()
        if knots != m_knots:
            return False
        if num_cvs != m_num_cvs:
            return False
        return True
        
    def create_curve(self, name, data, replace=False):
        if replace:
            mfn_curve = self.update_kcurve(name, data)
            if not mfn_curve:
                if self.object_exists(name):
                    children = self.get_children(name)
                    for x in range(children.length()):
                        self.unparent(children[x])
                    self.remove_node(name)                
                mfn_curve = self.create_kcurve(name, data)       
        else:
            mfn_curve = self.create_kcurve(name, data)
        return mfn_curve                
                
    def create_kcurve(self, name, data, radius=1):
        cv_array = self.create_mpoint_array(data['points'])
        knots_array = self.create_mdouble_array(data['knots'])
        mfn_curve = OpenMaya.MFnNurbsCurve()
        
        mfn_curve.create(
            cv_array,
            knots_array,
            data['degree'],
            data['form'],
            False,
            True,
            )
        mfn_curve.updateCurve() 
        mfn_dag_node = OpenMaya.MFnDagNode(mfn_curve.parent(0))
        if '|' in name:
            name = name.split('|')[-1]
        mfn_dag_node.setName(name)        
        mplug_x = mfn_dag_node.findPlug('scaleX')
        mplug_y = mfn_dag_node.findPlug('scaleY')  
        mplug_z = mfn_dag_node.findPlug('scaleZ')  
        mplug_x.setFloat(radius)
        mplug_y.setFloat(radius)
        mplug_z.setFloat(radius)
        self.freeze_transformations(mfn_dag_node)
        
        import json
        
        # print json.dumps(data, indent=4)
        
        self.set_ktransform(mfn_dag_node.object(), data)  # set position
        return mfn_curve

    def update_kcurve(self, name, data):
        cv_array = self.create_mpoint_array(data['points'])
        if not self.object_exists(name):
            return None
        dag_path = self.get_dagpath(name)         
        shape_dag_path = self.get_shape_node(dag_path)
        mfn_curve = OpenMaya.MFnNurbsCurve(shape_dag_path)
        if not self.validate_curve(mfn_curve, data['knots'], data['num_cvs']):
            return None
        mfn_curve.setCVs(cv_array, OpenMaya.MSpace.kObject)
        return mfn_curve

    def get_curve_data(self, mobject):
        transform_curve = self.extract_transform_primitive(
            OpenMaya.MFn.kCurve, shape=False, parent_mobject=mobject)               
        data = {}            
        for x in range(transform_curve.length()):
            curve_data = self.get_kcurve(transform_curve[x])
            curve_data['order'] = x
            data.setdefault(transform_curve[x].fullPathName(), curve_data)              
        return data          
    
