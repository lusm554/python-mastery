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

def print_table(records, headers, formatter):
  formatter.headings(headers)
  for r in records:
    rowdata = [getattr(r, fieldname) for fieldname in headers]
    formatter.row(rowdata)

if __name__ == '__main__':
  import stock, reader
  portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
  formatter = CSVTableFormatter()
  print_table(portfolio, ['name','shares','price'], formatter)
  formatter = HTMLTableFormatter()
  print_table(portfolio, ['name','shares','price'], formatter)
