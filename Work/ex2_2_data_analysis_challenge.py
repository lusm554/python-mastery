# ex2_2_data_analysis_challenge.py

import readrides

def how_many_bus_routes_exist(rows):
  routes = {row.route for row in rows}
  return len(routes) 

if __name__ == "__main__":
  rows = readrides.read_rides_as_rowslots('Data/ctabus.csv') 
  # How many bus routes exist in Chicago?
  bus_routes_cnt = how_many_bus_routes_exist(rows)
  print("How many bus routes exist in Chicago? Answer: %d." % bus_routes_cnt)
  
