import logging

from maya import OpenMaya

from studio_usd_pipe.core import preference


def set():
    pref = preference.Preference()       
    bundle_data = pref.get() 
    
    # print bundle_data['show_directory']
    set_workspace(bundle_data['show_directory'])   



def set_workspace(path):
    OpenMaya.MGlobal.executeCommand('setProject \"%s\"'%(path), False, True)           
    OpenMaya.MGlobal.executeCommand('workspace -act \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -bw \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -o \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -pp \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -bw \"default\"', False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -s \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -fr "scene" \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -fr "sourceImages" \"%s\"'%(path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -updateAll', False, True)
    print logging.info('set the show path to \"%s\"'%path)
    
def set_units():
    pass
    
    currentUnit -linear "centimeter" ;
    currentUnit -time "pal" ;
    currentUnit -angle "degree" ;
    string $abc = `currentUnit -q -time` ;
