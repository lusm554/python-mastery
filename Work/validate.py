# validate.py

class ValidatedFunction:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Calling', self.func)
    result = self.func(*args, **kwargs)
    return result

class Validator:
  def __init__(self, name=None):
    self.name = name

  def __set_name__(self, cls, name):
    self.name = name

  @classmethod
  def check(cls, value):
    return value

  def __set__(self, instance, value):
    instance.__dict__[self.name] = self.check(value)

class Typed(Validator):
  expected_type = object
  @classmethod
  def check(cls, value):
    if not isinstance(value, cls.expected_type):
      raise TypeError(f'Expected {cls.expected_type}')
    return super().check(value)

class Integer(Typed):
  expected_type = int

class Float(Typed):
  expected_type = float

class String(Typed):
  expected_type = str

class Positive(Validator):
  @classmethod
  def check(cls, value):
    if value < 0:
      raise ValueError('Expected >= 0')
    return super().check(value)

class NonEmpty(Validator):
  @classmethod
  def check(cls, value):  
    if len(value) == 0:
      raise ValueError('Must be non-empty')
    return super().check(value)

class PositiveInteger(Integer, Positive):
  pass

class PositiveFloat(Float, Positive):
  pass

class NonEmptyString(String, NonEmpty):
  pass


if __name__ == '__main__':
  class Stock:
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()
    def __init__(self, name, shares, price):
      self.name = name
      self.shares = shares
      self.price = price

    def __repr__(self):
      return f'Stock(\'{self.name}\', {self.shares}, {self.price})'

    @property
    def cost(self):
      return self.shares * self.price
       
    def sell(self, sellshares):
      self.shares -= sellshares

  s = Stock('GOOG', 100, 490.10)
  print(s.name)
  print(s.shares)
  s.shares = 34
  try:
    s.shares = '134'
  except Exception as e:
    print(e)
  try:
    s.shares = -1
  except Exception as e:
    print(e)
