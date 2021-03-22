import os
import glob
import json

from distutils import version
    
PATTERN = {
    'major': 0,
    'minor': 1,
    'patch': 2
    }


def get_versions(location, mode):
    dirname = os.path.join(location, mode)
    versions = glob.glob1(dirname, '*.*.*')
    sorted_versions = sorted(versions, key=version.StrictVersion)
    sorted_versions.reverse()
    return sorted_versions


def get_latest_version(location, mode):
    versions = get_versions(location, mode)
    if not versions:
        return None
    return versions[0]


def get_next_version(index, latest_version):  # **
    '''
        index 0, 1, 2 = MAJOR0, MINOR, PATCH
    '''
    if not latest_version:
        return '0.0.0'
    major, minor, patch = latest_version.split('.')
    if index == 0:
        n_version = '{}.{}.{}'.format(int(major) + 1, 0, 0)
    if index == 1:
        n_version = '{}.{}.{}'.format(major, int(minor) + 1, 0)
    if index == 2:
        n_version = '{}.{}.{}'.format(major, minor, int(patch) + 1)
    return n_version


def make_sorted_versions(versions):    
    sorted_versions = sorted(versions, key=version.StrictVersion)
    sorted_versions.reverse()
    return sorted_versions


def get_asset_dependency_versions(show_path, category, name, origin, dependency):
    '''
    :description get the asset depnendency versions
    :param show_path <str>
    :param category <str>
    :paraam name <str>
    :param origin <str>
    :param depnendency <str>    
    :example
        from core import versions
        show_path = '/venture/shows/katana_tutorials'
        category = 'character'
        name = 'batman'
        origin = 'lookdev'
        dependency = 'model'
        versions.get_asset_dependency_versions(show_path, category, name, origin, dependency)    
    '''
    origin_path = os.path.join(
        show_path,
        'asset',
        category,
        name
        )
    origin_versions = get_versions(origin_path, origin)
    dependencies = {}
    for origin_version in origin_versions:
        manifest = os.path.join(
            origin_path, origin, origin_version, 'manifest.json')  
        if not os.path.isfile(manifest):
            dependencies.setdefault('invalid', []).append(origin_version)
            continue               
        with(open(manifest, 'r')) as file:
            data = json.load(file)
            if 'data' not in data:
                dependencies.setdefault('invalid', []).append(origin_version)
                continue
            if dependency not in data['data']:
                dependencies.setdefault('invalid', []).append(origin_version)
                continue                
            current_dependency = data['data'][dependency]
            dependencies.setdefault(current_dependency, []).append(origin_version)
    print '#info: asset %s depnendency'%dependency
    print dependency, '[%s]'% origin
    print json.dumps(dependencies, indent=4)
    return dependencies

