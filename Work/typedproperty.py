# typedproperty.py

def typedproperty(expected_type):
  class Type:
    @property
    def value(self):
      return getattr(self, self.name)

    @value.setter
    def value(self, val):
      if not isinstance(val, expected_type):
        raise TypeError(f'Expected {expected_type}')
      setattr(self, self.name, val) 

    def __set_name__(self, cls, name):
      self.name = name

  return Type

String = lambda: typedproperty(str)
Integer = lambda: typedproperty(int)
Float = lambda: typedproperty(float)
