# stock.py

import csv

class Stock:
  __slots__ = ('name', '_shares', '_price')
  _types = (str, int, float)
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  @classmethod
  def from_row(cls, row):
    values = [cast(val) for cast, val in zip(cls._types, row)]
    return cls(*values)

  @property
  def cost(self):
    return self.shares * self.price

  @property
  def shares(self):
    return self._shares 

  @shares.setter
  def shares(self, value):
    if not isinstance(value, self._types[1]):
      raise TypeError(f'Expected {self._types[1].__name__}')
    if not value >= 0:
      raise TypeError('Expected shares >= 0')
    self._shares = value

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    if not isinstance(value, self._types[2]):
      raise TypeError(f'Expected {self._types[2].__name__}')
    if not value >= 0:
      raise TypeError('Expected price >= 0')
    self._price = value
     
  def sell(self, sellshares):
    self.shares -= sellshares


def read_portfolio(filename, cls):
  records = []
  with open(filename, 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      record = cls.from_row(row) 
      records.append(record) 
  return records

def print_portfolio(data):
  headers = ("name", "shares", "price")
  print('%10s %10s %10s' % headers)
  print("---------- "*len(headers))
  for s in data:
    print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == "__main__":
	import tableformat
	import reader
	portfolio = read_portfolio('Data/portfolio.csv', Stock)
	tableformat.print_table(portfolio, ['name', 'shares', 'price'])
