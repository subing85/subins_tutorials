'''
mayaNodes.py 0.0.1 
Date: February 2, 2019
Last modified: June 13, 2019
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2019, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    None.
'''

from pymel import core


def unknown_types():
    node_types = [
        'lightLinker',
        'materialInfo',
        'nodeGraphEditorInfo',
        'partition',
        'groupId',
        'hyperShadePrimaryNodeEditorSavedTabsInfo',
        'renderPartition',
        'timeToUnitConversion'
    ]
    return node_types


def default_nodes():
    nodes = [
        'time1',
        'defaultLightList1',
        'defaultShaderList1',
        'postProcessList1',
        'defaultRenderUtilityList1',
        'defaultRenderingList1',
        'lightList1',
        'defaultTextureList1',
        'lambert1',
        'particleCloud1',
        'initialShadingGroup',
        'initialParticleSE',
        'initialMaterialInfo',
        'shaderGlow1',
        'dof1',
        'defaultRenderGlobals',
        'defaultRenderQuality',
        'defaultResolution',
        'defaultLightSet',
        'defaultObjectSet',
        'defaultViewColorManager',
        'defaultColorMgtGlobals',
        'hardwareRenderGlobals',
        'characterPartition',
        'defaultHardwareRenderGlobals',
        'ikSystem',
        'hyperGraphInfo',
        'hyperGraphLayout',
        'globalCacheControl',
        'strokeGlobals',
        'dynController1',
        'lightLinker1',
        'layerManager',
        'defaultLayer',
        'renderLayerManager',
        'defaultRenderLayer',
        'hyperShadePrimaryNodeEditorSavedTabsInfo',
        'materialInfo1',
        'renderPartition',
        'renderGlobalsList1',
        'defaultLightList1',
    ]
    return nodes


def attribute_types():
    attr_types = [
        'bool',
        'byte',
        'enum',
        'string',
        'long',
        'short',
        'typed',
        'float3',
        'float',
        'TdataCompound',
        'matrix',
        'time',
        'float2',
        'double',
        'doubleAngle',
        'char'
        'attributeAlias'
    ]
    return attr_types


def valid_attribute():
    attr_types = [
        'bool',
        'byte',
        'enum',
        'string',
        'long',
        'short',
        'typed',
        'float3',
        'float',
        'TdataCompound',
        'time',
        'float2',
        'double',
        'doubleAngle',
        'char'
    ]
    return attr_types


def getShadingNodeTypes():
    shader_types = core.listNodeTypes('shader')
    texture_types = core.listNodeTypes('texture')
    utility_types = core.listNodeTypes('utility')
    texture3d_types = core.listNodeTypes('texture/3D')
    textureenv_types = core.listNodeTypes('texture/Environment')
    light_types = core.listNodeTypes('light')
    rendering_types = core.listNodeTypes('rendering')
    postprocess_types = core.listNodeTypes('postProcess')

    node_types = {
        'shader': shader_types,
        'texture': texture_types + texture3d_types + textureenv_types,
        'utility': utility_types,
        'light': light_types,
        'rendering': rendering_types,
        'postProcess': postprocess_types
    }
    return node_types
