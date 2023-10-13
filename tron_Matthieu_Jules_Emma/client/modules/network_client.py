import socket
import threading
import queue
import json
import sys

class NetworkClient():
    def __init__(self, ip_addr : str, port : int) -> None:
        self.ip_addr = ip_addr
        self.port = port
        self.sending_queue = queue.Queue()
        #self.rcv_queue=queue.Queue()
        self.players={}
        self.socket : socket.socket = None
        self.run=True
        self.connect()
        self._sending_thread = threading.Thread(target=self._sending_thread_target)
        self._rcv_thread = threading.Thread(target=self._rcv_thread_target)
        self.start()    
        
        

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.ip_addr, self.port))
        except socket.error as e:
            print(f"Erreur de connexion : {e}")
            return None
        except EOFError:
            print("Erreur : flux de données vide lors de la connexion.")
            return None
        
    def _sending_thread_target(self):
        while self.run:
            msg_sent : str = self.sending_queue.get(block=True)
            self.socket.send(msg_sent.encode(encoding='utf-8'))

    def _rcv_thread_target(self):
        while self.run:
            try:
                msg_rcv = self.socket.recv(20480).decode()
                # print(f'message received : {msg_rcv}')
                
                msg_rcv = json.loads(msg_rcv)
                # msg_rcv=eval(msg_rcv)
                #self.rcv_queue.put(msg_rcv)
                self.players.update(msg_rcv)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
            
    def start(self):
        self._rcv_thread.start()
        self._sending_thread.start()

    def stop(self):
        self.run=False

    def close(self):
        self.socket.close()
