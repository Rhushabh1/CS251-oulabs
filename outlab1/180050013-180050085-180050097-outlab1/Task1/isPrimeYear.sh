#!/bin/bash

# bc <<< 'scale=4; 100/3'
# year=$1
# echo $year
# e=$( echo "sqrt(10)" | bc -l )
# echo $e

# is_positive_int () {
# 	# rem=$(( bc <<< 'scale=4; $1%1.0' ))
# 	# rem=$(( 2.5+3.75 | bc ))
# 	rem=$( echo "$1%1" | bc -l )
# 	echo $rem is the remainder
# 	if [ $1 -ge 0 ] && (( $(echo "$rem == 0" | bc -l) ))
# 		# [ $rem -eq 0.0 ]
# 	then 
# 		echo $1 is positive integer
# 		# return $true
# 	else 
# 		echo $1 is not a positive integer
# 		# return $false
# 	fi
# }

# echo "10.22 == 0" | bc -l 
# is_positive_int $year

year=$1

re='^[0-9]+$'
if ! [[ $year =~ $re ]] ; then
   echo "Invalid argument!" >&2; exit 1
fi

is_prime () {
	if [ $1 -le 1 ]
	then
		echo Not a prime year 
		exit 1
	fi

	counter=2
	while [ $counter -lt $1 ]
	do 
		rem=$(( $1 % $counter ))
		# echo $counter - $rem
		if (( $rem == 0 ))
		then 
			echo Not a prime year.
			exit 1
		fi

		(( counter++ ))

	done

	echo Prime Year!
}

is_prime $year
