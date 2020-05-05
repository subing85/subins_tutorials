#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	echo -e "\e[1m\e[34m#header: maya bundle"
	echo -e "\e[0m\e[36m	       SHOW NAME: "$SHOW_LONG_NAME
	echo -e "	APPLICATION NAME: "$APPLICATION_NAME"\e[0m"
	/usr/autodesk/maya2018/bin/maya2018
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
