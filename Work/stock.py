# stock.py

from structure import Structure

class Stock(Structure):
  def __init__(self, name, shares, price):
    self._init()

  @property
  def cost(self):
    return self.price * self.shares

  def sell(self, nshares):
    self.shares -= nshares

Stock.set_fields()
  
if __name__ == '__main__':
  s = Stock('GOOG',100,490.1)
  print(s)
  s = Stock(name='GOOG',shares=100,price=490.1)
  print(s)

