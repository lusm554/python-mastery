# stock.py

from structure import Structure

class Stock(Structure):
  _fields = ('name','shares','price')

if __name__ == '__main__':
  s = Stock('GOOG',100,490.1)
  print(s)

