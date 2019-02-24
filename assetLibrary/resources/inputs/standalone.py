from maya import standalone
standalone.initialize(name='python')

publish_paths = ['/venture/temp/library/asset_library/characters/alice.asset']
studio_asset = studioAsset.Asset(paths=publish_paths)
result = studio_asset.create('standalone', 'reference')