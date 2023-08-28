# follow.py

import os
import time

def follow(filename):
  f = open(filename)
  f.seek(0, os.SEEK_END) # move file pointer 0 byes from end of file

  while True:
    line = f.readline()
    if line == '':
      time.sleep(0.1) # sleep briefly and retry
      continue
    yield line

if __name__ == '__main__':
  for line in follow('Data/stocklog.csv'):
    fields = line.split(',')
    name, price, change = fields[0].strip('"'), float(fields[1]), float(fields[4])
    if change < 0:
      print('%10s %10.2f %10.2f' % (name, price, change))

