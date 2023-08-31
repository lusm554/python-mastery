# html.py

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
  def headings(self, headers):
    hdrs = ' '.join(f'<th>{h}</th>' for h in headers)
    print(f'<tr> {hdrs} </tr>')

  def row(self, rowdata):
    dt = ' '.join(f'<td>{d}</td>' for d in rowdata)
    print(f'<tr> {dt} </tr>')
