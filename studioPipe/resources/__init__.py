'''
resource 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import platform

from studioPipe.utils import platforms

CURRENT_PATH = os.path.dirname(__file__)
MODULE = platforms.get_tool_kit()[0]


def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs')


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getImageFormats():
    formats = '(*.jpg *.tga *.png)'
    return formats 


def getPreferencePath():
    return os.path.join(getWorkspacePath(), 'preference')


def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.abspath (
            os.getenv('USERPROFILE') + '/Documents/%s' % MODULE).replace ('\\', '/')
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents', MODULE)
    

def getDefaultPreferences():
    current_data = {
        'pipe_maya_directory': '/usr/autodesk/maya2016',
        'pipe_maya_version': '2016',
        'pipe_name': 'studio_pipe',
        'pipe_nuke_directory': '/usr/autodesk/nuke',
        'pipe_nuke_version': '2.7',
        'pipe_python_directory': '/usr/bin/python',
        # 'pipe_shows_directory': os.path.join(getWorkspacePath()),
        'pipe_shows_directory': '/venture/shows',
        'pipe_site_packages_directory': '/usr/lib64/python2.7/site-packages',
        'pipe_studio_pipe_directory': '/venture/subins_tutorials/studioPipe'
    }
    return current_data


def getToolKitLink():
    return 'https://www.subins-toolkits.com'


def getToolKitHelpLink():
    return 'https://vimeo.com/314966208'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/shader-library'

# end ####################################################################
