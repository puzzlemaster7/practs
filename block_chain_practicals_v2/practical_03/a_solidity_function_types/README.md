# Practical 3(a): Solidity Function Types + Fallback

## Full question (as given)
**Solidity / Smart Contracts (OC3)**  
a. Write a Solidity program that demonstrates various types of functions including regular functions, view functions, pure functions, and the fallback function.

## What this contains
- Regular (state-changing) function
- `view` function
- `pure` function
- `receive()` and `fallback()`

## Description
Demonstrates common Solidity function types and how contracts behave when receiving ETH or unknown calldata.

## How the code works (high level)
- `setValue(...)` updates state.
- `getValue()` reads state (`view`).
- `add(...)` computes without state (`pure`).
- `receive()` handles plain ETH transfers.
- `fallback()` handles unknown function calls.

## Dependencies
- Node.js LTS
- `npm` and `npx` (included with Node.js)
- Internet for the first `npm install`

## Software required
- **Node.js LTS**
- No global Truffle/Ganache install needed
- `npx` comes with Node.js and is used to run `ganache` and `truffle`

## Reference
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

## 1) One-time setup (Windows 10/11)
1) Install **Node.js LTS**
2) Verify in PowerShell:
```powershell
node -v
npm -v
```
3) Verify `npx`:
```powershell
npx -v
```

## 2) Manual exam steps
Open two terminals in the practical folder:

**Terminal 1**
```powershell
cd G:\block_chain_practicals\practical_03\a_solidity_function_types
npm install
npx ganache -p 8545
```
If `npx` is not recognized, use:
```powershell
& "$env:ProgramFiles\nodejs\npx.cmd" ganache -p 8545
```

**Terminal 2**
```powershell
cd G:\block_chain_practicals\practical_03\a_solidity_function_types
npx truffle compile
npx truffle migrate --network development --reset
```

Use `--reset` when you want a fresh redeploy on the local Ganache chain.

Note: the `µWS` warning from Ganache/Truffle on some Windows + Node versions is normal. Truffle falls back to the Node.js implementation and deployment can still succeed.

## Output notes
- Save compilation/deployment screenshots/logs in `output/`.
- No helper scripts are needed for the exam.

<!--


































































































































-->
