'''
parameters.py 0.0.1 
Date: June 24, 2019
Last modified: August 03, 2019
Author: Subin. Gopi
mail id: subing85@gmail.com

# Copyright 2019, Subin Gopi https://www.subins-toolkits.com/ All rights reserved.
https://www.subins-toolkits.com/

# WARNING! All changes made in this file will be lost!

Description
    None
'''

from maya import OpenMaya
from maya import OpenMayaMPx

from studio_alembic.core import fileIO

reload(fileIO)

class Connect(OpenMayaMPx.MPxCommand):

    k_plugin_name = 'studioAlembic'

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        self.k_type = ['-typ', '-type']
        self.k_select = ['-s', '-select']
        self.k_directory = ['-dir', '-directory']
        self.k_objects = ['-obj', '-objects']        
        self.type_values = ['import', 'export']

    @staticmethod
    def cmdCreator():
        return OpenMayaMPx.asMPxPtr(Connect())

    def syntaxCreator(self):
        syntax = OpenMaya.MSyntax()
        
        syntax.addFlag(
            self.k_type[0], self.k_type[1], OpenMaya.MSyntax.kString)

        syntax.addFlag(
            self.k_select[0], self.k_select[1], OpenMaya.MSyntax.kBoolean)
        
        syntax.addFlag(
            self.k_directory[0], self.k_directory[1], OpenMaya.MSyntax.kString)
        
        syntax.addFlag(
            self.k_objects[0], self.k_objects[1], OpenMaya.MSyntax.kString)
       
        return syntax

    def doIt(self, args):
        args_data = OpenMaya.MArgDatabase(self.syntax(), args)
        
        type = None
        select = True
        directory = None
        objects = None

        if args_data.isFlagSet(self.k_type[0]):
            type = args_data.flagArgumentString(self.k_type[0], 0)
            
        if args_data.isFlagSet(self.k_select[0]):
            select = args_data.flagArgumentBool(self.k_select[0], 0)
           
        if args_data.isFlagSet(self.k_directory[0]):
            directory = args_data.flagArgumentString(self.k_directory[0], 0)
            
        if args_data.isFlagSet(self.k_objects[0]):
            objects = args_data.flagArgumentString(self.k_objects[0], 0)            
        
        print type, select, directory, objects
        fileIO.execute(type, select, directory, objects)  
        # sexim.execute(type, repeat, select, directory, query, objects, clear)
