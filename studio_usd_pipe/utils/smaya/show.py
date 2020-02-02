from maya import OpenMaya
from maya import OpenMayaAnim

from studio_usd_pipe import resource
from studio_usd_pipe.core import preference


def set():
    pref = preference.Preference()       
    bundle_data = pref.get() 
    print '\n', '#' * 50, '\nsubin\'s tool kits show configure.'
    print 'release\n\tname:', pref.config.name
    print '\tversion:', pref.config.version    
    set_workspace(bundle_data['show_directory'])  
    set_plugins()
    set_units()
    set_playbacks()
    set_undo()
    set_render_settings()
    OpenMaya.MGlobal.displayInfo('Successfully loaded <%s>' % pref.config.pretty)


def set_plugins():
    print '\nset the plugins'
    data = resource.getPluginData()
    for plugin in data['plugins']:
        try:
            OpenMaya.MGlobal.executeCommand(
                'loadPlugin -quiet \"%s\"' % (plugin), False, True)
            print '\tloaded plugin: <%s>' % plugin
        except Exception as LoadError:            
            print '\tloaded plugin failed: <%s>' % plugin, LoadError
                  
        
def set_workspace(path):
    print '\nset the workspace (project)'
    OpenMaya.MGlobal.executeCommand('setProject \"%s\"' % (path), False, True)           
    OpenMaya.MGlobal.executeCommand('workspace -act \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -bw \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -o \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -pp \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -bw \"default\"', False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -s \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -fr "scene" \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -fr "sourceImages" \"%s\"' % (path), False, True) 
    OpenMaya.MGlobal.executeCommand('workspace -updateAll', False, True)
    print '\tshow path to <%s>' % path

    
def set_units():
    print '\nset units'
    OpenMaya.MGlobal.setYAxisUp()
    OpenMaya.MGlobal.executeCommand('currentUnit -linear \"centimeter\"', False, True)   
    OpenMaya.MGlobal.executeCommand('currentUnit -angle \"degree\"', False, True)           
    OpenMaya.MGlobal.executeCommand('currentUnit -time \"pal\"', False, True)           
    OpenMaya.MGlobal.executeCommand('currentUnit -time \"24fps\"', False, True)
    print '\tup axis: <y>'
    print '\tcurrent linear unit: <centimeter>'
    print '\tcurrentUnit angle unit: <degree>'
    print '\tcurrentUnit time unit: <pal>, <24fps>'
    
    
def set_playbacks():
    print '\nset playbacks'    
    manim_control = OpenMayaAnim.MAnimControl()
    manim_control.setMinMaxTime(OpenMaya.MTime(1), OpenMaya.MTime(24))
    manim_control.setAnimationStartEndTime(OpenMaya.MTime(1), OpenMaya.MTime(24))
    manim_control.setPlaybackMode(manim_control.kPlaybackLoop)  # loop = continuous
    manim_control.setViewMode(manim_control.kPlaybackViewAll)  #   playback in all views. 
    manim_control.setPlaybackSpeed(1)
    print '\tframe range: <1, 24>'
    print '\tplayback mode: <loop, continuous>'
    print '\tview mode: <playback in all views>'
    print '\tplayback speed: <real-time>'

    
def set_undo():
    print '\nset undo'    
    OpenMaya.MGlobal.executeCommand('undoInfo -state on', False, True)           
    OpenMaya.MGlobal.executeCommand('undoInfo -infinity on', False, True)       
    print '\tundo state <on>'    
    print '\tundo infinity <on>'    
        

def set_render_settings():
    print '\nset render settings'    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.width\" 1920', False, True)         
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.height\" 1080', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.pixelAspect\" 1', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.deviceAspectRatio\" 1.7769999504089355', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.aspectLock\" no', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.lockDeviceAspectRatio\" no', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr \"defaultResolution.dotsPerInch\" 72', False, True)    
    OpenMaya.MGlobal.executeCommand(
        'setAttr defaultRenderGlobals.currentRenderer -type \"string\" \"renderman\"', False, True)
    print '\tresolution: <1920x1080(HD-1080)>'    
    print '\trender engine: <renderman>'    

