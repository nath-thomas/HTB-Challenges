#!/bin/bash

RESULT=0

while [ $RESULT -eq 0 ]
do
        PASSWORD=$( python3 /tmp/M0rsarchive.py )
        ZIPFILE=$( ls *.zip )
        unzip -P "$PASSWORD" "$ZIPFILE"
        RESULT=$?
        echo "Unzipped $ZIPFILE using password $PASSWORD ($RESULT)"
        cd flag
done
