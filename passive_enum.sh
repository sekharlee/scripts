#!/bin/bash

echo "Final Output is stored in all_domains "
echo "Script is Starting"

curl -s https://dns.bufferover.run/dns?q=.$1 |jq -r .FDNS_A[]|cut -d',' -f2|sort -u>>passive_domains

curl -s "https://crt.sh/?q=$1" |grep "$1"|cut -d 'T' -f 2|cut -d 'D' -f2|cut -d '<' -f1 |cut -d '>' -f2 |sort -u |grep -iv "&" |grep -iv "*" |grep -xv "I"|sort -u|grep  "\S">>passive_domains

curl -s "https://riddler.io/search/exportcsv?q=pld:$1" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u>>passive_domains

curl -s "http://web.archive.org/cdx/search/cdx?url=*.$1/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | sort -u >>passive_domains

curl -s "https://jldc.me/anubis/subdomains/$1" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u >>passive_domains

echo "Filtering"

cat passive_domains |cut -d: -f1|sort -u  >all_domains
rm -rf passive_domains
echo "DONE!!"
