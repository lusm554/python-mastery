# sample.py

from logcall import logged, logformat
from validate import Integer, enforce, validated

"""
@logged
def add(x,y):
  return x + y
"""

@enforce(x=Integer, y=Integer, return_=Integer)
def sub(x,y):
  return x - y

@validated
def asub(x: Integer, y: Integer) -> Integer:
  return x - y

"""
@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
  return x * y
"""

if __name__ == '__main__':
  #add(1, 2)
  print(sub(1, 1))
  print(sub(1., 1))
  print(asub('1', '1'))
  #mul(2, 2)
  """
  class Spam:
    @logged
    def instance_method(self):
        pass

    @logged
    @classmethod
    def class_method(cls):
        pass

    @logged
    @staticmethod
    def static_method():
        pass

    @logged
    @property
    def property_method(self):
        pass 
  s = Spam()
  s.instance_method()
  Spam.class_method()
  Spam.static_method()
  print(s.property_method)
  """
