function change_template {

#Checking the number of arguments
if [[ $# -ne 4 ]]; then
		echo "You must input two arguments:
		-t/--template - is a file with template,
		-r/--result - is a file to output result of script
		Try againg please." >&2
		return 1
		break
else
	#checking arguments
	while [[ $# -gt 0 ]]; do
		case "$1" in
			-t | --template ) TEMPLATE_FILE="$2"; shift 2;;
			-r | --result ) RESULT_FILE="$2"; shift 2;;
			*) printf "You have inputed the wrong argument[s], please try again." >&2
				return 1
				break;; 
		esac
	done
fi

#Checking existing of TEMPLATE file
if [[ ! -f "${TEMPLATE_FILE}" ]]; then
	echo "Input ${TEMPLATE_FILE} is not a file or doesn't exist, please try again." >&2
	return 1;
	break;
fi

#Checking access to TEMPLATE file
if [[ ! -r "${TEMPLATE_FILE}" ]]; then
	echo "Input ${TEMPLATE_FILE} is not readable, please try again." >&2
	return 1;
	break;
fi

touch $RESULT_FILE && echo > $RESULT_FILE

#If all right go on - read TEMPLATE file line by line
while read LINE
do
	#In case when there are more than one var in a single line
	NEW_LINE=$(echo $LINE)

	#Split input line, delimiter may be diffirent(key -d in cut)
	for i in $(echo $LINE | cut -d" " -f1-)
	do
		#if this word is a pattern
		if [[ "$i" =~ \{.*\} ]]; then
			#remove signs of pattern
			index=$(echo $i | sed 's/[{-}]//g')

			#change \,/,& to \/, \\, \& for futher sed processing
			first=$(echo $i | sed 's/[\/&]/\\&/g')
			second=$(echo ${!index} | sed 's/[\/&]/\\&/g')
			#make change
			NEW_LINE=$(echo $NEW_LINE | sed 's/'$first'/'$second'/g')
		fi
	done
	#Output result in RESULT file
	echo $NEW_LINE >> $RESULT_FILE
done < $TEMPLATE_FILE

printf "Successfully done.\n"
}

change_template $@

