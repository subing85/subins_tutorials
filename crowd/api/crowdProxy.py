from maya import OpenMaya
from maya import OpenMayaMPx
from maya import OpenMayaUI
from maya import OpenMayaRender

from crowd.api import crowdSetup
from crowd.api import crowdAttributes
reload(crowdAttributes)
reload(crowdSetup)


class Connect(OpenMayaMPx.MPxCommand):

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        self.attr = crowdAttributes.Connect()
        self.k_create = ['-c', '-create']
        self.k_type = ['-%s'%self.attr.k_type[0], '-%s'%self.attr.k_type[1]]
        self.k_count = ['-%s'%self.attr.k_count[0], '-%s'%self.attr.k_count[1]]
        self.k_distance = ['-%s'%self.attr.k_distance[0], '-%s'%self.attr.k_distance[1]]
        self.k_row = ['-%s'%self.attr.k_row[0], '-%s'%self.attr.k_row[1]]
        self.k_column = ['-%s'%self.attr.k_column[0], '-%s'%self.attr.k_column[1]]
        self.k_row_offset = ['-%s'%self.attr.k_row_offset[0], '-%s'%self.attr.k_row_offset[1]]
        self.k_column_offset = ['-%s'%self.attr.k_column_offset[0], '-%s'%self.attr.k_column_offset[1]]
        
        self.k_random = ['-%s'%self.attr.k_random[0], '-%s'%self.attr.k_random[1]]

    @staticmethod
    def cmdCreator():
        return OpenMayaMPx.asMPxPtr(Connect())

    def doIt(self, args):
        print "Hello World!"

        type = 'biped'
        count = 53
        distance = 20
        row = 5
        column = 5
        row_offset = 0
        column_offset = 0
        random = 0

        args_data = OpenMaya.MArgDatabase(self.syntax(), args)

        if args_data.isFlagSet(self.k_type[0]):
            type = args_data.flagArgumentString(self.k_type[0], 0)
 
        if args_data.isFlagSet(self.k_count[0]):
            count = args_data.flagArgumentInt(self.k_count[0], 0)

        if args_data.isFlagSet(self.k_distance[0]):
            count = args_data.flagArgumentInt(self.k_distance[0], 0)

        if args_data.isFlagSet(self.k_row[0]):
            row = args_data.flagArgumentInt(self.k_row[0], 0)

        if args_data.isFlagSet(self.k_column[0]):
            column = args_data.flagArgumentInt(self.k_column[0], 0)
       
        if args_data.isFlagSet(self.k_row_offset[0]):
            row_offset = args_data.flagArgumentDouble(self.k_row_offset[0], 0)

        if args_data.isFlagSet(self.k_column_offset[0]):
            column_offset = args_data.flagArgumentDouble(self.k_column_offset[0], 0)
             
        if args_data.isFlagSet(self.k_random[0]):
            random = args_data.flagArgumentDouble(self.k_random[0], 0)

        print 'row', row
        print 'column', column

         
        if args_data.isFlagSet(self.k_create[0]):
            create = args_data.flagArgumentBool(self.k_create[0], 0)

            crowd_setup = crowdSetup.Connect(
                type=type,
                count=count,
                distance = distance,
                row=row,
                column=column,
                rowOffset=row_offset,
                columnOffset=row_offset,
                random=random
                )
            crowd_setup.create()

    def syntaxCreator(self):
        syntax = OpenMaya.MSyntax()
        syntax.addFlag(self.k_create[0], self.k_create[1], OpenMaya.MSyntax.kBoolean)
        syntax.addFlag(self.k_type[0], self.k_type[1], OpenMaya.MSyntax.kString)
        syntax.addFlag(self.k_row[0], self.k_row[1], OpenMaya.MSyntax.kDouble)
        syntax.addFlag(self.k_column[0], self.k_column[1], OpenMaya.MSyntax.kDouble)
        syntax.addFlag(self.k_row_offset[0], self.k_row_offset[1], OpenMaya.MSyntax.kDouble)
        syntax.addFlag(self.k_column_offset[0], self.k_column_offset[1], OpenMaya.MSyntax.kDouble)
        syntax.addFlag(self.k_random[0], self.k_random[1], OpenMaya.MSyntax.kDouble)
        
        
        return syntax
