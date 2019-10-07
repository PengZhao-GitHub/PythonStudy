#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import csv

with open('tab_delimited_stock_price.txt','rb') as f:
    reader = csv.reader(f, delimiter = "\t")
    for row in reader:
        date = row[0]
        symbol = row[1]
        price = float(row[2])
        print date , symbol, price
        
        