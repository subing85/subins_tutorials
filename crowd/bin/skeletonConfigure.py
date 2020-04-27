def show_window(standalone=None):
    pass


from crowd.resource.ui import configure_ui
reload(configure_ui)
window = configure_ui.Connect()
window.show()
