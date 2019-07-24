a="1c0111001f010100061a024b53535009181c"
b="686974207468652062756c6c277320657965"

a=bytearray.fromhex(a)
b=bytearray.fromhex(b)

def xor(s1,s2):
	b=bytearray(len(s1))
	for i in range(len(s1)):
		b[i]=s1[i]^s2[i]
	return b

ans=bytes(xor(a,b))
print(ans.hex())