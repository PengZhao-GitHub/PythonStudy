'''
Created on Jan 23, 2017

@author: admin
'''

import csv
import dateutil.parser as p

data = []


def try_or_none(f):
    def f_or_none(x):
        try: return f(x)
        except: return None
    return f_or_none


def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else ValueError
            for value, parser in zip(input_row, parsers)]
    

def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)
        

with open("comma_stock_prices.csv", "rb") as f:
    reader = csv.reader(f)
    for line in parse_rows_with(reader, [p.parse, None, float]):  #Key function
        data.append(line)
        
for row in data:
    if any(x is None for x in row):
        print row
        

    


