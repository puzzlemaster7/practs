# Practical 4(b): Demonstration on Interacting with NFT

## Full question (as given)
**NFT (OC4)**  
b. Demonstration on interacting with NFT.

## What this is
This is a local ERC-721 interaction using Ganache + Truffle.

## Description
Demonstrates minting, reading ownership, approving, and transferring an NFT.

## Software required
- **Node.js LTS**
- **Ganache CLI**
- **Truffle**
- `npx` comes with Node.js and is used to run both tools

## Recommended workflow
Use a local chain so the whole practical can be reproduced on a fresh machine without any external wallet or testnet setup.

### 1) Install dependencies
Open a terminal in `code` and run:
```bash
npm install
```

### 2) Start Ganache
Terminal 1:
```bash
npx ganache -p 8545
```

### 3) Compile and deploy
Terminal 2:
```bash
npx truffle compile
npx truffle migrate --network development
```

### 4) Interact from Truffle console
```bash
npx truffle console --network development
```

Then run:
```javascript
const nft = await BasicNFT.deployed()
const accounts = await web3.eth.getAccounts()
await nft.mint(accounts[0], 1, { from: accounts[0] })
await nft.ownerOf(1)
await nft.approve(accounts[1], 1, { from: accounts[0] })
await nft.transferFrom(accounts[0], accounts[1], 1, { from: accounts[1] })
await nft.ownerOf(1)
```

## Expected result
- NFT contract deploys successfully
- Token `1` is minted to the first Ganache account
- `ownerOf(1)` returns the first account
- Approval succeeds
- Transfer succeeds
- `ownerOf(1)` returns the second account

## What to capture in `output/`
- Ganache startup
- Truffle compile
- Truffle migrate
- Console mint / owner / transfer proof

## Windows notes
- Use PowerShell or Command Prompt.
- If `npx` is not found, use the full Node.js path to `npx.cmd`.

## Ubuntu notes
- Install `nodejs` and `npm`.
- Run the same `npx` commands from a terminal.
