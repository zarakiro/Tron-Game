import socket
import threading
import queue
import json

MAX_CLIENTS = 4

class NetworkServer():

    def __init__(self, ip_addr: str, port: int) -> None:
        self.ip_addr = ip_addr
        self.port = port
        # self.sending_queue = queue.Queue()
        self.event_queue=queue.Queue()
        self.clients = []

        self.sockets = []        
        self.players = {}

        # self.rcv_msg_callback = rcv_msg_callback
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_addr, self.port))
        self.server_socket.listen(MAX_CLIENTS)
        # self.client_socket, self.client_addr = self.server_socket.accept()
        self.run = True
        # self._rcv_thread = threading.Thread(target=self._rcv_thread_target)


        self.wait_client=threading.Thread(target=self._waiting_for_clients)
        self.wait_client.start()

    def _waiting_for_clients(self):
        while self.run:
            try:
                client_socket,client_addr = self.server_socket.accept()
                self.event_queue.put((client_addr[1], 'new_player,'))
                new_thread = threading.Thread(target=self._client_thread_target, args=(client_socket,client_addr[1]))
                self.clients.append(new_thread)
                self.sockets.append(client_socket)
                new_thread.start()
            except Exception as e:
                print(f"Error accepting client: {e}")
                break


    def _client_thread_target(self, client_socket : socket.socket, addr : str):
        while self.run :
            msg_rcv = client_socket.recv(1024).decode('utf-8')
            self.event_queue.put((addr,msg_rcv))


    def sendall(self, data : dict):
        for socket in self.sockets:
            j=json.dumps(data)
            #j = json.dumps({str(k): v for k, v in data.items()})
            socket.sendall(j.encode())
            # socket.send(str(data).encode('utf-8'))

    def get_event_queue(self):
        return self.event_queue

    

    # def _rcv_thread_target(self):
    #     while self.run:
    #         msg_rcv = self.client_socket.recv(1024).decode('utf-8')
    #         # self.rcv_queue.put(msg_rcv)
    #         self.rcv_msg_callback(msg_rcv)

            
    # def _sending_thread_target(self):
    #     while self.run:
    #         msg_sent : str = self.sending_queue.get(block=True)
    #         self.client_socket.send(msg_sent.encode(encoding='utf-8'))

    # def start(self):
    #     self._rcv_thread.start()

    # def stop(self):
    #     self.run = False

    def close(self):
        self.run=False
        self.wait_client.join()
        self.server_socket.close()
        
        

