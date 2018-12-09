import os
import getpass

CURRENT_PATH = os.path.dirname(__file__)


def getGuiPath():
    return os.path.join(CURRENT_PATH, 'ui', 'main_ui.ui')


def getControlsPath():
    return os.path.join(CURRENT_PATH, 'preset', 'biped_controls.json')


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')