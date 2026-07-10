# Practical 9: RNN sequence analysis for stock-price-like data (offline)

## Full question (as given)
Demonstrate recurrent neural network that learns to perform sequence analysis for stock price. (google stock price) (OC2, OC3, OC4)

The original practical mentions Google stock prices; to keep this runnable on any machine **without web downloads**, this practical:
- Generates a stock-price-like time series (trend + seasonality + noise)
- Trains an LSTM to predict the next value from a lookback window
- Saves a plot of predictions vs actual values

## Description
Shows sequence modeling: given the last `lookback` timesteps, predict the next value.

## How the code works (high level)
- Creates a synthetic time series (trend + sine waves + noise).
- Builds supervised samples using a sliding window.
- Trains an LSTM to predict the next timestep value.
- Saves a plot comparing predicted vs actual values on the test split.

## Setup (Windows 10/11)
### 1) One-time setup (Windows 10/11)
1) Install **Python 3.x** (3.10+ recommended). In the installer, enable:
   - “Install `py` launcher”
   - “Add Python to PATH”
2) Verify in PowerShell:
```powershell
py -V
py -c "import sys; print(sys.executable)"
```
3) If venv activation is blocked, run once:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 2) Run (Windows 10/11)
```powershell
cd practical_09_rnn_stock_sequence
py -m venv .venv
.\.venv\Scripts\activate.bat
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

### PowerShell note
If you prefer PowerShell activation, the file is `.\.venv\Scripts\Activate.ps1` (often blocked by execution policy on college PCs).

### If activation is blocked (works everywhere)
```powershell
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

## Setup (Ubuntu)
### 3) One-time setup (Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

### 4) Run (Ubuntu)
```bash
cd practical_09_rnn_stock_sequence
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/pred_vs_actual.png`

## Offline/data notes
- Fully offline by design. If you want real Google stock prices offline, place a CSV in `data/` and load from it (recommended).

## Suggested improvements (optional)
- Add MinMax scaling and inverse-transform for clearer plots.
- Add MAE metric and compare with a naive baseline (last value).
