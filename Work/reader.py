# reader.py

import csv

def read_csv_as_dicts(filename, types):
  records = []
  with open(filename, 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      records.append({ key: cast(val) for key, val, cast in zip(headers, row, types) })
  return records

def read_csv_as_instances(filename, cls):
  '''
  Read a CSV file into a list of instances
  '''
  records = []
  with open(filename, 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      record = cls.from_row(row)
      records.append(record)
  return records

if __name__ == '__main__':
  from stock import Stock
  from pprint import pprint
  port = read_csv_as_instances('Data/portfolio.csv', Stock)
  pprint(port[:5])
