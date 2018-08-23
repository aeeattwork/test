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
