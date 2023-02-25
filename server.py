import socket


server = socket.create_server(('127.0.0.1', 8000))
# Настройка для освобождения порта после выхода из программы
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.listen(10)

try:
    while True:
        client_socket, address = server.accept()

        # чтение данных из клиентского сокета
        # по 1024 байта декодируя их в ютф-8
        recived_data = client_socket.recv(1024).decode('utf-8')

        print(f'Получили данные по сокету: {recived_data}')

        path = recived_data.split(' ')[1]

        response = (
            f'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
            f'Привееет!<br/>Path: {path}'
            )

        client_socket.send(response.encode('utf-8'))
        client_socket.shutdown(socket.SHUT_RDWR) # корректное выключение сокета
except KeyboardInterrupt:
    print('Сервер выключен')
    server.shutdown(socket.SHUT_RDWR)
    server.close()
