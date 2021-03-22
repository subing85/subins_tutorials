CATEGORIES = ['character', 'prop', 'set', 'camera']
RENDER_MODES = ['previewRender', 'liveRender', 'diskRender', 'batchRender']
COLOR_SPACE = ['linear', 'sRGB']
FILE_EXTENSION = ['exr', 'png', 'tif', 'jpg']


def get_attributes():
    attributes = [
        'reload',
        'asset_node',
        'load',
        'show_path',
        'sequence',
        'shot',
        'global_frame_range',
        'assets',
        'version',
        'latest_version',
        'next_version',
        'render_mode',
        'current_frame',
        'color_space',
        'file_extension',
        'render_camera',
        'render_location',
        'render',
        'publish',
        ]
    return attributes


def get_hints():
    reload_commands = [
        'from resources.SuperTools.lighting_render_node.v1 import ScriptActions',
        # 'reload(ScriptActions)',
        'ScriptActions.reload_lighting(parameter.getNode())'        
        ] 
    load_commands = [
        'from resources.SuperTools.lighting_render_node.v1 import ScriptActions',
        # 'reload(ScriptActions)',
        'ScriptActions.load_lighting(parameter.getNode())'        
        ]     
    version_commands = [
        'from resources.SuperTools.lighting_render_node.v1 import ScriptActions',
        # 'reload(ScriptActions)',
        'ScriptActions.version_lighting(parameter.getNode())'        
        ]    
    render_commands = [
        'from resources.SuperTools.lighting_render_node.v1 import ScriptActions',
        # 'reload(ScriptActions)',
        'ScriptActions.render_lighting(parameter.getNode())'        
        ] 
    publish_commands = [
        'from resources.SuperTools.lighting_render_node.v1 import ScriptActions',
        # 'reload(ScriptActions)',
        'ScriptActions.publish_lighting(parameter.getNode())'        
        ]          
    hints = {
        'reload': {
            'widget': 'scriptButton',
            'buttonText': 'reload',
            'scriptText': '\n'.join(reload_commands),
            'help':
                """
                search the lighting asset node from the current scene.
                """
            },
        'asset_node':{
            'widget': 'popup',
            'options': 'None',
            'help':
                """
                specify the studio lighting asset node from the current scene.(output of reload)
                """
            },
        'load':{
            'widget': 'scriptButton',
            'buttonText': 'load',
            'scriptText': '\n'.join(load_commands),
            'help':
                """
                collect the current scene date and update all the inputs.
                """
            },
        'show_path': {
            'widget': 'fileInput',
            'readOnly': True,
            },
        'sequence': {
            'widget': '',
            'readOnly': True,
            'help':
                """
                specify the current sequence name.
                """
            },
        'shot':{
            'widget': '',
            'readOnly': True,
            'help':
                """
                specify the current shot name.
                """
            },
        'global_frame_range': {
            'type': 'NumberArray',
            'widget': '',
            'help':
                """
                specify the shot frame range.
                """
            },
        'assets':{
            'type': 'Group',
            'widget': '',
            'help':
                """
                current shot asset list.
                """
            },
        'version': {
            'widget': 'scriptButton',
            'buttonText': 'version',
            'scriptText': '\n'.join(version_commands),
            'help':
                """semantic version
                specify the lighting semantic version, each click change semantic versions (0,1,2,3) for example  MAJOR0, MINOR, PATCH.
                """
            },
        'latest_version':{
            'widget': '',
            'readOnly': True,
            'help':
                """
                auto generate the lighting latest version based on semantic version\nuser permission disabled.
                """                
            },
        'next_version': {
            'widget': '',
            'readOnly': True,
            'help':
                """
                auto generate the lighting next publish version based on semantic and latest version\nuser permission disabled.
                """                
            },
        'render_mode': {
            'widget': 'popup',
            'options': RENDER_MODES,
            'help':
                """
                specify the render type.
                """
            },
        'current_frame': {
            'widget': 'checkBox'            
            },
        'color_space': {
            'widget': 'popup',
            'options': COLOR_SPACE,
            'help':
                """
                specify the render color space.
                """
            },
        'file_extension': {
            'widget': 'popup',
            'options': FILE_EXTENSION,
            'help':
                """
                specify the render file extension.
                """
            },
        'render_camera': {
            'widget': 'scenegraphLocation',
            'help':
                """
                specify the render file location.
                """
            },
        'render_location': {
            'widget': 'fileInput',
            'help':
                """
                specify the render file location.
                """
            },
        'render': {
            'widget': 'scriptButton',
            'buttonText': 'render',
            'scriptText': '\n'.join(render_commands),
            'help':
                """
                to render based on above render_mode.
                """,
            },
        'publish': {
            'widget': 'scriptButton',
            'buttonText': 'publish',
            'scriptText': '\n'.join(publish_commands),
            'help':
                """
                to publish your lighting file.
                """,
            }     
        
        }
    return hints
    
