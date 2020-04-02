import uuid
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


def init_conf():
    config=dict()
    config['PRIVATE_KEY']=rsa.generate_private_key(
	   		 public_exponent=65537,
	    		key_size=2048,
	   	 	backend=default_backend()
   		 )
    config['USR_PUBLIC_KEY']=config['PRIVATE_KEY'].public_key()
    config['USR_PUBLIC_KEY_STRING']=config['USR_PUBLIC_KEY'].public_bytes(
	    		encoding=serialization.Encoding.PEM,
	    		format=serialization.PublicFormat.SubjectPublicKeyInfo
		)
    return config
    
def adduser(user):
    global config
    config['USERNAME']=user

def add_server_pub_key(pkey):
    global config
    config['SERVER_PUBLIC_KEY']=pkey
    
    
	
Config=init_conf()

