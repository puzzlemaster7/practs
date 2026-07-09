# Tools Setup (Windows 10/11 + Ubuntu)

This guide is written so each practical can be executed on a **new machine** without needing extra online help (other than downloading/installing the software).

## 0) Common checks
Always verify versions first:
- Windows (PowerShell): `python --version`, `py -V`, `node -v`, `npm -v`, `docker --version`
- Ubuntu: `python3 --version`, `node -v`, `npm -v`, `docker --version`

---

## 1) Python (for Python practicals)

### Windows 10/11
1) Install **Python 3.10+** from python.org.
2) In the installer, enable:
   - **Add Python to PATH**
   - **Install `py` launcher**
3) Verify in PowerShell:
```powershell
py -V
py -c "import sys; print(sys.executable)"
py -m pip -V
```
4) If PowerShell venv activation is blocked (common on college PCs):
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
If you still can’t activate, run everything via `.\.venv\Scripts\python.exe` (no activation needed).

### Ubuntu
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
python3 -m pip -V
```

---

## 2) Node.js + npm (for Solidity/DApp/NFT practicals)

### Windows 10/11
1) Install **Node.js LTS** from nodejs.org.
2) Verify:
```powershell
node -v
npm -v
```

### Ubuntu
Install Node.js LTS using your preferred method (snap/apt/nvm). Verify:
```bash
node -v
npm -v
```

---

## 3) Ganache (local Ethereum chain)
In this repo, Ganache is included as an `npm` dependency in each Truffle-based practical, so you can run it with:
- `npx ganache -p 8545`

No global install required.
Important:
- Run `npm install` inside each practical folder that has its own `package.json`.
- Keep Ganache and Truffle in separate terminals when a README says to do so.

---

## 4) Truffle (Solidity compile/deploy)
In this repo, Truffle is included as a local dev dependency per practical, so you use:
- `npm install`
- `npx truffle compile`
- `npx truffle migrate --network development`

No global install required.

---

## 5) Bitcoin Core (bitcoind + bitcoin-cli)

### Windows 10/11
1) Install **Bitcoin Core** (includes `bitcoind.exe` and `bitcoin-cli.exe`).
2) Ensure the install folder is on PATH or run from the install directory.
3) For regtest lab work, start the node first with `-regtest -server`.
4) The regtest cookie is usually stored under:
```powershell
$env:LOCALAPPDATA\Bitcoin\regtest\.cookie
```
5) Verify:
```powershell
bitcoind -version
bitcoin-cli -version
```
6) If `bitcoind` is not recognized, use the full executable path.
7) If a practical mentions `bitcoin-cli` output only, that is still a real RPC call against the running node.

### Ubuntu
Install Bitcoin Core using your package method. Verify:
```bash
bitcoind -version
bitcoin-cli -version
```

---

## 6) Geth (Ethereum client)

### Windows 10/11
1) Open the official download page: [https://geth.ethereum.org/downloads/](https://geth.ethereum.org/downloads/)
2) Download the **Windows amd64** archive for a stable release.
3) Extract it to a simple folder such as `C:\Tools\geth\`.
4) Either add that folder to `PATH` or call the executable by full path.
5) Verify:
```powershell
geth version
```
6) If `geth` is not recognized, use:
```powershell
& "C:\Tools\geth\geth.exe" version
```

### Ubuntu
Install `geth` using the official Linux package or release archive, then verify:
```bash
geth version
```

---

## 7) Docker (for Iroha practical)

### Windows 10/11
1) Install **Docker Desktop**.
2) Make sure Docker Desktop is running before you start the Iroha demo.
3) Verify:
```powershell
docker --version
docker compose version
```

### Ubuntu
Install Docker Engine + Compose. Verify:
```bash
docker --version
docker compose version
```

---

## 8) Browser / frontend tools
Some practicals have a browser-facing result:
- Angular DApp practicals may need a browser to open `http://localhost:4200`
- NFT demos may need the browser only for verification screenshots

No extra global install is required beyond Node.js unless a specific README says otherwise.
