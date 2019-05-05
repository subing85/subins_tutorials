import warnings

from crowd.core import readWrite

reload(readWrite)

import json



def create(input=None):    
    if not input:
        rw = readWrite.ReadWrite()       
        input = rw.collect('skeletons', 'puppet')
        
    if 'biped' not in input:
        warnings.warn('input data not valid (biped)', Warning)
        return None    
    create_fk(input['biped']['fk'])


def create_fk(input):    
    sorted_data = readWrite.ReadWrite.sorted_data(input)
    
    for each_joint in sorted_data:
        current_joint = input[each_joint]
        print current_joint
    
    

