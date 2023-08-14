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

if __name__ == '__main__':
  port = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
  for s in port:
    print(s)
