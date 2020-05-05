#!/bin/bash
ENABLE=True

if [ $ENABLE = "True" ]; then
	info_color="\e[34m" #darkBlue
	message_color="\e[91m" #light red	
	error_color="\e[31m" #red	    
	warning_color="\e[35m" #magenta	    
	header_color="\e[32m" #green
	normal_color="\e[0m"	
		
	echo -e $header_color"#header: build-in application"
	echo -e $info_color"	     NAME: "$message_color"linux konsole"	
	echo -e $info_color"	  VERSION: "$message_color"2.10.5"
	echo -e $normal_color
	/usr/bin/ipython
else
	echo -e "\e[31m#warnings "$BUNDLE_NAME" is enabled!..\e[0m"
fi
		
