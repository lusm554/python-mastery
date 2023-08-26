# sample.py

from logcall import logged, logformat

@logged
def add(x,y):
  return x + y

@logged
def sub(x,y):
  return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
  return x * y

if __name__ == '__main__':
  add(1, 2)
  sub(1, 1)
  mul(2, 2)
