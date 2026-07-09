# Practical 3(c): Contracts, Inheritance, Constructors, Abstract, Interfaces

## Full question (as given)
**Solidity / Smart Contracts (OC3)**  
c. Write a Solidity program that demonstrates various features including contracts, inheritance, constructors, abstract contracts, interfaces.

## What this contains
- Interface definition + implementation
- Abstract contract + derived contract
- Constructor chaining

## Description
Demonstrates OOP-like features in Solidity: inheritance, interfaces, and abstract contracts.

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
cd G:\block_chain_practicals\practical_03\c_oop_features_inheritance_interfaces
npm install
npx ganache -p 8545
```
If `npx` is not recognized, use:
```powershell
& "$env:ProgramFiles\nodejs\npx.cmd" ganache -p 8545
```

**Terminal 2**
```powershell
cd G:\block_chain_practicals\practical_03\c_oop_features_inheritance_interfaces
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

## Ubuntu notes
Commands are the same, but paths use `/`:
```bash
cd practical_03/c_oop_features_inheritance_interfaces
npm install
npx ganache -p 8545
```
Then in Terminal 2:
```bash
cd practical_03/c_oop_features_inheritance_interfaces
npx truffle compile
npx truffle migrate --network development --reset
```
