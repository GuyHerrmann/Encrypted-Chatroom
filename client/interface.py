import re
import uuid
import getpass
import sys
import auth
import msgtype
from config import Config

yn_toBool={'y': True, 'n': False}

def is_newuser():
	while True:
		try:
			isnew=str(raw_input('Welcome, are you a new user? (y/n)'))
		except KeyboardInterrupt:
			sys.exit()
		try:
			return yn_toBool[isnew]
		except KeyError:
			print('invalid input')

def acc_create():
	while True:
		username=raw_input('Enter Username>')
		password=getpass.getpass('Enter Password>')
		if auth.passcheck(password):
			salt=uuid.uuid4.hex
			return(username, auth.passhash(password, salt),salt,  msgtype.outbound['NEWUSR_CREATE'] )
		else:
			print('invalid password, spesification: 8 to 20 have 1 capital letter, one lowercase and on nonalphanumeric character')
	
def username_login():
	while True:
		username=raw_input('Enter Username>')
		if len(username)>7 and len(username)<21:
			return(username, msgtype.outbound['OLDUSR_USRNAME'])

def password_login(salt):
	while True:
		try:
			password=getpass.getpass('Enter Password>')
		except KeyboardInterrupt:
			sys.exit()
		if auth.passcheck(password):
			passhashed=auth.passhash(password, salt)
			return(passhashed, msgtype.outbound['OLDUSR_PASS'])

def receive_inputs(sock):
	try:
		while True:
			msg=input('{}>'.format(Config['USERNAME']))
		#will need something to limit the length
			encrypted=auth.encrypt_message(msg)
			packet.send_pack(sock, (outbound['MESSAGE'], encrypted, time.time()))
	except KeyboardInterrupt:
		exit_routine()


def receive_sockets(sock):
	try:
		while True:
			rcv_encrypted=packet.pack_recv(sock)
			rcv=auth.decrypt_message(rcv_encrypted)
			user, msg=packet.extract_message(rcv)
			print('{0} > {1}'.format(user, msg))
	except KeyboardInterrupt:
		exit_routine()
