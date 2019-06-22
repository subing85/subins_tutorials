def show_window(standalone=None):
    from crowd.resource.ui import publish_ui
    window = publish_ui.Connect('skeleton')
    window.show()