# -*- coding: utf-8 -*-
"""preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kmYmretZeZx4Jlqqt-dpp-WpBqpMBI_Z
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
import nltk
import string

!pip install wordcloud

df = pd.read_csv('train-v2.tsv', sep='\t',header= None)

df.columns = ['class','tweet']
df

df['tweet'] = df['tweet'].str.replace('@USER','')

df.head()

df['tweet'] = df['tweet'].str.replace("[^a-zA-z#]", " ")
df.head()

total_string = " ".join([string for string in df['tweet']])
total_string

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
toke = word_tokenize(total_string)

import collections
count = collections.Counter(toke)

import collections
sorted_count = sorted(count.items(), key=lambda kv: kv[1], reverse= True)
sorted_dict = collections.OrderedDict(sorted_count)
print(sorted_dict)

from wordcloud import WordCloud
wc =WordCloud(width= 600, height=400, random_state=10, max_font_size=75).generate(total_string)

plt.figure(figsize=(14,7))
plt.imshow(wc,interpolation='bilinear' )
plt.axis('off')
plt.show()

