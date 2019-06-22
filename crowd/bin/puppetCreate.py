def show_window(standalone=None):
    from crowd.resource.ui import create_ui
    reload(create_ui)
    window = create_ui.Connect('puppet')
    window.show()
