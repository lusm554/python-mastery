# readriders.py

import csv

def as_tuples(route, date, daytype, rides):
  return (route, date, daytype, rides)


class Row:
  def __init__(self, route, date, daytype, rides):
    self.route = route
    self.date = date
    self.daytype = daytype
    self.rides = rides

def as_class(route, date, daytype, rides):
  return Row(route, date, daytype, rides)


from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides']) 

def as_namedtuple(route, date, daytype, rides):
  return Row(route, date, daytype, rides) 


class RowS:
  __slots__ = ['route', 'date', 'daytype', 'rides']
  def __init__(self, route, date, daytype, rides):
    self.route = route
    self.date = date
    self.daytype = daytype
    self.rides = rides

def as_class_slots(route, date, daytype, rides):
  return RowS(route, date, daytype, rides) 

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
  
  def rides_traced_memory(method):
    tracemalloc.start()
    rows = read_rides(method, 'Data/ctabus.csv')
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak
    

  print('Memory Use As Tuples: Current {:,}, Peak {:,}'.format(*rides_traced_memory(as_tuples)))
  print('Memory Use As Class Instance: Current {:,}, Peak {:,}'.format(*rides_traced_memory(as_class)))
  print('Memory Use As Named Tuple: Current {:,}, Peak {:,}'.format(*rides_traced_memory(as_namedtuple)))
  print('Memory Use As Class Slots: Current {:,}, Peak {:,}'.format(*rides_traced_memory(as_class_slots)))
