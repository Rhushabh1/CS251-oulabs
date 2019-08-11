#!/bin/bash

read text

chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

ord() {
  LC_CTYPE=C printf '%d' "'$1"
}

dual=ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ

key=$1
	
newphrase=$(echo $text | tr "${dual:0:26}" "${dual:$key:26}")
echo $newphrase