from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from six import StringIO
import json
import pandas

transactions = []

def readFile():
    f = open("ransomware/ransomwareTxs/7ev3n/1Lud76Q98VRHCUiyK7XUs7AgFofrqXeP78_txs.json")
    line = f.readline()
    print(f.name.split('_txs.json')[0])

    while line:
        jsonData = json.loads(line)
        transactions.append(jsonData)

        line = f.readline()

    f.close()



def buildCsv(transaction):
    nin = []
    nout = []
    
    nin.append(transaction['n_in'])
    nout.append(transaction['n_out'])

    df = pandas.DataFrame({'nin':nin,'nout':nout})
    df.to_csv('')


readFile()
for i in range(len(transactions)):
    buildCsv(transactions[i])