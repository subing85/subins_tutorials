#!/usr/bin/python

NAME = 'Reload'
ORDER = 15
VALID = True
TYPE = 'maya_tool'
KEY = 'reload'
SEPARATOR = True
ICON = 'reload.png'
OWNER = 'Subin Gopi'
COMMENTS = 'Relad modules!...'
VERSION = '0.0.0'
MODIFIED = 'April 29, 2020'



def execute():    
    from studio_usd_pipe import resource
    from studio_usd_pipe.core import common
    from studio_usd_pipe.core import sheader
    from studio_usd_pipe.core import swidgets
    from studio_usd_pipe.utils import maya_asset

    from studio_usd_pipe.api import studioUsd
    from studio_usd_pipe.api import studioMaya
    from studio_usd_pipe.api import studioModel
    from studio_usd_pipe.api import studioShader
    from studio_usd_pipe.api import studioNurbscurve  
    
    from studio_usd_pipe.api import studioShow
    from studio_usd_pipe.api import studioPush
    from studio_usd_pipe.api import studioPipe
    from studio_usd_pipe.api import studioEnviron    
    
    reload(resource)
    reload(common)
    reload(sheader)
    reload(swidgets)
    reload(maya_asset)

    reload(studioUsd)
    reload(studioMaya)
    reload(studioModel)
    reload(studioShader)
    reload(studioNurbscurve)

    reload(studioShow)
    reload(studioPush)
    reload(studioPipe)
    reload(studioEnviron)

