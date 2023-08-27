# structure.py

import sys
import inspect
from validate import Validator

class Structure:
  _fields = ()
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

def validate_attributes(cls):
  validators = []
  for name, val in vars(cls).items():
    if isinstance(val, Validator):
      validators.append(val)
  cls._fields = [val.name for val in validators]
  cls.create_init()
  return cls
