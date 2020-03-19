#!/bin/bash

# CURRENT_PATH=$(pwd -P)
CURRENT_PATH="/venture/source_code/subins_tutorials"

echo $CURRENT_PATH
export STUDIO_PATH=$CURRENT_PATH
export PYTHONPATH=$PYTHONPATH:$CURRENT_PATH
export PATH=$CURRENT_PATH/studio_usd_pipe/bin

echo ""
echo "Studio USD PIPE <Preference> 0.0.1"
echo "0.0.1 Release"
echo "www.subins-toolkits.comm"
echo "subing85@gmail.com"
echo ""

echo $STUDIO_PATH"/studio_usd_pipe/bin/publish.py"

preferences
# End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :