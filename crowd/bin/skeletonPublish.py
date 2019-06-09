
    
def publish():
    from crowd.resource.ui import publish_ui
    reload(publish_ui)
    window = publish_ui.Connect('skeleton')
    return window

window = publish()
window.show()