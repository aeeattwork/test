#!/usr/bin/python3
import re
import string
from collections import Counter

def read_txt(file):
    words = []
    with open(file,'r') as f:
        for line in f:
            for word in re.split(r"--|\s|\n",line):
                word = word.strip(string.punctuation).lower()
                words.append(word)
    words = list(filter(None, words))
    return words

def read_docx(file):
    try:
        from docx import Document
    except:
        print("Cannot import module")
        exit()
    words = []
    doc = Document(file)
    for p in doc.paragraphs:
        line = p.text
        for word in re.split(r"--|\s|\n",line):
            word = word.strip(string.punctuation).lower()
            words.append(word)
    words = list(filter(None, words))
    return words

def occurrence(read):
    number_of_occurrence = Counter(read)
    most_popular = Counter(read).most_common(10)
    return (number_of_occurrence, most_popular)

def inter_and_diff(read_files):
    matches = list(set.intersection(*map(set, read_files)))
    unique_values = []
    ln = len(read_files)
    n = 0
    for file in read_files:
        read_files.remove(file)
        n += 1
        unique = list(set(file).difference(*map(set, read_files)))
        unique = sorted(unique)
        unique_values.append(unique)
        read_files.insert(0,file)
    return (matches,unique_values)

def input_files():
    file1 = input('Enter file_1 path: ')
    while not file1.lower().endswith(('.docx','.txt')):
        print('Please provide file with one of the following extensions: .docx, .txt')
        file1 = input('Enter file_1 path: ')
    file2 = input('Enter file_2 path: ')
    while not file2.lower().endswith(('.docx','.txt')):
        print('Please provide file with one of the following extensions: .docx, .txt')
        file2 = input('Enter file_2 path: ')
    file3 = input('Enter file_3 path: ')
    while not file3.lower().endswith(('.docx','.txt')):
        print('Please provide file with one of the following extensions: .docx, .txt')
        file3 = input('Enter file_3 path: ')
    files = [file1,file2,file3]
    return (files)

def controller():
    files = input_files()
    all_files = []
    for f in files:
        if f.lower().endswith('.docx'):
            file = read_docx(f)
            all_files.append(file)
        elif f.lower().endswith('.txt'):
            file = read_txt(f)
            all_files.append(file)
    occ = []
    popu = []
    for file in all_files:
        oc, pop = occurrence(file)
        occ.append(oc)
        popu.append(pop)

    matches,unique_values = inter_and_diff(all_files)
    matches = sorted(matches)
    return (popu,matches,unique_values) 

def output():
    popu,matches,unique_values = controller()
    number = 0
    for pop in popu:
        number += 1
        print('\n',"The 10 most popular words in file%s:"%number,'\n','\n',pop)

    print('\n',"Words that can be found in all files:", '\n','\n',matches)

    number = 0
    for u in unique_values:
        number += 1
        print('\n',"Words that can only be found in file%s:"%number, '\n','\n',u)

output()
