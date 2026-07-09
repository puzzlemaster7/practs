# Hyperledger Iroha (Docker) - Lab Notes

This practical is designed to be reproducible and easy to clean up.

## What’s included
- `docker-compose.yml` starts an Iroha 2 container and exposes port `8080`.

## How to run
From this folder:
```bash
docker compose up -d
docker compose ps -a
docker logs iroha2_lab --tail 50
```

## Current limitation
The compose file mounts `iroha.toml`; if the container exits, update that config to match the image requirements.

## Clean up
From this folder:
```bash
docker compose down -v
```
