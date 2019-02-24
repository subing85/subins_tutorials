
import sys

path = '/mnt/venture/subins_tutorials'
if path not in sys.path:
    sys.path.append(path)

from assetLibrary.modules import readWrite 
from assetLibrary import resources


def get_input_data():
    category_path = resources.getInputPath(module='categories')
    rw = readWrite.ReadWrite(tag='categories')
    rw.file_path = category_path        
    input_data = rw.get_data()    
    order_data = rw.set_order(input_data)    
    return input_data, order_data

