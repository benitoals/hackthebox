#!/bin/bash

for i in *.JPG
do
	echo bullshit | kpcli --kbd MyPasswords.kdbx --key $i --command quit >/dev/null 2>&1
	if [[ $? -eq 0 ]] 
	then
		echo "key: $i"
		break	
	fi
done
