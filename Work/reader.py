# reader.py

import csv

def read_csv_as_dicts(filename, types):
  '''
  Read CSV data into a list of dictionaries with optional type conversion
  '''
  records = []
  with open(filename) as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
      record = { name: cast(val) for name, val, cast in zip(headers, row, types) }
      records.append(record)
  return records

def read_csv_as_instances(filename, cls):
  '''
  Read CSV data into a list of instances
  '''
  records = []
  with open(filename) as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
      record = cls.from_row(row)
      records.append(record)
  return records

if __name__ == '__main__':
  from stock import Stock
  from pprint import pprint
  p = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
  pprint(p) 

  p = read_csv_as_instances('Data/portfolio.csv', Stock)
  pprint(p)
