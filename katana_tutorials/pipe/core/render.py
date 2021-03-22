
from core import scene

from Katana import NodegraphAPI
from Katana import RenderManager


def start_render(render_node, render_mode, frame_ranges):    
    if render_mode == 'batchRender':
        batch_render(render_node, frame_ranges, scene.get_current_scene())
    else:
        normal_render(render_node, render_mode, frame_ranges)

        
def normal_render(render_node, render_mode, frame_ranges):
    if isinstance(render_node, str) or isinstance(render_node, unicode):
        render_node = NodegraphAPI.GetNode(render_node)
    if not render_node:
        print '#warnings: not a valid render node'
        return
    for index in range (frame_ranges[0], frame_ranges[1]):
        # RenderManager.RenderModes.DISK_RENDER
        settings = RenderManager.RenderingSettings()
        settings.frame = index
        settings.mode = render_mode
        settings.asynchRenderMessageCB = messageHandler
        settings.asynch = False
        RenderManager.StartRender(
            render_mode,
            node=render_node,
            settings=settings
            )    


def batch_render(render_node, frame_ranges, katana_scene):
    print '#warnings: under construction'


def messageHandler(sequenceID, message):
    print message

