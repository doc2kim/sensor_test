
import socket
import time
import threading
from data_slicing import Slicing


def binder(client_socket, addr):

    try:
        while True:
            receive_data = client_socket.recv(73)
            if not receive_data:
                print(addr, "to quit!")
                print("Waiting for next data...")
                break
            msg = receive_data.hex()
            print("data received!!", time.strftime(
                '%Y-%m-%d'), time.strftime('%H:%M:%S'))

            if msg:
                print('Received from', addr, msg)
                slicing = Slicing(msg)

                """ -------------------테스트 값 적용------------------- """

                slicing.temp()
                slicing.oxygen()
                slicing.ph()
                slicing.conductivity()

                """ ------------------------------------------------- """

            length = len(receive_data)
            client_socket.sendall(length.to_bytes(4, byteorder="big"))
            client_socket.sendall(receive_data)

    except ConnectionResetError as e:
        print(e, addr)

    finally:
        print("client socket close!!")
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('172.30.1.38', 6557))


server_socket.listen()
print('Server start up!')

try:
    while True:
        print('Receiving data...')
        client_socket, addr = server_socket.accept()
        th = threading.Thread(target=binder, args=(client_socket, addr))
        th.start()
        print("Device address : ", addr)
except socket.error as e:
    print(e)

finally:
    print("server socket close!!")
    server_socket.close()
