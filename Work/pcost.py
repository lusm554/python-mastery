# pcost.py

def portfolio_cost(filepath):
  total_shares_cost = 0
  with open(filepath, 'r') as f:
    for line in f:
      row = [x for x in line.split(" ") if x != '']
      try:
        total_shares_cost += int(row[1]) * float(row[2])
      except ValueError as error:
        print(f"Couldn't parse: {repr(line)}")
        print(f"Reason: {error}")
  return total_shares_cost

if __name__ == '__main__':
  print(portfolio_cost('Data/portfolio.dat'))
  print(portfolio_cost('Data/portfolio3.dat'))
  print(portfolio_cost('Data/portfolio2.dat'))
