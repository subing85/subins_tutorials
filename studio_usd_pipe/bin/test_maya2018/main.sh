#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	echo -e "\e[1m\e[34m#header: maya bundle"
	echo -e "\e[0m\e[36m	SHOW NAME: "$SHOW_NAME
	echo -e "	BUNDLE NAME: "$BUNDLE_NAME"\e[0m"
	# echo $PACKAGE_PATH"/"$PACKAGE_NAME"/bin/"$BUNDLE_NAME"/__init__.py"
	# python $PACKAGE_PATH"/"$PACKAGE_NAME"/bin/launcher/__init__.py"
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
		
