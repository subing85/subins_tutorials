import os
import json
import shutil
import resources

from core import versions


def asset_publish(name, category, type, version, model, lookdev):
    '''
    :example
        name = 'jasmin'
        category = 'character'
        type = 'model'
        version = '1.0.0'
        model = 'None'
        lookdev = 'None'
        from tools.maya_publish import publish
        asset_publish(name, category, type, version, model, lookdev)
    '''
    from pymel import core
    print '#info asset publish(%s)' % type
    py_node = core.PyNode(name) 
    attributes = {
        'name': name,
        'category': category,
        'type': type,
        'model': model,
        'version': version,
        'lookdev': lookdev
        }
    orders = ['name', 'category', 'type', 'version', 'model', 'lookdev']
    for order in orders:
        current_attribute = '%s.%s' % (py_node.name(), order)
        if core.objExists(current_attribute):
            core.deleteAttr(current_attribute)              
        py_node.addAttr(order, dt='string')
        py_node.setAttr(order, attributes[order])
    dirname = os.path.join(
        resources.get_show_path(),
        # '/venture/shows/katana_tutorials/asset',
        category,
        name,
        type,
        version
        )    
    if os.path.isdir(dirname):
        try:
            shutil.rmtree(dirname)
        except Exception:
            pass   
    if not os.path.isdir(dirname):
        os.makedirs(dirname)        
    maya_path = os.path.join(dirname, '%s.ma' % name) 
    abc_path = os.path.join(dirname, '%s.abc' % name)
    manifest_path = os.path.join(dirname, 'manifest.json')
    py_node.select(r=True)
    core.exportSelected(maya_path, f=True)     
    asset_attributes = '-attr ' + ' -attr '.join(orders)   
    command = '-frameRange 1001 1002 %s -uvWrite -attrPrefix xgen -worldSpace -root %s -stripNamespaces -file %s ' % (
        asset_attributes, name, abc_path)
    py_node.select(r=True)        
    core.AbcExport(j=command)
    manifest_data = {
         'pipe': 'asset',
         'data': attributes
         }
    with open(manifest_path, 'w') as manifest:
        manifest.write(json.dumps(manifest_data, indent=4))        
    os.system('xdg-open \"%s\"' % dirname)        
    print '\t', maya_path
    print '\t', abc_path
    print '\t', manifest_path


def scene_publish(sequence, shot, scene, version, puppets=None):
    '''
    :example
        sequence = 'sequence_101'
        shot = 'shot_1001'        
        scene = 'animation'
        version = '0.0.0'
        assets = ['batman:batman', 'jasmin:jasmin', 'scene:scene']
        # assets = ['batman:batman', 'jasmin:jasmin', 'scene:scene', 'motorcycle:motorcycle']    
        from tools.maya_publish import publish
        scene_publish(sequence, shot, scene, version)
    '''
    from pymel import core
    print '#info scene publish(%s)' % scene
    model_panels = core.getPanel(type='modelPanel')
    for model_panel in model_panels:
        core.modelEditor(model_panel, edit=True, displayAppearance='boundingBox')
        core.modelEditor(model_panel, edit=True, allObjects=False)
        core.modelEditor(model_panel, edit=True, nurbsCurves=True)
        core.modelEditor(model_panel, edit=True, polymeshes=True)
    if not puppets:
        puppets = get_valid_puppets()
    dirname = os.path.join(
        resources.get_show_path(),
        # '/venture/shows/katana_tutorials/scene',
        sequence,
        shot,
        scene,
        version  
        )    
    if os.path.isdir(dirname):
        try:
            shutil.rmtree(dirname)
        except Exception:
            pass
    if not os.path.isdir(dirname):
        os.makedirs(dirname) 
    min = int(core.playbackOptions(q=True, min=True))
    max = int(core.playbackOptions(q=True, max=True))
    puppet_attributes = ['name', 'category', 'type', 'version', 'model', 'lookdev']
    amination_attributes = ['min', 'max', 'latest_lookdev']
    puppet_contents = {}
    for puppet in puppets:
        py_node = core.PyNode(puppet) 
        for each in amination_attributes:        
            attribute = '%s.%s' % (py_node.name(), each)
            if core.objExists(attribute):
                core.deleteAttr(attribute)              
            py_node.addAttr(each, dt='string') 
        py_node.setAttr('min', str(min))        
        py_node.setAttr('max', str(max))
        puppet_name = puppet.split(':')[0]
        for puppet_attribute in puppet_attributes:
            value = py_node.getAttr(puppet_attribute)
            name = puppet.split(':')[0]
            if puppet_name not in puppet_contents:
                puppet_contents.setdefault(puppet_name, {})
            puppet_contents[puppet_name].setdefault(puppet_attribute, value)
        category = py_node.getAttr('category') 
        name = py_node.getAttr('name') 
        model = py_node.getAttr('model') 
        model_depnendency = get_lookdev_model_depnendency(category, name)
        latest_lookdev = 'None'
        if model_depnendency:
            if model_depnendency[model]:
                latest_lookdev = model_depnendency[model][0]
        py_node.setAttr('latest_lookdev', latest_lookdev) 
        abc_path = os.path.join(dirname, '%s.abc' % puppet_name)
        ud_attrubutes = []
        for attrubute in py_node.listAttr(ud=True):
            ud_attrubutes.append(attrubute.attrName())
        asset_attributes = '-attr ' + ' -attr '.join(ud_attrubutes)
        command = '-frameRange %s %s %s -uvWrite -attrPrefix xgen -worldSpace -root %s -stripNamespaces -file %s ' % (
            min, max, asset_attributes, puppet, abc_path)
        py_node.select(r=True)        
        core.AbcExport(j=command)        
        print '\t', abc_path
    core.select(puppets, r=True)
    maya_path = os.path.join(dirname, '%s.ma' % shot)
    manifest_path = os.path.join(dirname, 'manifest.json')    
    core.exportSelected(maya_path, preserveReferences=True, f=True)
    manifest_data = {
         'pipe': 'scene',
         'data': {
             'frame_range': [min, max],
             'sequence': sequence,
             'scene': scene,
             'puppets': puppet_contents,
             'version': version
             }
         }
    with open(manifest_path, 'w') as manifest:
        manifest.write(json.dumps(manifest_data, indent=4))  
    os.system('xdg-open \"%s\"' % dirname)        
    print '\t', manifest_path
    print '\t', maya_path


def get_valid_puppets():
    from pymel import core
    mnodes = core.ls(assemblies=True)    
    valid_puppets = []
    for mnode in mnodes:
        attributes = [
            'name', 'category', 'type', 'version', 'model', 'lookdev']
        index = []
        for attribute in attributes:
            current_attribute = '%s.%s' % (mnode.name(), attribute)
            if not core.objExists(current_attribute):
                continue
            index.append(attribute)
        if len(index) != 6:
            continue
        if mnode.getAttr('type') != 'puppet':
            continue    
        valid_puppets.append(mnode)
    return valid_puppets


def get_lookdev_model_depnendency(category, name):
    '''
    :example
        get_lookdev_model_depnendency('character', 'batman')    
    '''    
    model_depnendency = versions.get_asset_dependency_versions(
        resources.get_show_path(), category, name, 'lookdev', 'model')
    return model_depnendency
    #===========================================================================
    # lookdev_versions = versions.get_versions(lookdev_path, 'lookdev')
    # model_depnendency = {}
    # for lookdev_version in lookdev_versions:
    #     manifest = os.path.join(
    #         lookdev_path, 'lookdev', lookdev_version, 'manifest.json')
    #     if not os.path.isfile(manifest):
    #         model_depnendency.setdefault(lookdev_version, None)
    #         continue       
    #     with(open(manifest, 'r')) as file:
    #         data = json.load(file)
    #         model = data['data']['model']
    #         model_depnendency.setdefault(model, []).append(lookdev_version)
    # print '#info: lookdev_model_depnendency'
    # print 'model', '[lookdev]'
    # print json.dumps(model_depnendency, indent=4)
    # return model_depnendency
    #===========================================================================


def get_current_version(name):
    from pymel import core
    py_node = core.PyNode(name)
    if not core.objExists('%s.version' % name):
        return None        
    model = py_node.getAttr('version')
    return model

