
outbound={'NEWUSR_CREATE': 0, 
	'OLDUSR_USRNAME':1,
	'OLDUSR_PASS':2,
	'USR_PUBKEY':3,
	'AUTH_SERVERPUB_NONCE':4,
	'CONFIRMATION': 5,
	'MSG_BROADCAST': 6}

inbound={0:'RESP_NEWUSR',
        1: 'RESP_USRNAME',
	2: 'RESP_LOGIN',
	3: 'RESP_PUBKEY_USR_NONCE',
	4: 'RESP_CONFIRMATION',
	5: 'MSG_REC'
}

length={
	'salt': 32,
	'nonce':8,
	'pkey_length': 451,	
	'mode': 1,
	'encrypted_nonce':256,
	'shared_key': 44
}
