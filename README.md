# 🏴 CTF Writeups & PoC Collection

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green) ![Tests](https://img.shields.io/badge/tests-passing-success) ![Status](https://img.shields.io/badge/status-active-brightgreen)

Documented solutions from HackTheBox, TryHackMe, and CTF competitions.

## Structure
```
ctf-writeups/
├── HackTheBox/
│   ├── Easy/
│   ├── Medium/
│   └── Hard/
├── TryHackMe/
├── CTF-Competitions/
└── tools/
    ├── rev_shell_gen.py
    └── lfi_scanner.py
```

## Methodology
**Recon → Enum → Exploit → PrivEsc → Post-Exploitation**

```bash
# Recon
nmap -sV -sC -oA scan target
ffuf -w wordlist.txt -u http://target/FUZZ

# Linux PrivEsc
find / -perm -u=s -type f 2>/dev/null  # SUID
sudo -l                                  # sudo rights
linpeas.sh | tee linpeas.out
```

## Completed Machines

| Platform | Machine | Difficulty | Techniques |
|----------|---------|------------|------------|
| HTB | Lame | Easy | SMB exploit CVE-2007-2447 |
| HTB | Blue | Easy | EternalBlue MS17-010 |
| HTB | Jerry | Easy | Tomcat Manager RCE |
| HTB | Mirai | Easy | Default Pi-hole creds |
| THM | Mr. Robot | Medium | WP brute-force, SUID nmap |
| THM | Steel Mountain | Medium | HFS exploit, PowerShell privesc |
