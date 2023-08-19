# teststock.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
  def test_create(self):
    s = Stock('GOOG', 100, 490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

  def test_create_from_kw(self):
    s = Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

  def test_cost(self):
    s = Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.cost, 100*490.1)

  def test_sell(self):
    s = Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.shares, 100)
    s.sell(46)
    self.assertEqual(s.shares, 100-46)

  def test_from_row(self):
    row = ('GOOG', 100, 490.1)
    s = Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

  def test_repr(self):
    s = Stock(name='GOOG', shares=100, price=490.1)
    shouldbe = 'Stock(\'GOOG\', 100, 490.1)'
    self.assertEqual(repr(s), shouldbe)

  def test_eq(self):
    s = Stock(name='GOOG', shares=100, price=490.1)
    s2 = Stock(name='GOOG', shares=100, price=490.1)
    s3 = Stock(name='YNDX', shares=56, price=50.3)
    self.assertEqual(s, s2)
    self.assertNotEqual(s, s3)


if __name__ == '__main__':
  unittest.main()
