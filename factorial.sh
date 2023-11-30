#!/bin/bash

# Define a function to calculate factorial
calculate_factorial() {
    local num=$1
    local result=1

    if [ $num -eq 0 ]; then
        echo 1
    else
        for ((i = 1; i <= $num; i++)); do
            result=$((result * i))
        done
        echo $result
    fi
}

read -p "Enter a number: " number

factorial=$(calculate_factorial $number)

echo "Factorial of $number is $factorial"
