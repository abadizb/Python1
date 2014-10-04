import os
import fnmatch
import pickle
import quotes
from quotes import datalist
from datetime import datetime
def searcher():
    query=input("Enter:")
    query = query.split()
    query = set(query)
    query = list(query)
    dt1 = datetime.now()
    if "or" in (query) and "and" not in (query):
        query.remove("or")
        print (query)
        for quote in (quotes.datalist):
            for (word) in (query):
                found_at = quote.find(word)
                if( found_at > 0):
                    print(quote)
                    dt2= datetime.now()
                    print("Execution time:", dt2.microsecond-dt1.microsecond)
    elif "and" in (query):
        query.remove("and")
        if "or" in (query):
            query.remove("or")
        print (query)
        for quote in (quotes.datalist):
            if query[0] in quote and query[1] in quote:
                print(quote)
                dt2= datetime.now()
                print("Execution time:", dt2.microsecond-dt1.microsecond)
    else:
        print (query)
        for quote in (quotes.datalist):
            if query[0] in quote and query[1] in quote:
                print(quote)
                dt2= datetime.now()
                print("Execution time:", dt2.microsecond-dt1.microsecond)

searcher()
        
