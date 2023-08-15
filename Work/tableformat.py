# tableformat.py

def print_table(data, headers):
  frmt = '%10s ' * len(headers)
  print(frmt % tuple(headers))
  print("---------- "*len(headers))
  for s in data:
    print(frmt % tuple(getattr(s, attr) for attr in headers))

