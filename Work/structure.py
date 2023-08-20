# structure.py

import sys

class Structure:
  _fields = ()
  @staticmethod
  def _init():
    locs = sys._getframe(1).f_locals
    self = locs.pop('self')
    for name, val in locs.items():
      setattr(self, name, val)
  
  def __setattr__(self, name, val):
    if name.startswith('_') or name in self._fields:
      super().__setattr__(name, val)
    else:
      raise AttributeError("No attribute %s" % name)

  def __repr__(self):
    return "%s(%s)" % (self.__class__.__name__, ', '.join(repr(getattr(self, attr)) for attr in self._fields))
