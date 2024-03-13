#!/bin/bash

# Usage: ./script.sh headers.txt sequences.txt

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 headers_file sequences_file"
    exit 1
fi

# Read the files
headers_file=$1
sequences_file=$2

# Check if files exist
if [ ! -f "$headers_file" ]; then
    echo "$headers_file not found."
    exit 1
fi

if [ ! -f "$sequences_file" ]; then
    echo "$sequences_file not found."
    exit 1
fi

# Read files line by line in tandem
paste -d'\n' <(sed 's/^/>/' "$headers_file") "$sequences_file"
