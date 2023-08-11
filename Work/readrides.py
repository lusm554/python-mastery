# readriders.py

import csv

def read_rides_as_tuples(filename):
  record_structure = lambda route, date, daytype, rides: (route, date, daytype, rides)
  return read_rides(record_structure, filename) 

def read_rides_as_dicts(filename):
  record_structure = lambda route, date, daytype, rides: {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides
  }
  return read_rides(record_structure, filename) 

class Row:
  def __init__(self, route, date, daytype, rides):
    self.route = route
    self.date = date
    self.daytype = daytype
    self.rides = rides

def read_rides_as_classes(filename):
  record_structure = lambda route, date, daytype, rides: Row(route, date, daytype, rides)
  return read_rides(record_structure, filename) 

from collections import namedtuple
RowNamedT = namedtuple('Row', ['route', 'date', 'daytype', 'rides']) 

def read_rides_as_namedtuples(filename):
  record_structure = lambda route, date, daytype, rides: RowNamedT(route, date, daytype, rides)
  return read_rides(record_structure, filename) 

class RowSlot:
  __slots__ = ['route', 'date', 'daytype', 'rides']
  def __init__(self, route, date, daytype, rides):
    self.route = route
    self.date = date
    self.daytype = daytype
    self.rides = rides

  def __repr__(self):
    return f"{type(self).__name__}('{self.route}', {self.date}, {self.daytype}, {self.rides})"

def read_rides_as_rowslots(filename):
  record_structure = lambda route, date, daytype, rides: RowSlot(route, date, daytype, rides)
  return read_rides(record_structure, filename) 

def read_rides(data_structure, filename):
  records = []
  with open(filename) as f:
    rows = csv.reader(f)
    headings = next(rows)
    for row in rows:
      route, date, daytype, rides = row[0], row[1], row[2], int(row[3])
      record = data_structure(route, date, daytype, rides)
      records.append(record)
  return records

if __name__ == '__main__':
  import tracemalloc
  
  def rides_traced_memory(read_function):
    tracemalloc.start()
    rows = read_function('Data/ctabus.csv')
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

  print('Memory Use As Tuples: Current {:,}, Peak {:,}'.format(*rides_traced_memory(read_rides_as_tuples)))
  print('Memory Use As Dicts: Current {:,}, Peak {:,}'.format(*rides_traced_memory(read_rides_as_dicts)))
  print('Memory Use As Class Instance: Current {:,}, Peak {:,}'.format(*rides_traced_memory(read_rides_as_classes)))
  print('Memory Use As Named Tuple: Current {:,}, Peak {:,}'.format(*rides_traced_memory(read_rides_as_namedtuples)))
  print('Memory Use As Class Slots: Current {:,}, Peak {:,}'.format(*rides_traced_memory(read_rides_as_rowslots)))
