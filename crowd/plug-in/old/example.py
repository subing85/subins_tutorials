mport maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import sys, math
kPluginCmdName = "spHelix"
kPitchFlag = "-p"
kPitchLongFlag = "-pitch"
kRadiusFlag = "-r"
kRadiusLongFlag = "-radius"


# command
class scriptedCommand(OpenMayaMPx.MPxCommand):

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
    
    def doIt(self, args):
        deg = 3
        ncvs = 20
        spans = ncvs - deg
        nknots = spans + 2 * deg - 1
        radius = 4.0
        pitch = 0.5
        
        # Parse the arguments.
        argData = OpenMaya.MArgDatabase(self.syntax(), args)
        if argData.isFlagSet(kPitchFlag):
            pitch = argData.flagArgumentDouble(kPitchFlag, 0)
        if argData.isFlagSet(kRadiusFlag):
            radius = argData.flagArgumentDouble(kRadiusFlag, 0)
        controlVertices = OpenMaya.MPointArray()
        knotSequences = OpenMaya.MDoubleArray()
        
        # Set up cvs and knots for the helix
        for i in range(0, ncvs):
            controlVertices.append(OpenMaya.MPoint(radius * math.cos(i),
                pitch * i, radius * math.sin(i)))
        for i in range(0, nknots):
            knotSequences.append(i)
        
        # Now create the curve
        curveFn = OpenMaya.MFnNurbsCurve()
        
        nullObj = OpenMaya.MObject()
        try:
            # This plugin normally creates the curve by passing in the
            # cv's. A function to create curves by passing in the ep's
            # has been added. Set this to False to get that behaviour.
            if True:
                curveFn.create(controlVertices, knotSequences, deg, OpenMaya.MFnNurbsCurve.kOpen, 0, 0, nullObj)
            else:
                curveFn.createWithEditPoints(controlVertices, 3, OpenMaya.MFnNurbsCurve.kOpen, False, False, False)
        except:
            sys.stderr.write("Error creating curve.\n")
            raise


# Creator
def cmdCreator():
    # Create the command
    return OpenMayaMPx.asMPxPtr(scriptedCommand())


# Syntax creator
def syntaxCreator():
    syntax = OpenMaya.MSyntax()
    syntax.addFlag(kPitchFlag, kPitchLongFlag, OpenMaya.MSyntax.kDouble)
    syntax.addFlag(kRadiusFlag, kRadiusLongFlag, OpenMaya.MSyntax.kDouble)
    return syntax


# Initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject, "Autodesk", "1.0", "Any")
    try:
        mplugin.registerCommand(kPluginCmdName, cmdCreator, syntaxCreator)
    except:
        sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
        raise

        
# Uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(kPluginCmdName)
    except:
        sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)
        raise
