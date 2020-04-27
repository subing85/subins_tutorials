
from studio_usd_pipe.core import common 

from studio_usd_pipe.api import studioShow 
reload(studioShow)   


def get_shows():
    show = studioShow.Show()    
    data = show.get_shows(verbose=False)
    if not data:
        print '#warnings: not found any shows'
        return None
    return data.values()
    
 
def show_applications(current_show):
    show = studioShow.Show()    
    data = show.get_show_preset_data(current_show)
    if not data:
        return None
    applications = common.sort_dictionary(data['applications'])
    versions = []     
    for application in applications:
        name = [application, data['applications'][application]['version']]  
        versions.append(name)
    return versions


def launch_application(current_show, current_application):
    show = studioShow.Show()
    application = show.get_current_application(current_show, current_application)
    if not application:
        print '#warnings: not found any application under %s show'%current_show
        return
    print 'application', application
    show.launch(current_show, application, contents=None, bin=True, thread=False)
    print 'application', application
    
    
    
    
    
    