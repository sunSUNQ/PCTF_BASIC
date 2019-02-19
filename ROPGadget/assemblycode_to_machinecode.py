from pwn import *
print asm('XCHG EAX,ESP\nRET\nMOV ECX,[EAX]\nMOV [EDX],ECX\nPOP EBX\nRET'.lower()).encode('hex')
