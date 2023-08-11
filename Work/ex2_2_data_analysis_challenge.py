# ex2_2_data_analysis_challenge.py

import readrides
from collections import Counter, defaultdict
from pprint import pprint

def how_many_bus_routes_exist(rows):
  routes = {row.route for row in rows}
  return len(routes) 

def how_many_riders_by_route_day(route_num, date, rows):
  return sum(row.rides for row in rows if row.route == route_num and row.date == date) 

def total_num_rides_by_route(rows):
  totals = Counter()
  for row in rows:
    totals[row.route] += row.rides
  return totals

def top_5_routes(rows):
  rides_by_year = defaultdict(Counter)
  for row in rows:
    rowyr = row.date.split("/")[2]
    rides_by_year[rowyr][row.route] += row.rides
  diffs = rides_by_year['2011'] - rides_by_year['2001']
  return diffs.most_common(5)

if __name__ == "__main__":
  rows = readrides.read_rides_as_rowslots('Data/ctabus.csv') 
  # How many bus routes exist in Chicago?
  bus_routes_cnt = how_many_bus_routes_exist(rows)
  print("How many bus routes exist in Chicago? Answer: %d." % bus_routes_cnt)
  
  # How many people rode the number 22 bus on February 2, 2011?
  rides_on_22route_2_2_2011 = how_many_riders_by_route_day('22', '02/02/2011', rows)
  print("How many people rode the number 22 bus on February 2, 2011? Answer: %d." % rides_on_22route_2_2_2011)
  
  # What is the total number of rides taken on each bus route?
  total_num_by_routes = total_num_rides_by_route(rows)
  print("What is the total number of rides taken on each bus route?")
  for route, count in total_num_by_routes.most_common():
    print("%5s %10d" % (route, count))

  # What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
  top5 = top_5_routes(rows)
  print("What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?")
  for route, count in top5:
    print("%5s %10d" % (route, count))
