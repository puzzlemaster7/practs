# Pinned / Recommended Versions

These are the versions this repo is structured around (you can use newer versions, but if something breaks, align to these).

## Python practicals
- Python: 3.10+ (tested with 3.11 locally)

## Solidity / Truffle practicals
- Node.js: LTS (18+ recommended)
- Truffle: declared in each practical `package.json`
- Ganache: declared in each practical `package.json`
- solc: 0.8.20 (set in each `truffle-config.js`)

## Bitcoin Core practicals
- Bitcoin Core: any recent release that supports `regtest` + cookie auth

## Geth practicals
- Geth: any recent release with `--dev` and HTTP-RPC support

## Iroha practical
- Docker: Desktop/Engine with `docker compose`
- Iroha image: `hyperledger/iroha2:stable-2.0.0-pre-rc.20`
