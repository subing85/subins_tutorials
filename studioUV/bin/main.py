from maya import OpenMaya
from maya import OpenMayaMPx

from studioUV.core import exim
reload(exim)

class Connect(OpenMayaMPx.MPxCommand):

    k_plugin_name = 'studioUV'

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)

        self.k_type = ['-typ', '-type']
        self.k_select = ['-s', '-select']
        self.k_directory = ['-dir', 'directory']

        self.type_values = ['import', 'export']
        self.select_values = ['all', 'selected']

    @staticmethod
    def cmdCreator():
        return OpenMayaMPx.asMPxPtr(Connect())

    def syntaxCreator(self):
        syntax = OpenMaya.MSyntax()
        syntax.addFlag(
            self.k_type[0], self.k_type[1], OpenMaya.MSyntax.kString)
        syntax.addFlag(
            self.k_select[0], self.k_select[1], OpenMaya.MSyntax.kString)
        
        syntax.addFlag(
            self.k_directory[0], self.k_directory[1], OpenMaya.MSyntax.kString)
        
        return syntax

    def doIt(self, args):
        print "Subin uv export import!..."
        '''
        from pymel import core
        core.studioUV(
            typ='export', s='selected', dir='/venture/subins_tutorials/studioUV/test.uv')
        '''
        args_data = OpenMaya.MArgDatabase(self.syntax(), args)

        type = None
        select = None
        directory = None
        if args_data.isFlagSet(self.k_type[0]):
            type = args_data.flagArgumentString(self.k_type[0], 0)

        if args_data.isFlagSet(self.k_select[0]):
            select = args_data.flagArgumentString(self.k_select[0], 0)
            
        if args_data.isFlagSet(self.k_directory[0]):
            directory = args_data.flagArgumentString(self.k_directory[0], 0)
            
        if type not in self.type_values:
            OpenMaya.MGlobal.displayError(
                '\"typ\" or \"type\" flag value should be %s' % self.type_values)
            return

        if select not in self.select_values:
            OpenMaya.MGlobal.displayError(
                '\"s\" or \"select\" flag value should be %s' % self.select_values)
            return

        if not type or not select or not directory:
            message = [
                '\n\"typ\" or \"type\" flag value should be %s'%self.type_values,
                '\"s\" or \"select\" flag value should be %s'%self.select_values,
                '\"dir\" or \"directory\" flag value should be [\'path\']'
            ]
            OpenMaya.MGlobal.displayError('\n'.join(message))
            return        
        
        print 'type\t', type
        print 'select\t', select
        print 'directory\t', directory
        
        exim.execute(type, select, directory)
        
