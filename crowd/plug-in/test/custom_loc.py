import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaRender as OpenMayaRender
import maya.OpenMayaUI as OpenMayaUI

nodeTypeName = "testCustomLocator"
nodeTypeId = OpenMaya.MTypeId(0x87079)

glRenderer = OpenMayaRender.MHardwareRenderer.theRenderer()	
glFT = glRenderer.glFunctionTable()							


class myNode(OpenMayaMPx.MPxLocatorNode):

	def __init__(self):
		OpenMayaMPx.MPxLocatorNode.__init__(self)

	def draw(self, view, path, style, status):				
		print 'path', path
		print 'style', style
		print 'status', status
		
		view.beginGL()							
		
		glFT.glEnable(OpenMayaRender.MGL_BLEND)	
		
		glFT.glBegin(OpenMayaRender.MGL_LINES)
		glFT.glVertex3f(0.0, -0.5, 0.0)			
		glFT.glVertex3f(0.0, 0.5, 0.0)			
		glFT.glEnd()							
		
		if status == OpenMayaUI.M3dView.kLead:
			glFT.glColor4f(1, 0, 0, 0.3)	
		if status == OpenMayaUI.M3dView.kActive:
			glFT.glColor4f(1, 1, 0, 0.4)
		if status == OpenMayaUI.M3dView.kDormant:
			glFT.glColor4f(1, 0, 1, 0.5)
		
		glFT.glBegin(OpenMayaRender.MGL_QUADS)
		glFT.glVertex3f(-0.5, 0.0, -0.5)		
		glFT.glVertex3f(0.5, 0.0, -0.5)			
		glFT.glVertex3f(0.5, 0.0, 0.5)			
		glFT.glVertex3f(-0.5, 0.0, 0.5)			
		glFT.glEnd()							
		
		glFT.glDisable(OpenMayaRender.MGL_BLEND)
		
		view.endGL()


def nodeCreator():
	return OpenMayaMPx.asMPxPtr(myNode())

 
def nodeInitializer():
	pass

 
def initializePlugin(obj):
	print 'aaaaaaaaaaaaaaaaaaaaaaa\t', obj, obj.apiTypeStr()			
	plugin = OpenMayaMPx.MFnPlugin(obj)
	try:
		plugin.registerNode(nodeTypeName, nodeTypeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kLocatorNode)
	except:
		sys.stderr.write("Failed to register node: %s" % nodeTypeName)


def uninitializePlugin(obj):					
	plugin = OpenMayaMPx.MFnPlugin(obj)
	try:
		plugin.deregisterNode(nodeTypeId)
	except:
		sys.stderr.write("Failed to deregister node: %s" % nodeTypeName)
