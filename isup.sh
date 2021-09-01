#!/bin/bash

figlet "To find Alive Domains with ip in CSV format"
echo "Usage ./isup.sh <domains Name>"
echo "Example ./isup.sh google.com"


echo "$1,";ping -c 1 $1|awk '{print $3}'|egrep '\.'
