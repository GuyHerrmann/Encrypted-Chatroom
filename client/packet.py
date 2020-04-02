from msgtype import length

def pack_send(sock, tosend):
	tosend=''.join(tosend).encode('utf-8')
	sock.sendall(tosend)

def pack_recv(sock):
	return sock.recv(1024).strip()

def extract_salt(recv):
	salt=recv[length['mode']:length['mode']+length['salt']]
	assert(len(salt)==length['salt'])
	return salt
def extract_noncepkey(recv):
	s1=length['mode']
	s2=length['mode']+length['nonce']
	s3=length['mode']+length['nonce']+length['encryptednonce']
	s4=length['mode']+length['nonce']*2+length['pkey']
	mode=recv[0, s1]
	recieved_nonce=encryption.decode(recv[s2, s3])
	
	server_pkey=encryption.extract_server_pkey(recv[s3, s4])
	return (recieved_nonce, server_nonce, server_pkey)	

def extractshared(recv):
	s1=length['mode']
	s2=length['sharedkey']
	return recv[s1:s1+s2]

def extract_message(msg):
	s1=length['mode']
	s2=length['mode']+length['username']
	mode=msg[0:s1]
	username=msg[s1:s2]
	message=msg[s2:]
	return (username, message)
