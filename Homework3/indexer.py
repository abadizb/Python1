import os
import sys
import pickle
import quotes
def indexer():
    Dict = {}
    for i, quote in enumerate(quotes.datalist):
        words = quote.split()
        for word in words:
            if(word not in Dict.keys()):
                Dict[word]={i}
            else:
                Dict[word]= Dict[word]|{i}

indexer()
