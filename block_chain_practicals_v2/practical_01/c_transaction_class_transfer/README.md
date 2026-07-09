# Practical 1(c): `Transaction` Class + Transfer Method

## Full question (as given)
**Introduction to Blockchain Practical (OC1)**  
c. Create a Python class named Transaction with attributes for sender, receiver, and amount. Implement a method within the class to transfer money from the sender's account to the receiver's account.

## What this runs
- Creates an in-memory balance map
- Creates a `Transaction(sender, receiver, amount)`
- Transfers amount after validation

## Description
Demonstrates how a transaction updates account balances (similar to a ledger update) with basic checks.

## How the code works (high level)
- Defines `Transaction` as a dataclass.
- `transfer(balances)` validates:
  - sender/receiver exist
  - amount > 0
  - sender has sufficient funds
- Updates balances accordingly.

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
cd practical_01\c_transaction_class_transfer
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
cd practical_01/c_transaction_class_transfer
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python code/main.py
```

## Output notes
- Save screenshots/logs in `output/`.
