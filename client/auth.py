import re
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import uuid
import hashlib
import interface
from config import Config
import config
from msgtype import outbound, inbound, length
import os
import packet

def passcheck(password):
	return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,20}', password))

def passhash(password, salt):	
	return(hashlib.sha(hashlib.sha256(salt.encode()+password.encode())))

def new_user(sock):
	username, passhash, mode=interface.acc_create()
	tosend=(username, passhash, mode)
	packet.send_pack(sock, tosend)
	recv_pack=packet.recv_pack(sock)
	if not 'auth' in recv_pack:
		print('username or password invalid')
		print('exiting')
		sys.exit()
	config.adduser(username)
	return True

def old_user(sock):
	username, mode=interface.username_login()
	tosend=(username, mode)
	packet.send_pack(sock, tosend)
	recv_pack=packet.recv_pack(sock)
	if not 'auth' in recv_pack:
		print('username does nt exist')
		print('exiting')
		sys.exit()
	salt=packet.extract_salt(recv_packet)
	tosend=interface.password_login(salt)
	packet.send_pack(tosend)
	recv_pack=packet.recv_pack(sock)
	if not 'auth' in recv_pack:
		print('invalid password')
		print('exiting...')
	config.adduser(username)
	return True
	
def diffiexchange(s):
	nonce=''.join([str(random.SystemRandom().randint(0,9)) for i in range(length['nonce'])])
	
	assert((len(config['USR_PUBLIC_KEY_STRING'])+len(outbound['USR_PUB_KEY'], len(nonce)))==(length['pkey_length']++length['mode']+len(nonce)))
	#testing right length!
	
	packet.send_pack(s,(outbound['USR_PUB_KEY'],
	             nonce ,Config['PUBLIC_KEY_STRING'])) 
    recv_pack=packet.recv_pack(s)
	rec_nonce, ser_nonce, SERVER_PUB_KEY= packet.extract_noncepkey(recv_pack)
	if nonce != rec_nonce:
		raise ___# I don't really know how this raise thing works
    del rec_nonce
	config.add_server_pub_key(SERVER_PUB_KEY)
	encrypted_nonce=encryption.encode_server(ser_nonce)
	packet.send_pack(s, (outbound['AUTH_SERVERPUB_NONCE'], encrypted_nonce))
	recv_pack=packet.recv_pack(s)
	auth, mode=packet.extract(recv_pack)
	if not auth:
		raise ____error____
	else:
		return True
		
def receive_shared_key(sock):
    recv=packet.recv_pack(s)
    key=Fernet(packet.extractshared(recv))
    Config['SHARED_KEY']=key
    
def decrypt_message(msg):
	return Config['SHARED_KEY'].encrypt(msg)
	
def encrypt_message(msg):
	return Config['SHARED_KEY'].decrypt(msg)
