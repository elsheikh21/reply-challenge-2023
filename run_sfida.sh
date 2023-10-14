#!/bin/bash

CNTER=250

while true
do
    ((CNTER++))
    UNZIPME=$(python3 "$(pwd)"/parser_main.py lvl_"${CNTER}".txt)
    echo "[$(date --utc) --- index]: $CNTER"
    echo "[$(date --utc) --- 1 cmd exec]: python3 $(pwd)/parser_main.py lvl_${CNTER}.txt"
    echo "[$(date --utc) --- zip path]: $(pwd)/lvl_$CNTER.zip"
    echo "[$(date --utc) --- passwd ]: $UNZIPME"
    echo "[$(date --utc) --- 2 cmd exec]: 7za x -p$UNZIPME $(pwd)/lvl_$CNTER.zip"
    7za x "$(pwd)"/lvl_"$CNTER".zip -p"$UNZIPME"
    sleep 1s
done
