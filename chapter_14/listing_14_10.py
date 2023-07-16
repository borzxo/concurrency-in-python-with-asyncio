import functools
import selectors
import socket
from listing_14_8 import CustomFuture
from selectors import BaseSelector


def accept_connection(future: CustomFuture, connection: socket):
    print(f'Got connection request from {connection}')
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket:
    print('Socket registering to listen for connections')
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print('Pausing to listen for connections...')
    connection: socket = await future
    return connection


async def main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8000))
    sock.setblocking(False)

    print('Waiting for socket connection!')
    connection = await sock_accept(sel, sock)
    print(f'Got a connection {connection}!')


selector = selectors.DefaultSelector()

coro = main(selector)

while True:
    try:
        state = coro.send(None)

        events = selector.select()

        for k, m in events:
            print('Processing selector events...')
            callback = k.data
            callback(k.fileobj)
    except StopIteration as si:
        print('Application finished!')
        break
