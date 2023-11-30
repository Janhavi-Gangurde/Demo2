#!/bin/bash

# Define a function to reverse a string
reverse_string() {
    local input_string=$1
    local length=${#input_string}
    local reversed_string=""

    for ((i=length-1; i>=0; i--)); do
        reversed_string="${reversed_string}${input_string:i:1}"
    done

    echo "$reversed_string"
}

# Read input from the user
read -p "Enter a string: " input_string

# Call the reverse_string function and store the result
reversed_result=$(reverse_string "$input_string")

# Display the result
echo "Reversed string: $reversed_result"

