#!/bin/bash
#
#  Studio Bash 1.0.0
#  Date : April 22, 2020
#  Last modified: Friday April 24, 2020 12:12 PM
#  Author# Subin. Gopi (subing85@gmail.com)
#  Copyright (c) 2018, Subin Gopi
#  All rights reserved.
#
#   WARNING! All changes made in this file will be lost!
#
#  Description
#      This bash module for configure studio usd pipe package and bundles.  

# clear


function studio()
	{
	
		PACKAGE_PATH="/venture/source_code/subins_tutorials"
		PACKAGE_NAME="studio_usd_pipe"	

		if [ $PACKAGE_PATH = "temp" ]; then
			echo "#warnings please run the setup.py file and try!.."
			return
		fi
		
		if [ ! -d "$PACKAGE_PATH" ]; then
			echo "#warnings cannot access" $PACKAGE_PATH "No such file or directory!..."
			return
		fi
			
		export PACKAGE_PATH=$PACKAGE_PATH
		export PACKAGE_NAME=$PACKAGE_NAME		
		export PYTHONPATH=$PACKAGE_PATH
		
			
		PACKAGE_PATH="/venture/source_code/subins_tutorials"
		PACKAGE_NAME="studio_usd_pipe"
		
		bin_path=$PACKAGE_PATH"/"$PACKAGE_NAME"/bin/"

		get_bundles $bin_path bundles
	
		if [ $1 = "-b" ] || [ $2 = "-v" ]; then
			echo "Avilable bulndles are"
			let count=1	
			for each_bundle in ${bundles[@]}; do
				echo "  "$count". [ "$each_bundle" ]"
				((count++))
			done
		fi
		
		
		if [ $1 = "launcher" ]; then
			export BUNDLE_NAME=$1
			source $bin_path$1"/main.sh"
			return
		fi
		
		
		if [ $1 = "-s" ] || [ $3 = "-b" ]; then
			export SHOW_NAME=$2
			export BUNDLE_NAME=$4			
			source $bin_path$4"/main.sh"
		fi
	}

function get_bundles()
	{
		cd $1
		packages=`ls -D`
		declare -a bundle_list			
		let count=0		
		for package in $packages; do
			full_path=$1"/"$package
			if [ -d "$full_path" ]; then
				main=$full_path"/main.sh"
				if [ -f "$main" ]; then
					bundle_list[$count]=$package
					((count++))					
				fi
			fi
		done
	    local result_var=$2
	    local results=${bundle_list[@]}
	    eval $result_var="'$results'"
	}


# studio $1
studio $1 $2 $3 $4
