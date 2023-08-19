# structure.py

class Structure:
  _fields = ()
  def __init__(self, *args):
    if len(args) != len(self._fields):
      raise TypeError(f"Expected {len(self._fields)} arguments")
    for field, arg in zip(self._fields, args):
      setattr(self, field, arg)
  
  def __setattr__(self, name, val):
    if name.startswith('_') or name in self._fields:
      super().__setattr__(name, val)
    else:
      raise AttributeError("No attribute %s" % name)

  def __repr__(self):
    return "%s(%s)" % (self.__class__.__name__, ', '.join(repr(getattr(self, attr)) for attr in self._fields))
