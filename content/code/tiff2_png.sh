#!/bin/bash
for filename in *.tif
do
    echo "Converting $filename"
    convert "$filename" "$(basename "$filename" .tif).png"
done
