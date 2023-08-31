# tableformat.py

from abc import ABC, abstractmethod

__all__ = ['create_formatter', 'print_table']

class TableFormatter(ABC):
  @abstractmethod
  def headings(self, headers):
    raise NotImplementedError()
  
  @abstractmethod
  def row(self, rowdata):
    raise NotImplementedError()

class TextTableFormatter(TableFormatter):
  def headings(self, headers):
    print(' '.join('%10s' % h for h in headers))
    print(('-'*10 + ' ')*len(headers))

  def row(self, rowdata):
    print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
  def headings(self, headers):
    print(','.join(headers))

  def row(self, rowdata):
    print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
  def headings(self, headers):
    hdrs = ' '.join(f'<th>{h}</th>' for h in headers)
    print(f'<tr> {hdrs} </tr>')

  def row(self, rowdata):
    dt = ' '.join(f'<td>{d}</td>' for d in rowdata)
    print(f'<tr> {dt} </tr>')

class ColumnFormatMixin:
  formats = []
  def row(self, rowdata):
    rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
    super().row(rowdata)

class UpperHeadersMixin:
  def headings(self, headers):
    super().headings([h.upper() for h in headers])

def create_formatter(fmt, column_formats=None, upper_headers=False):
  if fmt == 'text':
    formatter_cls = TextTableFormatter
  elif fmt == 'csv':
    formatter_cls = CSVTableFormatter
  elif fmt == 'html':
    formatter_cls = HTMLTableFormatter
  else:
    raise ValueError(f'Format {fmt} not found')

  if column_formats:
    class formatter_cls(ColumnFormatMixin, formatter_cls):
      formats = column_formats

  if upper_headers:
    class formatter_cls(UpperHeadersMixin, formatter_cls):
      pass
  return formatter_cls()

def print_table(records, headers, formatter):
  if not isinstance(formatter, TableFormatter):
    raise TypeError('Not instance of TableFormatter')
  formatter.headings(headers)
  for r in records:
    rowdata = [getattr(r, fieldname) for fieldname in headers]
    formatter.row(rowdata)

if __name__ == '__main__':
  import stock, reader
  portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock) 
  formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f']) 
  print_table(portfolio, ['name','shares','price'], formatter)
  print()
  formatter = create_formatter('text', upper_headers=True)
  print_table(portfolio, ['name','shares','price'], formatter)
