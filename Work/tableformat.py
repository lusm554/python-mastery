# tableformat.py

class TableFormatter:
  def headings(self, headers):
    raise NotImplementedError()

  def row(self, rowdata):
    raise NotImplementedError()

class TextTableFormatter(TableFormatter):
  def headings(self, headers):
    print(' '.join('%10s' % h for h in headers))
    print(('-'*10 + ' ')*len(headers))

  def row(self, rowdata):
    print(' '.join('%10s' % d for d in rowdata))

def print_table(records, headers, formatter):
  formatter.headings(headers)
  for r in records:
    rowdata = [getattr(r, fieldname) for fieldname in headers]
    formatter.row(rowdata)

