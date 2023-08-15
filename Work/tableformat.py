# tableformat.py

class TableFormatter:
  def headings(self, headers):
    raise NotImplementedError()

  def row(self, rowdata):
    raise NotImplementedError()

def print_table(records, headers, formatter):
  formatter.headings(headers)
  for s in data:
    rowdata = [getattr(r, fieldname) for fieldname in headers]
    formatter.row(rowdata)

