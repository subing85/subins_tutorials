import json

from pprint import pprint

from crowd.core import generic

reload(generic)

def create_puppet(root, input_data):    
    print root
    print  input_data.keys()

    skeletons = generic.get_root_children()
    print skeletons
    
    scene_skeletons = generic.get_skeletons(root, skeletons)
    # 0 = center joints
    # 1 = left joints
    # 2 = right joints
    
    fk_skeletons = generic.find_fk_skeletons(
        scene_skeletons, input_data['fk'])
    pprint (fk_skeletons)
    
    pprint(input_data['fk'])
    