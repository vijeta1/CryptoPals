s="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
b=bytearray.fromhex(s).decode()
c=bytes(b,'utf-8')

for i in range(256):
	res=b''
	for byte in c:
		res+=bytes([byte ^ i])
	print(res,i)