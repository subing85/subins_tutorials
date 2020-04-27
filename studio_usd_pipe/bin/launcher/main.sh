#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	echo -e "\e[1m\e[34m#header: studio launcher"
	echo -e "\e[0m\e[36m	     NAME: \e[31mStudio Launcher"	
	echo -e "\e[0m\e[36m	  VERSION: \e[31m0.0.0"
	echo -e "\e[0m\e[36m	   AUTHOR: \e[31msubin gopi"
	echo -e "\e[0m\e[36m	 MODIFIED: \e[31mOctober:24:2019 - 09:00:01:PM"	
	echo -e "\e[0m\e[36m	COPYRIGHT: \e[31m(c) 2019, Subin Gopi All rights reserved (Opensource and free tool)"
	init="$(dirname -- "$0")/__init__.py"
	python $init
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
		
