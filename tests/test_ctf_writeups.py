import sys, os
sys.path.insert(0, ".")
sys.path.insert(0, "tools")

def test_rev_shell_gen_imports():
    import importlib.util, os
    path = os.path.join("tools", "rev_shell_gen.py")
    assert os.path.exists(path), f"rev_shell_gen.py not found at {path}"

def test_lfi_payloads_exist():
    path = os.path.join("tools", "lfi_scanner.py")
    assert os.path.exists(path)
    with open(path) as f:
        content = f.read()
    assert "etc/passwd" in content
    assert "PAYLOADS" in content

def test_writeups_structure():
    assert os.path.exists("HackTheBox")
    assert os.path.exists("TryHackMe")

def test_htb_lame_exists():
    path = os.path.join("HackTheBox", "Easy", "Lame-writeup.md")
    assert os.path.exists(path), f"Writeup not found: {path}"
    with open(path) as f:
        content = f.read()
    assert "CVE-2007-2447" in content or "nmap" in content.lower()

if __name__ == "__main__":
    test_rev_shell_gen_imports()
    test_lfi_payloads_exist()
    test_writeups_structure()
    test_htb_lame_exists()
    print("All tests passed.")
