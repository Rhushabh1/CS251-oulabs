#!/bin/bash

limit=2019

# ans=$( bash ./isPrimeYear.sh $limit )
# echo $ans

# touch ​numberOfPrimeYears.txt
dest_file=​numberOfPrimeYears.txt
touch $dest_file

year=1

while [ $year -le $limit ]
do
	found=1
	if [ $year -le 1 ]
	then 
		(( year++ ))
		continue
	fi 

	counter=2
	while [ $counter -lt $year ]
	do 
		rem=$(( $year % $counter ))
		# echo $counter - $rem
		if (( $rem == 0 ))
		then 
			found=0
			break
		fi

		(( counter++ ))

	done

	if [ $found -eq 1 ]
	then
		echo $year >> $dest_file
		echo $year is prime 
	fi

	(( year++ ))
done