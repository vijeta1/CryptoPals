def xor(text,key):
	res=bytearray(len(text))
	for i in range(len(text)):
		res[i]=text[i] ^ key[i]
	return res

s="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
s=bytes(s,'ascii')
key="ICE"
key= key * len(s)
key=bytes(key,'ascii')

ans=bytes(xor(s,key))
print(ans.hex())