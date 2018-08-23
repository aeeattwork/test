#!/usr/bin/python3
import re
import string
from collections import Counter

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

def main():
    #file1 = input('Enter file_1 root: ')
    #file2 = input('Enter file_2 root: ')
    #file3 = input('Enter file_3 root: ')
    file1 = "D:\Python\TEST\\avid_python_test\\file_1.txt"
    file2 = "D:\Python\TEST\\avid_python_test\\file_2.txt"
    file3 = "D:\Python\TEST\\avid_python_test\\file_3.txt"
    oc1, pop1 = occurrence(file1)
    oc2, pop2 = occurrence(file2)
    oc3, pop3 = occurrence(file3)
    files = []
    f1 = read_file(file1)
    f2 = read_file(file2)
    f3 = read_file(file3)
    matches = set(f1).intersection(f2, f3)
    unique1 = set(f1).difference(f2,f3)
    unique2 = set(f2).difference(f1,f3)
    unique3 = set(f3).difference(f1,f2)
    print('\n',"The 10 most popular words in file1:",'\n','\n',pop1)
    print('\n',"The 10 most popular words in file2:",'\n','\n',pop2)
    print('\n',"The 10 most popular words in file3:",'\n','\n',pop3)
    print('\n',"Words that can be found in all files:", '\n','\n',matches)
    print('\n',"Words that can only be found in file1:", '\n','\n',unique1)
    print('\n',"Words that can only be found in file2:", '\n','\n',unique2)
    print('\n',"Words that can only be found in file3:", '\n','\n',unique3)

main()
