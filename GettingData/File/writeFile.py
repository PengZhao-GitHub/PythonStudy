#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import csv




with open('colon_delimited_stock_prices.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    with open('targetFile.txt', 'wb') as tf:   #use 'ab' to append records
        writer = csv.writer(tf, delimiter=',')  #how to write a file
        for row in reader:
            date = row['date']
            symbol = row['symbol']
            price = row['price']
            record = [date, symbol, price]
            writer.writerow(record)
            
            
        