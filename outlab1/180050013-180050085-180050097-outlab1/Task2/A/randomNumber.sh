#!/bin/bash

n=$1
 # $ od -An -N2 -i /dev/urandom

randomgen(){
result=0
while [[ $result -eq 0 ]]; do
	result=$(od -vAn -N1 -tu1 < /dev/urandom)
	((result%=10))
done

for (( i = 1; i < $n; i++ )); do
	temp=$(od -vAn -N1 -tu1 < /dev/urandom)
	((temp%=10))
	((result=result*10+temp))
done
echo $result
}

randomgen

# echo $od
# echo rand is $dd
