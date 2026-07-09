# NFT Practical (4b)

Use the files in this folder to run a local NFT interaction demo.

## Files
- `contracts/BasicNFT.sol` — minimal NFT contract with mint, approve, transfer, and owner lookup
- `migrations/1_deploy.js` — deploys the NFT contract
- `truffle-config.js` — points Truffle to the local Ganache RPC

## Run order
1. Open `code` in a terminal.
2. Run `npm install` once.
3. Start Ganache with `npx ganache -p 8545`.
4. In a second terminal run `npx truffle compile` and `npx truffle migrate --network development`.
5. Open `npx truffle console --network development` and mint / approve / transfer the token.

## Expected proof
- Contract deployment address
- Token mint transaction hash
- `ownerOf(1)` before transfer
- `ownerOf(1)` after transfer
