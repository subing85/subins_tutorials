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

CURRENT_PATH = os.path.dirname(__file__)


def get_tool_kit():
    return 'Studio Maya Interpreter ', 'smi', '0.0.1'

def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getPreferencePath():
    return os.path.join(getWorkspacePath(), 'preference')


def getWorkspacePath():
    if platform.system() == 'Windows':
        return os.path.abspath(
            os.getenv('USERPROFILE') + '/Documents').replace('\\', '/')
    if platform.system() == 'Linux':
        return os.path.join(os.getenv('HOME'), 'Documents', 'MODULE')


def getToolKitLink():
    return 'https://www.subins-toolkits.com'


def getToolKitHelpLink():
    return 'https://vimeo.com/322552816'


def getDownloadLink():
    return 'https://www.subins-toolkits.com/asset-library'

# end ####################################################################
