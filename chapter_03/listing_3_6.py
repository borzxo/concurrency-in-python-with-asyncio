import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

connections = list()

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Got connection from {client_address}!')
            connections.append(connection)
        except BlockingIOError:
            pass

        for connection in connections:
            try:
                buffer = b''

                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f'Got data: {data}')
                        buffer += data
                print(f'All data {buffer}')
                connection.send(buffer)
            except BlockingIOError:
                pass
finally:
    server_socket.close()