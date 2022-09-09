#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os 
import sys
from pathlib import Path 


# get father path
root_path = Path(__file__).resolve().parents[0]

def open_text(file_name):
    """
        input: single file name
        output: 1. corpora text list
                2. corpora labels 
    """
    with open(os.path.join(root_path, "data", file_name), "r") as f:
        temp_data = f.readlines()
    corpora = []
    labels = []
    for line in temp_data:
        label, text = line.split("\t")
        labels.append(int(label)) 
        corpora.append(text.strip("\n"))
    return corpora, labels

def remove_punc(text):
    return text.translate(str.maketrans('', '', string.punctuation.replace("@","")))

def tokenize(text, delimiter = " "):
    return text.split(" ")

def remove_stopwords(word_list, stopwords_list  = ["@user"]):
    word_list = [w.lower() for w in word_list if not w.lower() in stopwords_list] 
    return word_list

def process_corpora(corpora_list): 
    processed_text = []
    global_word_list = []
    for text in corpora_list: 
        text = remove_punc(text)
        word_list = tokenize(text)
        word_list = remove_stopwords(word_list)
        if "" in word_list:
            word_list.remove("")
        processed_text.append(word_list)
        global_word_list += word_list
    return processed_text, global_word_list


