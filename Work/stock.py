# stock.py

from structly import *

class Stock(Structure):
  name = String()
  shares = PositiveInteger()
  price = PositiveFloat()

  @property
  def cost(self):
    return self.price * self.shares

  def sell(self, nshares: PositiveInteger):
    self.shares -= nshares

if __name__ == '__main__':
  from structly.reader import read_csv_as_instances
  from structly.tableformat import create_formatter, print_table
  portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
  formatter = create_formatter('text')
  print_table(portfolio, ['name', 'shares', 'price'], formatter)
