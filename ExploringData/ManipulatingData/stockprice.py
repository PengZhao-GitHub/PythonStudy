'''
Created on Jan 23, 2017

@author: admin
'''

import datetime
from _collections import defaultdict


data = [
    
    {'price' : 102.86,
     'date': datetime.datetime(2014,8,29,0,0),
     'symbol' : 'APPL'},
        
    {'price': 90.7,
     'date': datetime.datetime(2014,8,29,0,0),
     'symbol': 'MS'},
    
    {'price': 16,
     'date': datetime.datetime(2014,8,29,0,0),
     'symbol': 'Facebook'},
        
     {'price': 92.86,
     'date': datetime.datetime(2014,8,28,0,0),
     'symbol': 'APPL'},
        
    {'price': 40.7,
     'date': datetime.datetime(2014,8,28,0,0),
     'symbol': 'MS'},
    
    {'price': 80,
     'date': datetime.datetime(2014,8,28,0,0),
     'symbol': 'Facebook'},
    
    {'price': 72.86,
     'date': datetime.datetime(2014,8,27,0,0),
     'symbol': 'APPL'},
        
    {'price': 88.7,
     'date': datetime.datetime(2014,8,27,0,0),
     'symbol': 'MS'},
    
    {'price': 100,
     'date': datetime.datetime(2014,8,27,0,0),
     'symbol': 'Facebook'},
    
]

# single stock
max_appl_price = max(row["price"]
                     for row in data
                     if row["symbol"] == "APPL")

if max_appl_price != None:
    print max_appl_price


# Multiple stocks
by_symbol = defaultdict(list)

for row in data:
    by_symbol[row["symbol"]].append(row)
    
print by_symbol

max_price_by_symbol = { symbol : max(row["price"]
                                     for row in grouped_rows)
                       for symbol, grouped_rows in by_symbol.iteritems()}

print max_price_by_symbol


#Define a set of funcitons 

def picker(field_name):
    return lambda row: row[field_name]  #return a function that picks a field out of a dict

def pluck(field_name, rows):
    return map(picker(field_name), rows)

def group_by(grouper, rows, value_transform=None):
    grouped = defaultdict(list)
    for row in rows:
        grouped[grouper(row)].append(row)
    
    if value_transform is None:
        return grouped
    else:
        return {key : value_transform(rows)
                for key, rows in grouped.iteritems()}
        
        
max_price_by_symbol_v2 = group_by(picker("symbol"),
                               data,
                               lambda rows: max(pluck("price",rows)))

print max_price_by_symbol_v2

def percent_price_change(yesterday, today):
    return today["price"] / yesterday["price"] - 1

def day_over_day_changes(grouped_rows):
    ordered = sorted(grouped_rows, key=picker("date"))
    
    print ordered 
    
    return [{ "symbol" : today["symbol"],
              "date" : today["date"],
              "change" : percent_price_change(yesterday, today)}
            for yesterday, today in zip(ordered, ordered[1:])]

changes_by_symbol = group_by(picker("symbol"), data, day_over_day_changes)

print changes_by_symbol

all_changes = [change 
               for changes in changes_by_symbol.values()
               for change in changes ]

print "----------------------------"

print all_changes

print max(all_changes, key=picker("change"))
print min(all_changes, key=picker("change"))


def combine_pct_chanages(pct_change1, pct_change2):
    return (1 + pct_change1) * (1 + pct_change2) - 1

def overall_change(changes):
    return reduce(combine_pct_chanages, pluck("change", changes))

overall_change_by_month = group_by(lambda row: row["date"].month,
                                   all_changes,
                                   overall_change)

print 
print overall_change_by_month

