#!/bin/bash

current_path=`pwd`
export STUDIO_PATH=$current_path
export PYTHONPATH=$current_path

echo ""
echo "Asset Library"
echo "0.0.1 Release"
echo "www.subins-toolkits.comm"
echo "subing85@gmail.com"
echo ""

python $STUDIO_PATH"/assetLibrary/__init__.py"
# End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :