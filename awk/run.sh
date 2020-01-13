echo "Would you like to show outcome in percent?(y/n)"
read result_type

until [[ "$result_type" == "y" ]] || [[ "$result_type" == "n" ]]
do
	echo "Choose y or n, please"
	read result_type
done

awk 'BEGIN { for (i=1;i<200;i++)  print int (101*rand()) }' | awk -v result_type=$result_type -f historgam