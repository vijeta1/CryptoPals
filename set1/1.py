import base64

my_str="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
b=bytearray.fromhex(my_str).decode()
c= bytes(b,'utf-8')
base=base64.b64encode(c)
base=base.decode('utf-8')
print(base)