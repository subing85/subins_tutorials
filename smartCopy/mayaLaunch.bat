:  !/bin/bash

:  Maya Launcher
:  Version=1.0.0 Release.
:  Date : March 28, 2018
:  Last modified: March 28, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:	WARNING! All changes made in this file will be lost!

:   Description
:		This module contain all input value for the Gimp.  


set MAYA_VERSION=Maya2016
set MAYA_PATH=C:/Program Files/Autodesk/%MAYA_VERSION%/bin/maya.exe
set PYTHONPATH=D:/MyScripts/pythonApplication/subinTutorials
set PUPPETCS_PATH=%PUPPETCS_PATH%

echo ""
echo "................................................................"
echo "Maya"
echo %MAYA_VERSION%
echo %MAYA_PATH%
echo "Loading Maya, please wait .............................."
echo ""

echo %MAYA_PATH%

start "" "%MAYA_PATH%"

:pause

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :