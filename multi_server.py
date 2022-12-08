#UDP
import socket
import logging

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    host = ('127.0.0.1', 9999)
    server.bind(host)

    logging.info('UDP Server on %s:%s...', host[0], host[1])

    user = {}
    while True:
        try:
            data, addr = server.recvfrom(1024)

            if not addr in user:
                for address in user:
                    server.sendto(data + " 進入聊天室...".encode('utf-8'), address)
                
                user[addr] = data.decode('utf-8')
                continue

            if 'EXIT'.lower() in data.decode('utf-8'):
                name  = user[addr]
                user.pop(addr)
                for address in user:
                    server.sendto((name + " 離開聊天室...").encode(), address)

            else:
                print('"%s" from %s:%s' %(data.decode('utf-8'), addr[0], addr[1]))
                for address in user:
                    if address != addr:
                        server.sendto(data, address)

        except ConnectionResetError:
            logging.warning('Someone left unexcept.')

if __name__ == '__main__':
    main()