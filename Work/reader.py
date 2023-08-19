# reader.py

import csv
from typing import List, Callable, Iterable

def csv_as_dicts(lines: Iterable, types: type, headers: list | None = None) -> List[dict]:
  '''
  Convert data to list of dicts
  '''
  records = []
  lines = csv.reader(lines)
  headers = next(lines) if not headers else headers
  for line in lines:
    record = { name: cast(val) for name, val, cast in zip(headers, line, types) }
    records.append(record)
  return records

def csv_as_instances(lines: Iterable, cls: type, headers: list | None = None) -> List[type]:
  '''
  Convert data to list of instances
  '''
  records = []
  lines = csv.reader(lines)
  headers = next(lines) if not headers else headers
  for line in lines:
    record = cls.from_row(line)
    records.append(record)
  return records

def read_csv_as_dicts(filename: str, types: List[Callable]) -> List[dict]:
  '''
  Read CSV data into a list of dictionaries with optional type conversion
  '''
  with open(filename) as file:
    records = csv_as_dicts(file, [str, int, float])
  return records


def read_csv_as_instances(filename: str, cls: type) -> List[type]:
  '''
  Read CSV data into a list of instances
  '''
  with open(filename) as file:
    records = csv_as_instances(file, cls)
  return records


if __name__ == '__main__':
  from stock import Stock
  from pprint import pprint
  p = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
  pprint(p) 

  p = read_csv_as_instances('Data/portfolio.csv', Stock)
  pprint(p)
