#!/bin/bash

# Define the file names
header_file="headers.txt"
sequence_file="sequences.fasta"

# Check if both files exist
if [[ -f "$header_file" ]] && [[ -f "$sequence_file" ]]; then
    # Read the headers file line by line
    while IFS= read -r header; do
        # Print the header
        echo "$header"
        
        # Read the sequences file line by line
        while IFS= read -r sequence; do
            # If the line starts with '>', it's a new sequence header
            # So we break out of the loop to read the next header from the headers file
            if [[ "$sequence" == ">"* ]]; then
                break
            fi
            
            # Print the sequence
            echo "$sequence"
        done <"$sequence_file"
    done <"$header_file"
else
    echo "One or both files do not exist."
fi
