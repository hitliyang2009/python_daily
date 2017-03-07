#!/bin/bash
#include git commit commands to make work
#use hellp:
#./gitcommit.sh "add commit shell script"

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export PATH

curr_time_str=`date "+%Y-%m-%d %H:%M:%S"`
#note that this statement  tag is print by the key below ESC

des_str="${curr_time_str}---$1"
echo "${des_str} an new commit is called..."

#step 1: add all files into version control
git add .
#step 2: exec commit locally
git commit -m "${des_str}"
#step 3: sync to github
git push origin master
#note that after step 3, github will call you to type in name and password
