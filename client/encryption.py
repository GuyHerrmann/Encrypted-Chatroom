from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from config import Config

def pub_keytostring(pubkey):
    return pubkey.public_bytes(
	            encoding=serialization.Encoding.PEM,
	            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
def decode(token):
    return Config['PRIVATE_KEY'].decrypt(token.encode('utf-8'),
					padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
					algorithm=hashes.SHA256(),
					label=None))
 
def encode_usr(token):
    return Config['USR_PUBLIC_KEY'].encrypt(token.encode('utf-8'),
					padding.OAEP(
						mgf=padding.MGF1(algorithm=hashes.SHA256()),
						algorithm=hashes.SHA256(),
						label=None)
					)
					
def encode_server(token):
    #here maybe test if exists
    return Config['SERVER_PUBLIC_KEY'].encrypt(token.encode('utf-8'),
					padding.OAEP(
						mgf=padding.MGF1(algorithm=hashes.SHA256()),
						algorithm=hashes.SHA256(),
						label=None)
						
def extract_server_pkey(key):
    		return server_pub_key=serialization.load_pem_public_key(
						key,
						backend=default_backend()
				)
					

