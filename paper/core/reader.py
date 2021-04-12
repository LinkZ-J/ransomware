#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from six import StringIO
import json
import pandas as pd
import os
from prettytable import PrettyTable


# In[2]:


def read_csv_to_list(path):
    messages = []
    for root,dirs,files in os.walk(path):
        for dir in dirs:
            for r,ds,fs in os.walk(dir):
                for f in fs:
                    readFile(messages, r, f)
        for file in files:
            readFile(messages, root, file)
    return messages


# In[3]:


def getAddrName(str):
    return str.split('_txs.json')[0]


# In[4]:


def readFile(messages, rootName, fileName):
    addrName = getAddrName(fileName)
    f = open(os.path.join(rootName, fileName))
    
    line = f.readline()
    while line:
        transaction_json = json.loads(line)
        messages.append(transaction_json)
        line = f.readline()

    f.close()

