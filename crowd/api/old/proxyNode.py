from maya import OpenMaya
from maya import OpenMayaMPx
from maya import OpenMayaUI
from maya import OpenMayaRender

node_name = 'crowdProxy'
node_Id = OpenMaya.MTypeId(0x87079)

gl_renderer = OpenMayaRender.MHardwareRenderer.theRenderer()
gl_ft = gl_renderer.glFunctionTable()

class Connect(OpenMayaMPx.MPxLocatorNode):
        
    def __init__(self):
        OpenMayaMPx.MPxLocatorNode.__init__(self)  

    def draw(self, view, path, style, status): 
        view.beginGL()        
        gl_ft.glDisable(OpenMayaRender.MGL_LIGHTING)       
        gl_ft.glBegin(OpenMayaRender.MGL_POINTS)
        gl_ft.glLineWidth(50)        
        gl_ft.glColor3f(1.0, 0.0, 0.0)
        gl_ft.glVertex3f(0.0, -1.0, 0.0)
        gl_ft.glVertex3f(0.0, 0.0, 0.0)            
        gl_ft.glEnd()
        view.endGL()


def nodeCreator():
    return OpenMayaMPx.asMPxPtr(Connect())

def nodeInitializer():
    pass

