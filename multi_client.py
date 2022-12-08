from os import name
import socket
import threading

def recv(sock, addr):
    sock.sendto(name.encode('utf-8'), addr)
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))

def send(sock, addr):
    while True:
        string = input('')
        message = name + ' : ' + string
        data = message.encode('utf-8')
        sock.sendto(data, addr)
        if string.lower() == 'EXIT'.lower():
            break

def main(ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = (ip, 9999)
    tr = threading.Thread(target=recv, args=(client, server), daemon=True)
    ts = threading.Thread(target=send, args=(client, server))
    tr.start()
    ts.start()
    ts.join()
    client.close()

if __name__ == '__main__':
    print("----------歡迎來到聊天室，退出請輸入'EXIT'-------------")
    ip = '127.0.0.1'
    name = input("請輸入名稱：")
    print('-----------------%s----------------' % name)
    main(ip)