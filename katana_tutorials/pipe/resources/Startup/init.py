from Katana import Callbacks


def studio_pipe_menu(**kwargs):
    from resources import menu
    pipe_menu = menu.Menu('studio_toolkits')
    pipe_menu.show_pipe_menu()
    
    
callback_type = Callbacks.Type.onStartupComplete
Callbacks.addCallback(callback_type, studio_pipe_menu, callbackObjectHash=None)        
