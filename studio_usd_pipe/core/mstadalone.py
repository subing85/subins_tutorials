def publish_wrapper(**kwargs):
    pass
    
    
    #===========================================================================
    # /usr/autodesk/maya2018/bin/mayapy -c "from studio_usd_pipe.api import studioPublish;from studio_usd_pipe.api import studioPublish; pub = studioPublish.Publish(pipe='assets', subfield='model'); pub.real_pack()"
    # 
    # 
    # commands = [
    #     '\"from maya import standalone\"',
    #     '\"standalone.initialize(name="python")\"',
    #     '\"from studio_usd_pipe.api import studioPublish\"',
    #     '\"pub = studioPublish.Publish(pipe=\'assets\')\"'
    #     
    #     '\"print \"hello\"\"'
    #     ]
    # 
    # 
    # mayapy = '/usr/autodesk/maya2018/bin/mayapy -c'
    # 
    # print commands[0] + ' ' + commands[1] + ' ' + commands[2] + ' ' + commands[2] + ' ' + commands[-1]
    # 
    # os.system('{} {}'.format(
    #     
    #     mayapy,
    #     commands[0] + '; ' + commands[1] + ';' + commands[2] + '; ' + commands[2] + '; ' + commands[-1]
    #     
    #     )
    # 
    # 
    #===========================================================================
    )

    
    '''
    from maya import standalone
    standalone.initialize(name="python")
    from pymel import core
    data = asset_data
    for each_asset in  data:
    asset_name = data[each_asset]['name']
    asset_path = data[each_asset]['path']
    asset_format = data[each_asset]['format']
    core_type
    print "\n", "asset name", "\t=" , asset_name
    print "create_type", "\t=", asset_path
    try:
    core.saveAs('output_file', typ='maya_type')
    except Exception as error:
    "save error", error
    standalone.uninitialize(name='python')
    
    '''
    

def publish(pipe, **kwargs):
    pass
    
