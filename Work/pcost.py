# pcost.py

import csv

total_shares_cost = 0
with open('Data/portfolio.dat', 'r') as f:
  rows = csv.reader(f, delimiter=' ')
  for row in rows:
    total_shares_cost += int(row[1]) * float(row[2])

print("Total cost of shares in portoflio: %s" % total_shares_cost)
