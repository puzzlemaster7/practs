# Practical 1(b): Multiple Transactions and Organized Display

## Full question (as given)
**Introduction to Blockchain Practical (OC1)**  
b. Allow users to create multiple transactions and display them in an organised format.

## What this runs
- Takes multiple transactions as input (sender/receiver/amount)
- Displays them in a readable organized format (table)

## Description
Builds a small in-memory transaction list and prints it neatly for easy verification.

## How the code works (high level)
- Reads/creates multiple transaction entries.
- Stores them in a list.
- Prints a formatted output (optionally sorted).

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
cd practical_01\b_multiple_transactions_display
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
cd practical_01/b_multiple_transactions_display
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python code/main.py
```

## Output notes
- Save screenshots/logs in `output/`.
