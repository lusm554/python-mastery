# colreader.py

import csv
from collections import abc, defaultdict

class DataCollection(abc.Sequence):
  def __init__(self, columns):
    self.column_names = list(columns)
    self.column_data = list(columns.values())

  def __len__(self):
    return len(self.column_data[0])

  def __getitem__(self, index):
    if isinstance(index, slice):
      return [dict(zip(self.column_names, col)) for col in zip(*[col[index] for col in self.column_data])]
    return dict(zip(self.column_names, (col[index] for col in self.column_data)))

def read_csv_as_columns(filename, types):
  records = defaultdict(list)
  with open(filename, 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      for key, val, cast in zip(headers, row, types):
        records[key].append(cast(val))
  return DataCollection(records)


if __name__ == '__main__':
  import tracemalloc
  from sys import intern
  tracemalloc.start()
  data = read_csv_as_columns('Data/ctabus.csv', [intern, intern, intern, int])
  print('Memory use: Current {:,}, Peak {:,}'.format(*tracemalloc.get_traced_memory()))
  # Without intern: Memory use: Current 96,170,191, Peak 96,200,208
  # With intern: Memory use: Current 34,775,821, Peak 34,805,948
  # About 3X TIMES!
