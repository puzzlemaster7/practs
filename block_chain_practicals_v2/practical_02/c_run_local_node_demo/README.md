# Practical 2(c): Run a Blockchain Node Locally

## Full question (as given)
**Blockchain Node (OC2)**  
c. Demonstrating the process of running a blockchain node on your local machine.

## What this is
This is mostly a **commands + screenshots/logs** practical (you may not need Python code).

## Description
Demonstrates setting up a local node and verifying it via logs and RPC calls.

## Software required
- **Bitcoin Core** (`bitcoind` + `bitcoin-cli`)

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

---

## Path A: Bitcoin Core node (regtest) — recommended

### A1) Terminal 1: Start the node
Run in PowerShell (Windows) or Terminal (Ubuntu):
```bash
bitcoind -regtest -server -txindex=1
```
If `bitcoind` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoind.exe" -regtest -server -txindex=1
```

### A2) Terminal 2: Verify it is running (CLI)
```bash
bitcoin-cli -regtest getblockchaininfo
```
If `bitcoin-cli` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest getblockchaininfo
```

### A3) Create a wallet and mine blocks (optional but strong proof)
Wallet is required only for the mining proof below. If you skip mining, you can skip the wallet step.

Windows PowerShell:
```powershell
bitcoin-cli -regtest createwallet "labwallet"
$addr = & "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest getnewaddress
bitcoin-cli -regtest generatetoaddress 101 $addr
bitcoin-cli -regtest getblockcount
```

If `bitcoin-cli` is not recognized, use the full path:
```powershell
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest createwallet "labwallet"
$addr = & "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest getnewaddress
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest generatetoaddress 101 $addr
& "C:\Program Files\Bitcoin\daemon\bitcoin-cli.exe" -regtest getblockcount
```

### A4) Proof to capture in `output/`
- `bitcoind` startup logs showing it finished loading (e.g., “Done loading”)
- `bitcoin-cli -regtest getblockchaininfo` output
- `bitcoin-cli -regtest getblockcount` output after mining

---

## What to capture in `output/` (general checklist)
- Install steps (your OS) + versions used
- Config used (conf file / flags)
- Commands used to start/stop node
- Proof it’s running (RPC/CLI output + logs)

## Why `2(c)` is not the same as `2(b)`
- `2(b)` proves the node is reachable and the RPC API works.
- `2(c)` becomes different when you do the wallet + mining proof, because that shows you can create blocks on the node.
- If you skip the wallet/mining part, `2(c)` is mostly the same as `2(b)` for the Bitcoin path.

<!--


































































































































-->

## Ubuntu Notes
Use the same practical, but with Linux paths and commands:

### Bitcoin Core path
```bash
bitcoind -regtest -server -txindex=1
bitcoin-cli -regtest getblockchaininfo
bitcoin-cli -regtest createwallet "labwallet"
ADDR=$(bitcoin-cli -regtest getnewaddress)
bitcoin-cli -regtest generatetoaddress 101 "$ADDR"
bitcoin-cli -regtest getblockcount
```

### Geth path
```bash
geth --dev --http --http.addr 127.0.0.1 --http.port 8545 --http.api eth,net,web3,personal,miner --verbosity 3 console
```
