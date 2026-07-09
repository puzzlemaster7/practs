from __future__ import annotations

import base64
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen

DEFAULT_REGTEST_URL = "http://127.0.0.1:18443"


def _default_cookie_path() -> Path | None:
    # Cookie auth is the easiest for local regtest.
    if os.name == "nt":
        localappdata = os.environ.get("LOCALAPPDATA")
        if not localappdata:
            return None
        return Path(localappdata) / "Bitcoin" / "regtest" / ".cookie"
    return Path.home() / ".bitcoin" / "regtest" / ".cookie"


def _load_cookie(cookie_path: Path) -> tuple[str, str]:
    userpass = cookie_path.read_text(encoding="utf-8").strip()
    if ":" not in userpass:
        raise ValueError("Invalid cookie format.")
    user, password = userpass.split(":", 1)
    return user, password


def _rpc_call(rpc_url: str, rpc_user: str, rpc_password: str, method: str, params: list) -> dict:
    payload = {"jsonrpc": "1.0", "id": "python", "method": method, "params": params}
    auth = base64.b64encode(f"{rpc_user}:{rpc_password}".encode("utf-8")).decode("ascii")
    req = Request(
        rpc_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Basic {auth}"},
        method="POST",
    )
    with urlopen(req, timeout=10) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw)


def main() -> None:
    rpc_url = os.environ.get("RPC_URL", DEFAULT_REGTEST_URL).strip()
    rpc_user = os.environ.get("RPC_USER", "").strip()
    rpc_password = os.environ.get("RPC_PASSWORD", "").strip()
    show_wallet_info = os.environ.get("SHOW_WALLETINFO", "").strip() == "1"

    if (not rpc_user or not rpc_password) and os.environ.get("RPC_COOKIE", "").strip():
        cookie_path = Path(os.environ["RPC_COOKIE"]).expanduser()
        rpc_user, rpc_password = _load_cookie(cookie_path)

    if (not rpc_user or not rpc_password) and os.environ.get("RPC_COOKIE", "").strip() == "":
        cookie_path = _default_cookie_path()
        if cookie_path and cookie_path.exists():
            rpc_user, rpc_password = _load_cookie(cookie_path)

    if not rpc_user or not rpc_password:
        print("Missing RPC auth. Use one of these options:")
        print("1) Cookie auth (recommended): start bitcoind regtest, then set RPC_COOKIE (optional).")
        print("   - Windows cookie: %APPDATA%\\Bitcoin\\regtest\\.cookie")
        print("   - Ubuntu cookie:  ~/.bitcoin/regtest/.cookie")
        print("2) Or set env vars: RPC_USER and RPC_PASSWORD.")
        raise SystemExit(2)

    try:
        info = _rpc_call(rpc_url, rpc_user, rpc_password, "getblockchaininfo", [])
        print("getblockchaininfo:")
        print(json.dumps(info, indent=2))

        if show_wallet_info:
            try:
                wallet_info = _rpc_call(rpc_url, rpc_user, rpc_password, "getwalletinfo", [])
                if wallet_info.get("error"):
                    print()
                    print("getwalletinfo returned error (wallet may not be loaded).")
                    print(json.dumps(wallet_info, indent=2))
                else:
                    print()
                    print("getwalletinfo:")
                    print(json.dumps(wallet_info, indent=2))
            except Exception as wallet_exc:
                print()
                print(f"getwalletinfo skipped: {wallet_exc}")
    except Exception as exc:
        raise SystemExit(f"RPC call failed: {exc}") from exc


if __name__ == "__main__":
    main()
