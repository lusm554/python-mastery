# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

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
  s = Stock('GOOG',100,490.1)
  print(s)
  try:
    s.sell(-1)
  except TypeError:
    print('except works') 
  s = Stock(name='GOOG',shares=100,price=490.1)
  print(s)
  s = Stock.from_row(['GOOG',100,490.1])
  print(s)
