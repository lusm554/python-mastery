# reader.py

import csv
from typing import List, Callable, Iterable
import logging
log = logging.getLogger(__name__)

def convert_csv(lines, converter, *, headers=None) -> List:
  '''
  Convert data to list of converter objects
  '''
  records = []
  lines = csv.reader(lines)
  headers = next(lines) if not headers else headers
  for rowno, line in enumerate(lines, start=1):
    try:
      records.append(converter(line, headers))
    except ValueError as error:
      log.warning("Row %d: Bad row: %s" % (rowno, line))
      log.debug("Row %d: Reason: %s" % (rowno, error))
      
  return records

def csv_as_dicts(lines: Iterable, types: type, *, headers: list | None = None) -> List[dict]:
  '''
  Convert data to list of dicts
  '''
  converter = lambda line, headers: { name: cast(val) for name, val, cast in zip(headers, line, types) }
  return convert_csv(lines, converter, headers=headers)

def csv_as_instances(lines: Iterable, cls: type, *, headers: list | None = None) -> List[type]:
  '''
  Convert data to list of instances
  '''
  converter = lambda line, headers: cls.from_row(line)
  return convert_csv(lines, converter, headers=headers)

def read_csv_as_dicts(filename: str, types: List[Callable], *, headers=None) -> List[dict]:
  '''
  Read CSV data into a list of dictionaries with optional type conversion
  '''
  with open(filename) as file:
    records = csv_as_dicts(file, [str, int, float], headers=headers)
  return records

def read_csv_as_instances(filename: str, cls: type, *, headers=None) -> List[type]:
  '''
  Read CSV data into a list of instances
  '''
  with open(filename) as file:
    records = csv_as_instances(file, cls, headers=headers)
  return records


if __name__ == '__main__':
  from stock import Stock
  from pprint import pprint
  p = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
  pprint(p) 

  p = read_csv_as_instances('Data/portfolio.csv', Stock)
  pprint(p)

  port = read_csv_as_dicts('Data/missing.csv', types=[str, int, float])
  print(len(port))
