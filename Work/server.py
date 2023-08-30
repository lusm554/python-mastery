# server.py

from socket import *
from select import select
from collections import deque
from types import coroutine

tasks = deque()
recv_wait = {}
send_wait = {}

def run():
  while any([tasks, recv_wait, send_wait]):
    while not tasks:
      # Wait until one or more file descriptors are ready for some kind of I/O.
      # can_recv - wait until ready for reading
      # can_send - wait until ready for writing
      can_recv, can_send, _ = select(recv_wait, send_wait, []) 
      for s in can_recv: # add if task ready
        tasks.append(recv_wait.pop(s))
      for s in can_send: # add if task ready
        tasks.append(send_wait.pop(s))
    task = tasks.popleft() # get some task
    try:
      reason, resource = task.send(None)
      if reason == 'recv':
        recv_wait[resource] = task
      elif reason == 'send':
        send_wait[resource] = task
      else:
        raise RuntimeError('Unknown reason %r' % reason)
    except StopIteration:
      print('Task done')

class GenSocket:
  def __init__(self, sock):
    self.sock = sock

  @coroutine
  def accept(self):
    yield 'recv', self.sock
    client, addr = self.sock.accept()
    return GenSocket(client), addr

  @coroutine
  def recv(self, maxsize):
    yield 'recv', self.sock
    return self.sock.recv(maxsize)

  @coroutine
  def send(self, data):
    yield 'send', self.sock
    return self.sock.send(data)

  def __getattr__(self, name):
    return getattr(self.sock, name)

async def tcp_server(address, handler):
  sock = GenSocket(socket(AF_INET, SOCK_STREAM))
  sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  sock.bind(address)
  sock.listen()
  while True:
    client, addr = await sock.accept() 
    tasks.append(handler(client, addr))

async def echo_handler(client, address):
  print('Connection from', address)
  while True:
    data = await client.recv(1000)
    if not data:
      break
    await client.send(b'GOT:' + data)
  print('Connection closed')

if __name__ == '__main__':
  tasks.append(tcp_server(('127.0.0.1', 8080), echo_handler))
  run()
