# ex2_2_data_analysis_challenge.py

import readrides

def how_many_bus_routes_exist(rows):
  routes = {row.route for row in rows}
  return len(routes) 

def how_many_riders_by_route_day(route_num, date, rows):
  return sum(row.rides for row in rows if row.route == route_num and row.date == date) 

if __name__ == "__main__":
  rows = readrides.read_rides_as_rowslots('Data/ctabus.csv') 
  # How many bus routes exist in Chicago?
  bus_routes_cnt = how_many_bus_routes_exist(rows)
  print("How many bus routes exist in Chicago? Answer: %d." % bus_routes_cnt)
  
  # How many people rode the number 22 bus on February 2, 2011?
  rides_on_22route_2_2_2011 = how_many_riders_by_route_day('22', '02/02/2011', rows)
  print("How many people rode the number 22 bus on February 2, 2011? Answer: %d." % rides_on_22route_2_2_2011)

