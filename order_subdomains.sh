#!/bin/bash



cat $1|tr -d [:blank:]|perl -lne 'print join ".", reverse(split /\./)'|sort |awk -F. ' !seen[$1.$2.$3]++ && NR>1 {print ""} {for (i=NF;i>1;i--) printf "%s.", $i; print $1}'|xargs -n 1
