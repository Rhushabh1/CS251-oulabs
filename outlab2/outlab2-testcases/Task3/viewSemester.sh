#!/bin/bash
sed -n -e '1,3 p' $1
grep -w $2 $1 | grep -w $3 | sort -k3  
