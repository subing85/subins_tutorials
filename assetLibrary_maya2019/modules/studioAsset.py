'''
stdioAsset.py 0.0.1 
Date: February 11, 2019
Last modified: February 24, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

import os
import tempfile
import subprocess
import tempfile
import warnings
import platform

from datetime import datetime

from assetLibrary_maya2019.utils import platforms
from assetLibrary_maya2019.modules import readWrite
from assetLibrary_maya2019.modules import studioImage
from assetLibrary_maya2019 import resources


class Asset(object):

    def __init__(self, path=None, paths=None, image=None):
        self.path = path
        self.paths = paths
        self.image = image
        self.tool_kit_object, self.tool_kit_name, self.version = platforms.get_tool_kit()
        self.output_path = tempfile.gettempdir()
        self.asset_setname = 'asset_set'
        self.maya_formats = {'.mb': 'mayaBinary', '.ma': 'mayaAscii'}
        self.maya_file_types = {'mayaBinary': '.mb', 'mayaAscii': '.ma'}
        
    def get_format(self):
        if not self.path:
            return None
        current_format = os.path.splitext(self.path)[-1]
        if current_format not in self.maya_formats:
            return None
        self.maya_type = self.maya_formats[current_format]
        return self.maya_type

    def had_valid(self, publish_file):
        rw = readWrite.ReadWrite(t='asset')
        rw.file_path = publish_file
        result = rw.has_valid()
        return result

    def read_data(self, type, paths):
        rw = readWrite.ReadWrite(t='asset')
        rw.file_path = paths
        result = {True: None}
        asset_data = {}
        for each_path in self.paths:
            rw.file_path = each_path
            if type == 'info':
                data = rw.get_info()
            if type == 'data':
                data = rw.get_data()
            asset_data.setdefault(each_path, data)
        return asset_data

    def create(self, mode, create_type, maya_type=None, fake=False, maya_path=None, output_path=None):
        paths = self.paths
        if fake:
            paths = [self.paths[-1]]
            info_data = self.read_data('info', paths)
            return info_data        
        asset_data = self.read_data('data', self.paths)
        if mode == 'standalone':
            result = self.create_maya_file(
                asset_data, create_type, maya_type, maya_path, output_path)
        if mode == 'maya':
            result = self.create_assets(asset_data, create_type)
        return result

    def create_maya_file(self, asset_data, create_type, maya_type, maya_path, output_path):
        bash_file = os.path.abspath(
            os.path.join(tempfile.gettempdir(), 'asset_library.py')).replace('\\', '/')
        if os.path.isfile(bash_file):
            try:
                os.chmod(folder_path, 0777)
                os.remove(bash_file)
            except:
                pass
        core_type = 'core.createReference(asset_path, iv=True, ns=asset_name)'
        if create_type == 'import':
            core_type = 'core.importFile(asset_path, iv=True, ns=asset_name)'
        if not output_path:
            output_path = tempfile.gettempdir()
        current_time = datetime.now().strftime('%Y_%d_%B_%I_%M_%S_%p')
        output_file = os.path.abspath(os.path.join(
            output_path, 'asset_bundle_{}.{}'.format(current_time, self.maya_file_types[maya_type])))        
        output_file = output_file.replace('\\', '/')
        data = [
            '#!{}/bin/mayapy'.format(maya_path),
            'from maya import standalone',
            'standalone.initialize(name="python")',
            'from pymel import core',
            'data = {}'.format(asset_data),
            'for each_asset in  data:',
            '\tasset_name = data[each_asset][\'name\']',
            '\tasset_path = data[each_asset][\'path\']',
            '\tasset_format = data[each_asset][\'format\']',
            '\t{}'.format(core_type),
            '\tprint \"\\n\", \"asset name\", \"\\t=\" , asset_name',
            '\tprint \"{}\", \"\\t=\", asset_path'.format(create_type),            
            '\ttry:',
            '\t\tcore.saveAs(\'{}\', typ=\'{}\')'.format(output_file, maya_type),
            '\texcept Exception as error:',
            '\t\t\"save error\", error',
            'standalone.uninitialize(name=\'python\')'
            ]
        bash_data = open(bash_file, 'w')
        try:
            bash_data.write('\n'.join(data))
        except Exception as error:
            warnings.warn(str(error), Warning)
        finally:
            bash_data.close()
        try:
            os.chmod(bash_file, 0o777)
        except Exception as error:
            warnings.warn(str(error), Warning)		
        if platform.system()=='Windows':	    
            mayapy = os.path.abspath(os.path.join(maya_path, 'bin/mayapy.exe')).replace('\\', '/')
            windows_command = '\"{}\" \"{}\"'.format(mayapy, bash_file)
            result = subprocess.call(
            windows_command, stdout=None, shell=True, stderr=None)	
        if platform.system()=='Linux':
            result = subprocess.call(
            bash_file, stdout=None, shell=True, stderr=None)            
        if os.path.isfile(bash_file):
            try:
                os.chmod(bash_file, 0777)
                os.remove(bash_file)
            except Exception as result:
                print(result)            
        return output_file

    def create_assets(self, asset_data, create_type):
        from pymel import core
        self.set_bounding_box()
        for each_asset in asset_data:
            asset_name = asset_data[each_asset]['name']
            asset_path = asset_data[each_asset]['path']
            asset_format = asset_data[each_asset]['format']
            if create_type == 'reference':
                core.createReference(asset_path, iv=True, ns=asset_name)
            if create_type == 'import':
                core.importFile(asset_path, iv=True, ns=asset_name)
        return True

    def save(self, file_path, name, user_comment=None):
        comment = '%s %s - asset' % (
            self.tool_kit_name, self.version)
        if user_comment:
            comment = '%s %s - asset\n%s' % (
                self.tool_kit_name, self.version, user_comment)
        created_date = datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')
        description = 'This data contain information about asset'
        type = 'asset'
        valid = True
        format = self.get_format()
        data = {
            'name': name,
            'path': self.path,
            'format': format
            }
        tag = self.tool_kit_object
        rw = readWrite.ReadWrite(c=comment, cd=created_date,
                 d=description, t=type, v=valid, data=data, tag=tag,
                 path=file_path, name=name, format='asset')
        result, asset_path = rw.create()
        if False in result:
            return result
        studio_image = studioImage.ImageCalibration(
            path=file_path, name=name, format='png')
        image_path = studio_image.writeImage(self.image)
        print '\nresult', asset_path, image_path
        return result

    def had_file(self, dirname, name):
        rw = readWrite.ReadWrite(
            path=dirname, name=name, format='asset', t='asset')
        return rw.has_file()

    def get_image(self, asset_path):
        return asset_path.replace('.asset', '.png')

    def set_bounding_box(self):
        from pymel import core
        panels = core.getPanel(type='modelPanel')
        for each_panel in panels:
            core.modelEditor(each_panel, e=True, da='boundingBox')


# end ####################################################################
