#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	info_color="\e[34m" #darkBlue
	message_color="\e[91m" #light red	
	error_color="\e[31m" #red	    
	warning_color="\e[35m" #magenta	    
	header_color="\e[32m" #green
	normal_color="\e[0m"	
		
	echo -e $header_color"#header: common application"
	echo -e $info_color"	     NAME: "$message_color"Casting Sheet"	
	echo -e $info_color"	  VERSION: "$message_color"0.0.0"
	echo -e $info_color"	   AUTHOR: "$message_color"subin gopi"
	echo -e $info_color"	 MODIFIED: "$message_color"'May:17:2020 - 09:00:01:PM"	
	echo -e $info_color"	COPYRIGHT: "$message_color"(c) 2019, Subin Gopi All rights reserved (Opensource and free tool)"
	echo -e $normal_color
	init="$(dirname -- "$0")/__init__.py"
	python $init
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
		
