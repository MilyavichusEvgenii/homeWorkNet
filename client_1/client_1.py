import socket
import random
import threading
from datetime import datetime
from colorama import Fore, init, Back

init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
client_color = random.choice(colors)
host = '27.0.0.1'
port = 55555
separator_token = "<SEP>"
s = socket.socket()
print(f'[*] connecting to {host} : {port}')
s.connect((host, port))
print('[+] connected')
name = input('Enter your name: ')
def listening_for_massages():
    while True:
        massage = s.recv(1024).decode()
        print('\n' + massage)

t = threading.Thread(target=listening_for_massages)
t.daemon = True
t.start()
while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    date_now = datetime.now().strftime('%y-%m-%d %H-%M-%S')
    to_send = f"{client_color}[{date_now}] {name} {separator_token} {to_send} {Fore.RESET}"
    s.send(to_send.encode())
    
s.close()
        