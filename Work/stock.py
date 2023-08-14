# stock.py

import csv

class Stock:
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def cost(self):
    return self.shares * self.price
  
  def sell(self, sellshares):
    self.shares -= sellshares
  

def read_portfolio(filename):
  records = []
  with open(filename, 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      record = Stock(row[0], int(row[1]), float(row[2]))
      records.append(record) 
  return records

if __name__ == "__main__":
  from pprint import pprint
  portfolio = read_portfolio('Data/portfolio.csv')
  pprint(portfolio[:10])
