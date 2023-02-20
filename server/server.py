import socket
import threading

host = '127.0.0.1'
port = 55555
separator_token = "<SEP>"
client_socets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
print(f"[*] listenin {host} : {port}")

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f'[!] Error: {e}')
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_socets:
            client_socket.send(msg.encode())
            
while True:
    client_socket, client_address = s.accept()
    print(f'[+] {client_address} connected')
    client_socets.add(client_socket)
    t = threading.Thread(target=listen_for_client, args=(client_socket, ))
    t.daemon = True
    t.start()
for cs in client_socets:
    cs.close()
s.close()    