from studio_usd_pipe import resource
from studio_usd_pipe.core import mayaread

inputs = {
    "description": "aaaaaaaa",
    "dependency": "None",
    "source_maya": "/venture/shows/batman/batman_0.0.3.mb",
    "subfield": "model",
    "caption": "batman",
    "tag": "character",
    "user": "shreya",
    "version": "9.0.0",
    "type": "interactive",
    "thumbnail": "/venture/shows/batman/my_super_hero.png",
    "pipe": "assets"
}
 
maya = '/venture/shows/batman/batman.ma'
script = resource.getScriptPath() + '/maya_release.py'
data = mayaread.read(maya, script, **inputs)

import json

print json.dumps(data, indent=4)
