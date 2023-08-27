# structure.py

import sys
import inspect
from validate import Validator, validated

def validate_attributes(cls):
  '''
  Class decorator that scans a class definition for Validators
  and builds a _fields variable that captures their definition order.
  '''
  validators = []
  for name, val in vars(cls).items():
    if isinstance(val, Validator):
      validators.append(val)
    elif callable(val) and val.__annotations__:
      setattr(cls, name, validated(val))
  cls._fields = tuple([val.name for val in validators])
  cls._types = tuple([ getattr(v, 'expected_type') for v in validators]) 
  cls.create_init()
  return cls

class Structure:
  _fields = ()
  _types = ()

  @classmethod
  def __init_subclass__(cls):
    validate_attributes(cls)

  @classmethod
  def create_init(cls):
    argstr = ','.join(cls._fields)
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
      code += f'  self.{name} = {name}\n'
    locs = { }
    exec(code, locs)
    cls.__init__ = locs['__init__']

  @classmethod
  def from_row(cls, row):
    rowdata = [ cast(val) for val, cast in zip(row, cls._types) ]
    return cls(*rowdata)

  @classmethod
  def set_fields(cls):
    sig = inspect.signature(cls)
    cls._fields = tuple(sig.parameters) 
  
  def __setattr__(self, name, val):
    if name.startswith('_') or name in self._fields:
      super().__setattr__(name, val)
    else:
      raise AttributeError("No attribute %s" % name)

  def __repr__(self):
    return "%s(%s)" % (self.__class__.__name__, ', '.join(repr(getattr(self, attr)) for attr in self._fields))
