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

from studio_uv.core import exim


class Connect(OpenMayaMPx.MPxCommand):

    k_plugin_name = 'studioUV'

    def __init__(self):
        OpenMayaMPx.MPxCommand.__init__(self)
        self.k_type = ['-typ', '-type']
        self.k_select = ['-s', '-select']
        self.k_repeat = ['-rp', '-repeat']
        self.k_directory = ['-dir', '-directory']
        self.k_query = ['-q', '-query']
        self.k_objects = ['-obj', '-objects']
        self.type_values = ['import', 'export']
        self.select_values = ['all', 'selected', 'auto']

    @staticmethod
    def cmdCreator():
        return OpenMayaMPx.asMPxPtr(Connect())

    def syntaxCreator(self):
        syntax = OpenMaya.MSyntax()
        syntax.addFlag(
            self.k_type[0], self.k_type[1], OpenMaya.MSyntax.kString)
        syntax.addFlag(
            self.k_repeat[0], self.k_repeat[1], OpenMaya.MSyntax.kBoolean)
        syntax.addFlag(
            self.k_select[0], self.k_select[1], OpenMaya.MSyntax.kString)
        syntax.addFlag(
            self.k_directory[0], self.k_directory[1], OpenMaya.MSyntax.kString)
        syntax.addFlag(
            self.k_query[0], self.k_query[1], OpenMaya.MSyntax.kBoolean)
        syntax.addFlag(
            self.k_objects[0], self.k_objects[1], OpenMaya.MSyntax.kString)
        return syntax

    def doIt(self, args):
        args_data = OpenMaya.MArgDatabase(self.syntax(), args)
        type = None
        select = None
        repeat = False
        directory = None
        query = False
        objects = None
        match = False
        if args_data.isFlagSet(self.k_type[0]):
            type = args_data.flagArgumentString(self.k_type[0], 0)
        if args_data.isFlagSet(self.k_select[0]):
            select = args_data.flagArgumentString(self.k_select[0], 0)
        if args_data.isFlagSet(self.k_repeat[0]):
            repeat = args_data.flagArgumentBool(self.k_repeat[0], 0)
        if args_data.isFlagSet(self.k_directory[0]):
            directory = args_data.flagArgumentString(self.k_directory[0], 0)
        if args_data.isFlagSet(self.k_query[0]):
            query = args_data.flagArgumentBool(self.k_query[0], 0)
        if args_data.isFlagSet(self.k_objects[0]):
            objects = args_data.flagArgumentString(self.k_objects[0], 0)
        exim.execute(type, repeat, select, directory, query, objects)
