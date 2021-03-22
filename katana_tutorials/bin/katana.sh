#!/bin/bash

BIN_PATH=$(dirname "$0")

PACKAGE_PATH=`python $BIN_PATH"/__init__.py"`

KEY=" "
read -a strarr <<< "$PACKAGE_PATH"

SHOW_PATH=${strarr[0]}
PIPE_PATH=${strarr[1]}

KATANA_VERSION="Katana2.6v4"

# more environment vriables
# https://learn.foundry.com/katana/2.5/dev-guide/EnvironmentVariables.html
# https://rmanwiki.pixar.com/display/RFK/Environment+Variables+in+Katana

RMANTREE="/opt/pixar/RenderManProServer-21.6"
RMAN_RESOURCES="/opt/pixar/RenderManForKatana-21.6-katana2.6/plugins/Resources/PRMan21"

PIPE_RESOURCES=$PIPE_PATH"/resources"

# https://graphics.pixar.com/usd/docs/Katana-USD-Plugins.html
#pixar USD
USD_INSTALL_ROOT="/usr/usd/katana2.6v4/19.05"
USD_PYTHON_PATH=$USD_INSTALL_ROOT"/lib/python"


# set python env path
export PYTHONPATH=$PYTHONPATH:$PIPE_PATH:$USD_PYTHON_PATH

# set show and pipe path
export SHOW_PATH=$SHOW_PATH
export PIPE_PATH=$PIPE_PATH

# set prman env path
export RMANTREE=$RMANTREE
export KATANA_RESOURCES=$KATANA_RESOURCES:$RMAN_RESOURCES:$PIPE_RESOURCES

echo "................................................"
echo "Katana Python Tutorial"
echo "Katana Version: "$KATANA_VERSION
echo "SHOW_PATH: " $SHOW_PATH
echo "PIPE_PATH: " $PIPE_PATH
echo "Katana Third-Party Resources"
echo "	1. PRMan21(RenderManForKatana-21.6-katana2.6)"
echo "................................................"

# execute katana
/usr/foundry/katana/$KATANA_VERSION/katana
