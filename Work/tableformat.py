# tableformat.py

def print_table(data, headers):
  frmt = '%10s ' * len(headers)
  print(frmt % tuple(headers))
  print("---------- "*len(headers))
  for s in data:
    print(frmt % tuple(getattr(s, attr) for attr in headers))

if __name__ == '__main__':
  import stock
  portfolio = stock.read_portfolio('Data/portfolio.csv')
  print_table(portfolio, ['name','shares','price'])
  print()
  print_table(portfolio,['shares','name'])
  print()
  print_table(portfolio,['name'])
