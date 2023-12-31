# validate.py

import inspect
from functools import wraps

class ValidatedFunction:
  def __init__(self, func):
    self.func = func
    self.annotations = func.__annotations__
    self.signature = inspect.signature(func)

  def __call__(self, *args, **kwargs):
    bound = self.signature.bind(*args, **kwargs)
    for name, val in self.annotations.items():
      val.check(bound.arguments[name])
    result = self.func(*args, **kwargs)
    return result

def enforce(**enforceanns):
  def validated(func):
    if enforceanns:
      if 'return_' in enforceanns:
        enforceanns['return'] = enforceanns.pop('return_', None)
      annotations = enforceanns
    else:
      annotations = func.__annotations__
    sig = inspect.signature(func)
    # get return annotations
    retcheck = annotations.pop('return', None)
    @wraps(func)
    def wrapper(*args, **kwargs):
      bound = sig.bind(*args, **kwargs)
      errors = []
      for name, val in annotations.items():
        try:
          val.check(bound.arguments[name])
        except Exception as e:
          errors.append(f'  {name}: {e}')
      if errors:
        raise TypeError('Bad arguments\n%s' % '\n'.join(errors))
      result = func(*args, **kwargs)
      if retcheck:
        try:
          retcheck.check(result)
        except Exception as e:
          raise TypeError(f'Bad return: {e}') from None
      return result
    return wrapper
  return validated

validated = enforce()

class Validator:
  def __init__(self, name=None):
    self.name = name

  validators = { }
  @classmethod
  def __init_subclass__(cls):
    cls.validators[cls.__name__] = cls

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

_typed_classes = [
  ('Integer', int),
  ('Float', float),
  ('String', str),
]
globals().update((name, type(name, (Typed,), {'expected_type': ty})) for name, ty in _typed_classes)

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
