"""
NAME: disable_nodes
ICON: /venture/shows/katana_tutorials/pipe/resources/icons/disable.png
KEYBOARD_SHORTCUT: 
SCOPE:
description: bypass (disable) the katana node 

"""

# The following symbols are added when run as shelf buttons:
# exit():      Allows 'error-free' early exit from the script.
# dropEvent:   If your script registers DROP_TYPES, this is a QDropEvent
#              upon a valid drop. Otherwise, it is None.
#              Example:  Registering for "nodegraph/nodes" DROP_TYPES
#                        allows the user to get dropped nodes using
#       nodes = [NodegraphAPI.GetNode(x) for x in
#               str(dropEvent.encodedData( 'nodegraph/nodes' )).split(',')]
# console_print(message, raisePanel = False):
#              If the Python Console exists, print the message to it.
#              Otherwise, print the message to the shell. If raisePanel
#              is passed as True, the panel will be raised to the front.

from core import nodegraph
nodegraph.set_knode_disable()