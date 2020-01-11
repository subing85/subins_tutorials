from maya import OpenMaya

from studio_usd_pipe import resource

from studio_usd_pipe.api import studioMaya
reload(resource)

class Nurbscurve(studioMaya.Maya):
    
    def __init__(self):
        studioMaya.Maya.__init__(self)        
        
    def create_world(self, mfn_dag_node, parent=False):
        parent_node = OpenMaya.MFnDependencyNode(mfn_dag_node.object())
        mplug_x = parent_node.findPlug('boundingBoxMaxX')
        mplug_z = parent_node.findPlug('boundingBoxMaxZ')        
        radius = max([mplug_x.asFloat(), mplug_z.asFloat()])
        world_data = resource.getWroldData()
        world_node = self.create_kcurve(world_data, radius=radius + 0.5, name='world') 
        if parent:
            children = OpenMaya.MObjectArray()
            for x in range (mfn_dag_node.childCount()): 
                children.append(mfn_dag_node.child(x))                
            for x in range(children.length()):                
                self.set_parent(children[x], world_node.object())   
            self.set_parent(world_node.object(), mfn_dag_node.object())
        return world_node 
    
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
        data = {
            'points': vertices,
            'knots': list(knots_array),
            'degree': mfn_curve.degree(),
            'form': mfn_curve.form(),
            'name': mfn_curve.name(),
            'num_cvs': mfn_curve.numCVs(),
            'bounding': bounding_value,
            }        
        return data
        
    def create_kcurve(self, data, radius=1, name=None):
        cv_array = self.create_mpoint_array(data['control_vertices'])
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
        mfn_dependency_node = OpenMaya.MFnDependencyNode(mfn_curve.parent(0))
        mfn_dependency_node.setName(name)        
        mplug_x = mfn_dependency_node.findPlug('scaleX')
        mplug_y = mfn_dependency_node.findPlug('scaleY')  
        mplug_z = mfn_dependency_node.findPlug('scaleZ')  
        mplug_x.setFloat(radius)
        mplug_y.setFloat(radius)
        mplug_z.setFloat(radius)
        self.freeze_transformations(mfn_dependency_node.object())
        return mfn_dependency_node

    def get_curve_data(self, mobject):
        transform_curve = self.extract_transform_primitive(
            OpenMaya.MFn.kCurve, root_mobject=mobject)               
        data = {}            
        for x in range(transform_curve.length()):
            curve_data = self.get_kcurve(transform_curve[x])
            curve_data['order'] = x
            data.setdefault(transform_curve[x].fullPathName(), curve_data)              
        return data          
    
