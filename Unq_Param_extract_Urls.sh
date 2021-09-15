#!/bin/bash

figlet "Unq Param extract Urls"
echo "Sample Result"
echo -n "Input                                      " ; echo "Output"
echo -n "https://domain.com/path1?param1=value      "
echo "https://domain.com/path1?param1=value"
echo -n "https://domain.com/path2?param1=value      "
echo "https://domain.com/path3?param2=value"
echo "https://domain.com/path3?param2=value"


echo ""
echo "Usage ./unq_param.urls.sh <Filename>"
echo ""

cat $1 |sed 's/?/ /g'|sort -u -k2|sed 's/ /?/g'
