#!/bin/bash

if [[ "$#" -eq 0 ]]
then
	echo "Usage: ./recursiveSearch.sh <words-to-search>"
	exit 1
fi
# echo $@ are the inputs
grep -inrw $@ Data/ 
