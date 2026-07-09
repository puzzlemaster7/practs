# Practical 2(a): Python Program to Demonstrate Mining

## Full question (as given)
**Bitcoin / Mining (OC2)**  
a. Write a python program to demonstrate mining.

## What this runs
- Computes SHA-256 hashes for block data + nonce
- Finds a nonce such that the hash starts with `difficulty` leading zeros
- Prints the mined nonce, hash, and time taken

## Description
Demonstrates Proof-of-Work mining by brute-force searching for a nonce that satisfies a difficulty target.

## How the code works (high level)
- Builds a small block header string (data + previous hash + nonce).
- Repeatedly hashes until the prefix condition is satisfied.
- Measures time to show how difficulty impacts mining.

## Dependencies
- Python 3.10+ recommended

## Software required
- **Python**: 3.10+ recommended

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

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
cd practical_02\a_python_mining_demo
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
cd practical_02/a_python_mining_demo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python code/main.py
```

## Output notes
- Save screenshots/logs in `output/`.
