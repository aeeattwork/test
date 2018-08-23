#!/usr/bin/python3
import os
import re
import sys
import string

def read_file(file):
    words = []
    with open(file,'r') as f:
        for line in f:
            #for word in re.split(r"--\s|\n",line):
            for word in line.split():
                word = word.strip(string.punctuation)
                words.append(word)
    return words

def occurrence(file):
    output = read_file(file)
    number_of_occurrence = Counter(output)
    most_popular = Counter(output).most_common(10)
    return (number_of_occurrence, most_popular)
