#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	echo -e "\e[1m\e[34m#header: maya bundle"
	echo -e "\e[0m\e[36m	SHOW NAME: "$SHOW_NAME
	echo -e "	BUNDLE NAME: "$BUNDLE_NAME"\e[0m"
	/opt/katana/katana3.2.3/katana
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
		
