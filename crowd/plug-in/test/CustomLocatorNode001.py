import sys
import maya.OpenMaya as OpenMaya  # import du module des classes communes
import maya.OpenMayaMPx as OpenMayaMPx  # import du module des classes de proxy
import maya.OpenMayaRender as OpenMayaRender  # import du module des classes propres au rendu

nodeTypeName = "myCustomLocator"  # le nom du node
nodeTypeId = OpenMaya.MTypeId(0x87079)  # creation de l'id du node

glRenderer = OpenMayaRender.MHardwareRenderer.theRenderer()  # semble recuperer un pointeur vers le renderer hardware utiliser
glFT = glRenderer.glFunctionTable()  # renvois un pointeur vers la "table des fonctions OpenGL"


class myNode(OpenMayaMPx.MPxLocatorNode):

	def __init__(self):
		OpenMayaMPx.MPxLocatorNode.__init__(self)

	def draw(self, view, path, style, status):  # procedure appele au momment du "dessin" du locator

		view.beginGL()  # fonctionne bien sans mais il semble que ce soit necessaire pour eviter les plantages...

		glFT.glBegin(OpenMayaRender.MGL_LINES)  # debut de la primive de type MGL_LINES
		glFT.glVertex3f(0.0, -0.5, 0.0)  # dessine un premier vextex
		glFT.glVertex3f(0.0, 0.5, 0.0)  # dessine le seconde vextex
		glFT.glEnd()  # fin de la primive de type MGL_LINES

		view.endGL()


def nodeCreator():
	return OpenMayaMPx.asMPxPtr(myNode())

 
def nodeInitializer():
	# return OpenMaya.MStatus.kSuccess
	pass

 
def initializePlugin(obj):  # procedure lance au moment de l'initialisation du plugin
	plugin = OpenMayaMPx.MFnPlugin(obj)
	try:
		plugin.registerNode(nodeTypeName, nodeTypeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kLocatorNode)
	except:
		sys.stderr.write("Failed to register node: %s" % nodeTypeName)


def uninitializePlugin(obj):  # procedure lance au moment de la desactivation du plugin
	plugin = OpenMayaMPx.MFnPlugin(obj)
	try:
		plugin.deregisterNode(nodeTypeId)
	except:
		sys.stderr.write("Failed to deregister node: %s" % nodeTypeName)
