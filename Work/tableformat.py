# tableformat.py

from abc import ABC, abstractmethod

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

def create_formatter(fmt):
  if fmt == 'text':
    return TextTableFormatter()
  elif fmt == 'csv':
    return CSVTableFormatter()
  elif fmt == 'html':
    return HTMLTableFormatter()
  else:
    raise ValueError(f'Format {fmt} not found')

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
  class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
    formats = ['%s', '%d', '%0.2f']
  formatter = PortfolioFormatter()
  print_table(portfolio, ['name','shares','price'], formatter)
  print()
  
  class PortfolioFormatter2(UpperHeadersMixin, TextTableFormatter):
    pass
  formatter = PortfolioFormatter2()
  print_table(portfolio, ['name','shares','price'], formatter)
