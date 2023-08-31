# formatter.py

from abc import ABC, abstractmethod

__all__ = ['create_formatter', 'print_table']

class TableFormatter(ABC):
  @abstractmethod
  def headings(self, headers):
    raise NotImplementedError()
  
  @abstractmethod
  def row(self, rowdata):
    raise NotImplementedError()

class ColumnFormatMixin:
  formats = []
  def row(self, rowdata):
    rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
    super().row(rowdata)

class UpperHeadersMixin:
  def headings(self, headers):
    super().headings([h.upper() for h in headers])

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

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
