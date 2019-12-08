import os
import ast
import json

from studio_usd_pipe import resources

def get_plugins():
    pulgins = None
    plugin_path = os.path.join(resources.getInputPath(), 'plugins.json')
    with (open(plugin_path, 'r')) as open_data:
        bundle_data = json.load(open_data)
        if 'plugins' not in bundle_data['data']:
            return
        pulgins = bundle_data['data']['plugins']    
    if not pulgins:
        return    
    return pulgins


def set_plugins():
    from maya import cmds    
    pulgins = get_plugins()
    print '\n\nPlugins are loading!...\n'
    for plugin in pulgins:
        try:        
            cmds.loadPlugin(plugin, quiet=True)
            print '{} loaded plugin'.format(plugin)
        except ImportError as error:
            print error
    print '\nPlgins loaded!...\n\n'
            
            
def sys_argv_to_dict(arguments):
    replaces_to = [
        '[', ']', '{', '}', ','] 
    dict_data = {}
    for argument in arguments:
        for replace_to in replaces_to:
            argument = argument.replace(replace_to, '')
        dict_data.setdefault('args', []).append(argument)
    return dict_data

#.replace('[', '').replace(']', '').replace('{', ''), .replace('}', '')
























#===============================================================================
# def start(source_file, codes, save, register_time):
#     from maya import standalone
#     standalone.initialize(name='python')
#     from maya import OpenMaya    
#     set_plugins()
#     file_io = OpenMaya.MFileIO()
#     file_io.open(source_file)
#     for each in codes.split('; '):
#         exec(each)
#     print '\nsubshell process donw!...'
#     if save:
#         file_type = file_io.fileType()
#         file_io.saveAs(save, file_type.encode(), True)
#         os.utime(save, (register_time, register_time))
#         print '// Result:', save
#     standalone.uninitialize(name='python')
#===============================================================================



        

       
    