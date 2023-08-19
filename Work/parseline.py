# parseline.py

def parse_line(line: str) -> tuple:
  '''
  Parse line like name=value into tuple.
  '''
  name, val = line.split('=')
  return name, val

if __name__ == '__main__':
  res = parse_line('email=guido@python.org')
  print(res)
