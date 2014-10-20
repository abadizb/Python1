import os
import sys
import pickle
import quotes
import shelve
def indexer():
    Dict = {}
    pickles = open ("C:\Users\Halim\Python34\raw_data.pickle","br")
    x = pickle.load(r)
    shelve = shelve.open("datalist")
    for x, quote in enumerate(quotes.datalist):
        words = quote.split()
        for word in words:
            if(word not in Dict.keys()):
                Dict[word]={x}
            else:
                Dict[word]= Dict[word]|{x}
    for key, value in Dict.items():
        shelve[key]=(value)
    pickles.close()
    shelve.close()

indexer()
