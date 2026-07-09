# Practical 2(b): Bitcoin Core API Interaction Demo

## Full question (as given)
**Bitcoin Core (OC2)**  
b. Demonstrate the use of the Bitcoin Core API to interact with a Bitcoin Core node.

## What this runs
- Connects to a local Bitcoin Core node using JSON-RPC
- Calls basic RPC methods (example: `getblockchaininfo`)
- Wallet is optional for this practical unless you enable `SHOW_WALLETINFO=1`

## Why both `bitcoin-cli` and `main.py`?
- `bitcoin-cli` and `main.py` are both reading the same Bitcoin Core RPC data.
- `bitcoin-cli` proves the node is running and responding.
- `main.py` proves your Python program can talk to the same node through RPC.
- So the command-line check and the Python script are complementary, not duplicate effort.

## Description
Shows how to interact with Bitcoin Core programmatically via JSON-RPC (recommended: `regtest`).

## How the code works (high level)
- Builds a JSON-RPC request body.
- Sends it to the RPC URL with credentials.
- Prints the response result/error.

## Dependencies
- Python 3.10+ recommended
- No third-party Python packages (stdlib only)

## Software required
- **Python**: 3.10+ recommended
- **Bitcoin Core**: `bitcoind` and `bitcoin-cli` (recommended: `regtest` for labs)

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

## 1) One-time setup (Windows 10/11)
1) Install **Python 3.x** (3.10+ recommended) with `py` launcher and PATH.
2) Install Bitcoin Core and ensure both `bitcoind` and `bitcoin-cli` are available.
3) Verify Python in PowerShell:
```powershell
py -V
py -c "import sys; print(sys.executable)"
```
4) Verify Bitcoin Core binaries:
```powershell
bitcoind -version
bitcoin-cli -version
```
If `bitcoind` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoind.exe" -version
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -version
```
Cookie path on many Windows installs is:
```powershell
$env:LOCALAPPDATA\Bitcoin\regtest\.cookie
```

## 3) Run (Windows 10/11)
### A) Terminal 1: Start Bitcoin Core in regtest (recommended)
Start `bitcoind` in its own terminal:
```powershell
bitcoind -regtest -server -txindex=1
```
If `bitcoind` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoind.exe" -regtest -server -txindex=1
```

Cookie auth will be created automatically at:
- `%LOCALAPPDATA%\Bitcoin\regtest\.cookie`

### B) Terminal 2: Run the Python RPC demo (cookie auth)
```powershell
cd practical_02\b_bitcoin_core_api_demo
py -m venv .venv
.\.venv\Scripts\activate.bat
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
$env:RPC_URL="http://127.0.0.1:18443"   # default regtest RPC
$env:RPC_COOKIE="$env:LOCALAPPDATA\\Bitcoin\\regtest\\.cookie"
# Optional: $env:SHOW_WALLETINFO="1"
.\.venv\Scripts\python code\main.py
```
To verify the node directly with `bitcoin-cli`:
```powershell
bitcoin-cli -regtest getblockchaininfo
```
If `bitcoin-cli` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest getblockchaininfo
```

## Notes / troubleshooting
- If `bitcoind` is not on PATH, use the full path to the binary (Bitcoin Core install folder).
- If `bitcoin-cli` is not on PATH, use the same full-path approach as `bitcoind`.
- If you see `HTTP Error 500` from `getwalletinfo`, that is normal when no wallet is loaded; the demo still succeeds with `getblockchaininfo`.
- If the script prints `Missing RPC auth`, confirm the `.cookie` file exists and `bitcoind` is running.
- If you want wallet output, create or load a wallet first and set `SHOW_WALLETINFO=1`.

## Output notes
- Save screenshots/logs in `output/`.

<!--


































































































































-->

## 2) One-time setup (Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

## 4) Run (Ubuntu)
### A) Terminal 1: Start Bitcoin Core in regtest (recommended)
```bash
bitcoind -regtest -server -txindex=1 -fallbackfee=0.0002
```

Cookie auth will be created automatically at:
- `~/.bitcoin/regtest/.cookie`

### B) Terminal 2: Run the Python RPC demo (cookie auth)
```bash
cd practical_02/b_bitcoin_core_api_demo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
export RPC_URL="http://127.0.0.1:18443"
export RPC_COOKIE="$HOME/.bitcoin/regtest/.cookie"
python code/main.py
```
