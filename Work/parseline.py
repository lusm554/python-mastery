# parseline.py

def parse_line(line: str) -> tuple:
  '''
  Parse line like name=value into tuple.
  '''
  try:
    name, val = line.split('=')
  except ValueError:
    # Design discussion: Would it be better for the parse_line() function to raise an exception on malformed data?
    # Yes. I think better raise exception when data incorrect. 
    return None
  return name, val

if __name__ == '__main__':
  res = parse_line('email=guido@python.org')
  print(res)
  res = parse_line('spam')
  print(res)
