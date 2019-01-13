import platform
from smartDeformer.utils import config
reload(config)


def has_valid():
    tool_os, tool_app, tool_ver, tool_py = config.get_conig()    
    operating_system, application, version, python = get_platform()    
    result = {True, 'Support to your maya version'}    
    if tool_os!=operating_system:
        result = {False: 'Only support \"%s\" operating system' % tool_os}
        return result    
    if tool_app not in application:
        result = {False: 'Only support \"%s %s\" operating system' % (tool_app, tool_ver)}
        return result            
    if tool_ver not in version:
        result = {False: 'Only support \"%s %s\" operating system' % (tool_app, tool_ver)}
        return result    
    return result    


def get_platform():    
    from pymel import core    
    operating_system = platform.system()
    application = core.about(q=True, a=True)
    version = core.about(q=True, v=True)
    python = platform.python_version()    
    return operating_system, application, version, python   



