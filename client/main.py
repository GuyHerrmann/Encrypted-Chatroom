import interface
import threading
import packet
import socket
import sys
from config import Config
import auth
status=list()

sock=socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.connect(Config.IP, Config.PORT)

if interface.is_newuser:
	auth.new_user(sock)
else:
	auth.old_user(sock)

if not auth.diffiexchange(sock):
	print('error, diffiehelman exchange not succesful')
	sys.exit()
auth.receive_shared_key(sock)

t1=threading.Thread(interface.receive_inputs)
t2=threading.Thread(interface.receive_sockets, arg=sock)

t1.start()
t2.start()

t1.join()
t2.join()

