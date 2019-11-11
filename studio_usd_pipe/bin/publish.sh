#!/bin/bash

# CURRENT_PATH=$(pwd -P)
CURRENT_PATH="/venture/subins_tutorials"

echo $CURRENT_PATH
export STUDIO_PATH=$CURRENT_PATH
export PYTHONPATH=$PYTHONPATH:$CURRENT_PATH

echo ""
echo "Studio USD PIPE <Asset Publish> 0.0.1"
echo "0.0.1 Release"
echo "www.subins-toolkits.comm"
echo "subing85@gmail.com"
echo ""

python $STUDIO_PATH"/studio_usd_pipe/bin/publish.py"
# End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :