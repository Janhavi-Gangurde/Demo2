#!/bin/bash

fibonacci_series() {
    local terms=$1
    local a=0
    local b=1

    if [ $terms -ge 1 ]; then
        echo -n "$a "
    fi

    if [ $terms -ge 2 ]; then
        echo -n "$b "
    fi

    for ((i=2; i<terms; i++)); do
        local next=$((a + b))
        echo -n "$next "
        a=$b
        b=$next
    done

    echo
}

read -p "Enter the number of terms in the Fibonacci series: " num_terms


fibonacci_series $num_terms

