# Practical 3(e): DApp with Angular + Truffle + Ganache CLI

## Full question (as given)
**DApp Development (OC3)**  
e. Build a decentralized application (DApp) using Angular for the front end and Truffle along with Ganache CLI for the back end.

## What this contains
- `backend/`: Truffle project for contract deployment
- `frontend/`: Angular app for UI interaction

## Description
End-to-end DApp workflow: local blockchain (Ganache) + contract deployment (Truffle) + UI interaction (Angular).

## Dependencies
- Node.js LTS
- `npm` and `npx` (included with Node.js)
- Internet for the first `npm install`

## Software required
- **Node.js LTS**
- No global Truffle/Ganache install needed
- Angular CLI is needed for the frontend part of the practical
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
Use the backend folder for the blockchain part:

**Terminal 1**
```powershell
cd G:\block_chain_practicals\practical_03\e_dapp_angular_truffle_ganache\backend
npm install
npx ganache -p 8545
```
If `npx` is not recognized, use:
```powershell
& "$env:ProgramFiles\nodejs\npx.cmd" ganache -p 8545
```

**Terminal 2**
```powershell
cd G:\block_chain_practicals\practical_03\e_dapp_angular_truffle_ganache\backend
npx truffle compile
npx truffle migrate --network development --reset
```

Use `--reset` when you want a fresh redeploy on the local Ganache chain.

Note: the `µWS` warning from Ganache/Truffle on some Windows + Node versions is normal. Truffle falls back to the Node.js implementation and deployment can still succeed.

## Frontend
Run the Angular UI and connect it to the local Ganache/Truffle backend.
The frontend uses the deployed `SimpleStorage` contract and reads the stored value from Ganache.

**Frontend steps**
```powershell
cd G:\block_chain_practicals\practical_03\e_dapp_angular_truffle_ganache\frontend
npm install
npx ng serve
```
Open the app at `http://localhost:4200`.

### Frontend contract setup
1) Keep Ganache running on `127.0.0.1:8545`.
2) After `truffle migrate`, copy the deployed contract address from the backend output.
3) Update `frontend\src\app\app.component.ts`:
   - `rpcUrl`
   - `contractAddress`
4) Open the app and click **Load stored value** to verify the contract read works.
5) Enter a whole number and click **Send transaction** to write to the deployed contract through the local Ganache RPC.
6) If you redeploy with `truffle migrate --reset`, update the frontend contract address again.

Note: this exam-friendly version uses the Ganache RPC directly for both read and write, so MetaMask is not required.

## Output notes
- Save backend deployment and frontend UI screenshots/logs in `output/`.
- No helper scripts are needed for the exam.

<!--



















































































-->

## Ubuntu notes
Backend commands are the same, but paths use `/`:
```bash
cd practical_03/e_dapp_angular_truffle_ganache/backend
npm install
npx ganache -p 8545
```
Then in Terminal 2:
```bash
cd practical_03/e_dapp_angular_truffle_ganache/backend
npx truffle compile
npx truffle migrate --network development --reset
```

