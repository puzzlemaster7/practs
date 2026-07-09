# Practical 2(d): Mining using Geth on a Private Network

## Full question (as given)
**Ethereum / Geth (OC2)**  
d. Demonstrate mining using geth on your private network.

## What this is
This is mostly a **commands + screenshots/logs** practical.

## Description
Demonstrates starting a local `geth --dev` chain and proving block production with a self-transaction.

## Software required
- **Geth** (`geth`) installed
- **PowerShell** on Windows 10/11

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

## Local execution (dev chain)
This uses `geth --dev`, which starts a local development chain without a custom genesis file. It is suitable for labs and avoids public networks.

### 1) Terminal 0: Create a fresh data directory
Choose a folder (inside this practical is fine):
```powershell
cd practical_02\d_geth_private_mining_demo
mkdir datadir
```

### 2) Terminal 1: Start geth in dev mode
```powershell
geth --dev --datadir .\datadir --http --http.addr 127.0.0.1 --http.port 8545 --http.api eth,net,web3,miner,admin --ipcdisable --nodiscover --verbosity 3 console
```
If `geth` is not recognized, use the full path:
```powershell
& "C:\Program Files\Geth\geth.exe" --dev --datadir .\datadir --http --http.addr 127.0.0.1 --http.port 8545 --http.api eth,net,web3,miner,admin --ipcdisable --nodiscover --verbosity 3 console
```

### 3) Terminal 1 (inside geth console): Check the developer account and block height
```javascript
eth.accounts
eth.blockNumber
eth.sendTransaction({from: eth.accounts[0], to: eth.accounts[0], value: web3.toWei(0.1, "ether")})
eth.blockNumber
```

### 4) Optional proof to capture in `output/`
- `geth --dev ... console` startup logs
- `eth.accounts`
- `eth.blockNumber` before and after the transaction
- `eth.sendTransaction(...)` returning a transaction hash

## What to capture in `output/`
- `geth --dev ... console` startup logs
- `eth.accounts`
- `eth.blockNumber` before and after the transaction
- `eth.sendTransaction(...)` and the resulting mined block

## Ubuntu notes
Commands are the same, but paths use `/`:
```bash
mkdir -p datadir
geth --dev --datadir ./datadir --http --http.addr 127.0.0.1 --http.port 8545 --http.api eth,net,web3,miner,admin --ipcdisable --nodiscover --verbosity 3 console
```
