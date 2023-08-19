# stock.py

import csv
from typedproperty import String, Integer, Float


class Stock:
  name = String()
  shares = Integer()
  price = Float()

  #__slots__ = ('name', '_shares', '_price') # slots!
  _types = (str, int, float)
  def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

  def __repr__(self):
    return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

  def __eq__(self, other):
    return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                         (other.name, self.shares, other.price))

  @classmethod
  def from_row(cls, row):
    ''' Alt constructor '''
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
    if not isinstance(value, self._types[1]): # here we using type checking by _types class variable
      raise TypeError(f'Expected {self._types[1].__name__}')
    if not value >= 0:
      raise TypeError('Expected shares >= 0')
    self._shares = value

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    if not isinstance(value, self._types[2]): # here we using type checking by _types class variable
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

class redirect_stdout:
  def __init__(self, out_file):
    self.out_file = out_file

  def __enter__(self):
    self.stdout = sys.stdout
    sys.stdout = self.out_file

  def __exit__(self, ty, val, tb):
    sys.stdout = self.stdout

if __name__ == "__main__":
  s = Stock('test', 1, .04)
  print(s)
  exit()

  import tableformat
  import reader
  import sys
  portfolio = read_portfolio('Data/portfolio.csv', Stock)
  with redirect_stdout(open('out.txt', 'w')) as file:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], tableformat.create_formatter('text'))
