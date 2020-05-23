composition = {
        "model": {
            "0": {
                "1.0.0": "/venture/shows/batman/assets/batman/model/1.0.0/batman.usd", 
                "0.0.0": "/venture/shows/batman/assets/batman/model/0.0.0/batman.usd"
            }
        }, 
        "uv": {
            "1": {
                "1.0.0": "/venture/shows/batman/assets/batman/uv/1.0.0/batman.usd", 
                "0.0.0": "/venture/shows/batman/assets/batman/uv/0.0.0/batman.usd"
            }
        }, 
        "shader": {
            "2": {
                "1.0.0": "/venture/shows/batman/assets/batman/shader/1.0.0/batman.usd", 
                "0.0.0": "/venture/shows/batman/assets/batman/shader/0.0.0/batman.usd", 
                "2.0.0": "/venture/shows/batman/assets/batman/shader/2.0.0/batman.usd"
            }
        }
    }
from studio_usd_pipe.api import studioPush
reload(studioPush)

current_show = 'btm'
pipe = 'assets'

push = studioPush.Push(current_show, pipe)        
valid, message = push.do_publish(repair=True, trail=False, **composition)
