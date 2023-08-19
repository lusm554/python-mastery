# teststock.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
  def test_create(self):
    s = Stock('GOOG', 100, 490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)


if __name__ == '__main__':
  unittest.main()
