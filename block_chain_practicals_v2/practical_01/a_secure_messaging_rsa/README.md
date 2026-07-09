# Practical 1(a): Secure Messaging using RSA

## Full question (as given)
**Introduction to Blockchain Practical (OC1)**  
a. Develop a secure messaging application where users can exchange messages securely using RSA encryption. Implement a mechanism for generating RSA key pairs and encrypting/decrypting messages.

## What this runs
- Generates RSA key pairs
- Encrypts a message with the receiver’s public key
- Decrypts with the receiver’s private key

## Description
Demonstrates asymmetric cryptography for secure message exchange using RSA.

## How the code works (high level)
- Generates a public/private key pair.
- Encrypts plaintext using the public key.
- Decrypts ciphertext using the private key.

## Dependencies
- Python 3.10+ recommended

## Software required
- **Python**: 3.10+ recommended (Windows: python.org installer)

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

## Security note
This practical implements **educational RSA** (pure Python) for learning. It is **not** production-grade cryptography.

## 1) One-time setup (Windows 10/11)
1) Install **Python 3.x** (3.10+ recommended). In the installer, enable:
   - “Install `py` launcher”
   - “Add Python to PATH”
2) Verify in PowerShell:
```powershell
py -V
py -c "import sys; print(sys.executable)"
```
3) If venv activation is blocked, run once:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 2) One-time setup (Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

## 3) Run (Windows 10/11)
```powershell
cd practical_01\a_secure_messaging_rsa
py -m venv .venv
.\.venv\Scripts\activate.bat
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python code\main.py
```

### If activation is blocked (works everywhere)
```powershell
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python code\main.py
```

## 4) Run (Ubuntu)
```bash
cd practical_01/a_secure_messaging_rsa
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python code/main.py
```

## Output notes
- Save screenshots/logs in `output/`.
