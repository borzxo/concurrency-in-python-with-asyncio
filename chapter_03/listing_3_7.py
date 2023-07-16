import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)  # A

    if len(events) == 0:  # B
        print('No events, still waiting!')

    for event, _ in events:
        event_socket = event.fileobj  # C

        if event_socket == server_socket:  # D
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Got connection from {address}')
            selector.register(connection, selectors.EVENT_READ)  # E

        else:
            data = event_socket.recv(1024)  # F
            print(f'Got data {data}')
            event_socket.send(data)
