# cotiker.py

from structure import Structure

class Ticker(Structure):
  name = String()
  price = Float()
  date = String()
  time = String()
  change = Float()
  open = Float()
  high = Float()
  low = Float()
  volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv

@consumer
def to_csv(target):
  '''
  Send line in csv format
  '''
  def producer():
    while True:
      yield line

  reader = csv.reader(producer())
  while True:
    line = yield
    target.send(next(reader))

@consumer
def create_ticker(target):
  '''
  Creates from row Ticker instance
  '''
  while True:
    row = yield
    target.send(Ticker.from_row(row))

@consumer
def negchange(target):
  '''
  Filter Ticker instance for negative change
  '''
  while True:
    record = yield
    if record.change < 0:
      target.send(record)

@consumer
def ticker(fmt, fields):
  '''
  Prints in format Ticker instance
  '''
  formatter = create_formatter(fmt)
  formatter.headings(fields)
  while True:
    rec = yield
    row = [getattr(rec, name) for name in fields]
    formatter.row(row)

if __name__ == '__main__':
  target = to_csv(create_ticker(negchange(ticker('text', ['name', 'price', 'change']))))
  follow('Data/stocklog.csv', target)
