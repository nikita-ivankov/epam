#!/bin/bash

#Checking existing of config file
if [[ ! -f "config.cfg" ]] || [[ ! -r "config.cfg" ]]
then
	printf "config.cfg is not a file or doesn't exist or isn't readable, please try again.\n";
else
	SOURCEDIR=$(awk -F "=" '/SOURCEDIR/ {print $2}' config.cfg)
	TARGETDIR=$(awk -F "=" '/TARGETDIR/ {print $2}' config.cfg)
	LOGFILENAME=$(awk -F "=" '/LOGFILENAME/ {print $2}' config.cfg)

	#Checking existing of SOURCEDIR, TARGETDIR directory and existing and availability if LOGFILENAME
	if [[ ! -d "${SOURCEDIR}" ]] || [[ ! -d "${TARGETDIR}" ]] || [[ ! -f "${LOGFILENAME}" ]] || [[ ! -w "${LOGFILENAME}" ]] 
	then
		printf "Some problem with arguments from config file, please try again.\n";
	else
		while true 
		do
			#getting files from SOURCE dir
			if [[ "$(ls -A $SOURCEDIR)" ]]
			then
				for file in $SOURCEDIR/*
				do
					#if last line consists a UUID(1,2,3,4 and 5 types)
					if [[ $(tail -1 $file) =~ ^[0-9A-F]{8}-[0-9A-F]{4}-[1-5][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$ ]]
					then
						#making parts of new name
						first_part=$(awk -F "\t" 'NR==1 {print $1}' $file)
						second_part=$(awk -F "\t" 'NR==1 {print $2}' $file)
						third_part=$(date -r $file +%F)
					
						#if file was moved successfully that make a notice in a log file
						if mv $file /$TARGETDIR/"${first_part}_${second_part}_${third_part}" 2>/dev/null
						then
							echo "$(date +%F-%T) The file $file was successfully moved in $TARGETDIR as ${first_part}_${second_part}_${third_part} " >> log.txt
						fi
					fi

				done
			fi
		done
	fi
fi