import unittest
import encryption
from config import Config

class EncryptionTest(unittest.TestCase):
	def setUp(self):
		self.privatekey=rsa.generate_private_key(
        	   		 public_exponent=65537,
    	    		key_size=2048,
        	   	 	backend=default_backend()
       		 )
	
	def test_encode_public_decode_private(self):
	    message='helloimguy'
	    publickey=self.privatekey.public_key()
	    encoded=encryption.encode(message, publickey)
	    decoded=encryption.decode(encoded, self.privatekey)
	    self.assertEqual(decoded, message)
	    
if __name__=='__main__':
    unittest.main()
