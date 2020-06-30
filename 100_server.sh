#!/bin/bash
list=("saltmaster001" "shellserver001" "consul001" "consul002")
result=''
for i in ${list[@]}
do
        ssh $i -p 22 "pgrep consul > /dev/null"
        if [ $? -eq 0 ]
        then
                result="${result} Process is running for ${i} \n."
        else
                result="${result} Process is not running for ${i} \n."
        fi
done

# echo $result
echo $array | mail -s "list of the runnin servers" "jkhunt@ebay.com"