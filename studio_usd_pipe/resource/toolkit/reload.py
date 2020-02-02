NAME = 'Reload'
ORDER = 14
VALID = True
LAST_MODIFIED = 'January 25, 2020'
OWNER = 'Subin Gopi'
COMMENTS = 'Relad modules!...'
SEPARATOR = True

def execute():    
    # from maya import OpenMaya
    # OpenMaya.MGlobal.executeCommand('unloadPlugin \"subins_usd_toolkits\"', False, True)           
    #  OpenMaya.MGlobal.executeCommand('updatePluginDirectories', False, True)           
    # OpenMaya.MGlobal.executeCommand('loadPlugin \"subins_usd_toolkits\"', False, True)           
    
    from studio_usd_pipe.core import menu
    reload(menu)
    from studio_usd_pipe.core import asset
    reload(asset)
    from studio_usd_pipe.core import common
    reload(common)
    from studio_usd_pipe.core import configure
    reload(configure)
    from studio_usd_pipe.core import database
    reload(database)
    from studio_usd_pipe.core import image
    reload(image)

    from studio_usd_pipe.core import manifest
    reload(manifest)
    from studio_usd_pipe.core import mayapack
    reload(mayapack)
    from studio_usd_pipe.core import preference
    reload(preference)
    from studio_usd_pipe.core import publish
    reload(publish)
    from studio_usd_pipe.core import widgets
    reload(widgets)
    
    from studio_usd_pipe.api import studioPreference
    reload(studioPreference)
    from studio_usd_pipe.api import studioShader
    reload(studioShader)
    from studio_usd_pipe.api import studioUsd
    reload(studioUsd)
    
    from studio_usd_pipe.api import assetPublish
    reload(assetPublish)
    from studio_usd_pipe.api import studioMaya
    reload(studioMaya)
    from studio_usd_pipe.api import studioModel
    reload(studioModel)
    from studio_usd_pipe.api import studioNurbscurve
    reload(studioNurbscurve)
    
    from studio_usd_pipe import resource
    reload(resource)
        
    from studio_usd_pipe.utils import smaya
    reload(smaya)
    
    from studio_usd_pipe.gui import preference
    reload(preference)
    
    from studio_usd_pipe.resource.ui import inputs
    reload(inputs) 
       
    from studio_usd_pipe.resource.ui import preference
    reload(preference) 
        
    #===========================================================================
    # import os
    # for a in os.listdir('/venture/subins_tutorials/studio_usd_pipe/resource/ui'):
    #     if '.pyc' in a:
    #         continue
    #     print  'from studio_usd_pipe.resource.ui import', a.split('.')[0]
    #     print 'reload(%s)'% a.split('.')[0]
    #===========================================================================