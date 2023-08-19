# typedproperty.py

def typedproperty(name, expected_type):
  private_name = '_' + name

  @property
  def value(self):
    return getattr(self, private_name)

  @value.setter
  def value(self, val):
    if not isinstance(val, expected_type):
      raise TypeError(f'Expected {expected_type}')
    setattr(self, private_name, val) 

  return value

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
