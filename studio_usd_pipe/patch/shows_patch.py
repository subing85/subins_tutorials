#!/usr/bin/python

from studio_usd_pipe.core import common 
from studio_usd_pipe.api import studioShow 


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
    versions = []
    for application in ['show_applications', 'common_applications']:
        if application not in data:
            continue
        if not data[application]:
            continue
        applications = common.sort_dictionary(data[application])
        for each in applications:
            print each
            name = [each, data[application][each]['version'][1]]  
            versions.append(name)    
    return versions


def launch_application(current_show, current_application):
    show = studioShow.Show()
    application, application_type = show.get_current_application(current_show, current_application)
    if not application:
        print '#warnings: not found %s application under %s show' % (current_application, current_show)
        return
    show.launch(current_show, application_type, application, contents=None, thread=False)
    
