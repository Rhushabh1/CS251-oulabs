#!/bin/bash

pa="howFarFromTruth.txt"
if [[ -e $pa ]]; then
	rm $pa
fi
r=34
c=0
while [[ $r -ne 42 ]]; do
	(( r = $( ./../A/randomNumber.sh 2 ) )) 
	((c=c+1))
	echo $r >> $pa
done
echo $c