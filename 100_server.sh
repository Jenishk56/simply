#!/bin/bash
list=("saltmaster001" "shellserver001" "consul001" "consul002")

for i in ${list[@]}
do
        ssh $i "pgrep consul > /dev/null"
        if [ $? -eq 0 ]
        then
                echo "Process is running for ${i}."
        else
                echo "Process is not running."
        fi
done