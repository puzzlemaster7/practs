# Practical 4(a): Install + Demonstrate Hyperledger Iroha

## Full question (as given)
**Permissioned Blockchain (OC4)**  
a. Install and demonstrate use of Hyperledger Iroha.

## What this is
This practical uses the official single-node `iroha3-dev` sample bundle from the upstream repo.

## Software required
- **Docker Desktop**
- **Docker Compose**

## Reference
- Official repo: `https://github.com/hyperledger-iroha/iroha`
- Tool installation guide: `G:\block_chain_practicals\TOOLS_SETUP.md`
- Version notes: `G:\block_chain_practicals\VERSIONS.md`

## Local execution (Docker)
The `code/` folder now contains the official single-node sample bundle:
- `docker-compose.yml`
- `config.toml`
- `genesis.json`

### 1) One-time setup
- Install **Docker Desktop** on Windows 10/11
- Verify:
```bash
docker --version
docker compose version
```

### 2) Start Iroha
```bash
cd practical_04/a_hyperledger_iroha_demo/code
docker compose up -d
docker compose ps -a
docker logs iroha-iroha3-dev --tail 50
```
The sample uses the official `hyperledger/iroha:latest` image and the bundled `irohad --sora` command.

### 3) Proof of interaction
At minimum, capture:
- `docker compose ps -a`
- `docker logs iroha-iroha3-dev --tail 50`
- a reachable status endpoint if available

### 4) Stop + clean removal
```bash
cd practical_04/a_hyperledger_iroha_demo/code
docker compose down -v
```

## What to capture in `output/`
- Docker install/config proof
- `docker compose up -d`
- `docker compose ps -a`
- peer logs or status proof

## Ubuntu notes
- Install **Docker Engine + Docker Compose**
- Use the same commands as above
