# reader.py

import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
  def parse(self, filename):
    records = []
    with open(filename) as f:
      rows = csv.reader(f)
      headers = next(rows)
      for row in rows:
        record = self.make_record(headers, row)
        records.append(record)
    return records

  @abstractmethod
  def make_record(self, headers, row):
    raise NotImplemented()

class DictCSVParser(CSVParser):
  def __init__(self, types):
    self.types = types

  def make_record(self, headers, row):
    return { name: cast(val) for name, val, cast in zip(headers, row, self.types) }

class InstanceCSVParser(CSVParser):
  def __init__(self, cls):
    self.cls = cls

  def make_record(self, headers, row):
    return self.cls.from_row(row)

def read_csv_as_dicts(filename, types):
  return DictCSVParser(types).parse(filename)

def read_csv_as_instances(filename, cls):
  '''
  Read a CSV file into a list of instances
  '''
  return InstanceCSVParser(cls).parse(filename)

if __name__ == '__main__':
  from stock import Stock
  from pprint import pprint
  port = read_csv_as_instances('Data/portfolio.csv', Stock)
  pprint(port[:5])
  port = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
  pprint(port[:5])
