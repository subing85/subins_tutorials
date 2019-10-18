import os
import getpass

from datetime import datetime

CURRENT_PATH = os.path.dirname(__file__)


def getInputPath():
    return os.path.join(CURRENT_PATH, 'inputs')


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getRowData(type, tag, valid, description, data):
    row_data = {
        'created_date': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
        'last_modified': datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p'),
        'author': 'Subin Gopi',
        'copyright': '(c) 2019, Subin Gopi All rights reserved.',
        'warning': 'WARNING! All changes made in this file will be lost!',
        'description': 'This data contain information about studio pipe {}'.format(description),
        'type': type,
        'tag': tag,
        'valid': valid,
        'user': getpass.getuser(),
        'data': data
    }
    return row_data
