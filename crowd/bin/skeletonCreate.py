def show_window(standalone=None):
    #===========================================================================
    # from crowd.resource.ui import create_ui
    # reload(create_ui)
    # window_a = create_ui.Connect('skeleton')
    # window_a.show()
    #===========================================================================
    pass

from crowd.resource.ui import create_ui
reload(create_ui)
window_a = create_ui.Connect('skeleton')
window_a.show()
