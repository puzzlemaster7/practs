# Practical 6: Autoencoder on real-world data (sklearn digits)

## Full question (as given)
Applying the Autoencoder algorithms for encoding real-world data (OC2, OC3, OC4)

Uses the `sklearn` digits dataset (8x8 grayscale images), trains a dense autoencoder, and saves reconstruction examples.

## Description
Learns a compact representation (“encoding”) of digit images by training a network to reconstruct its input.

## How the code works (high level)
- Loads the `sklearn` digits dataset and normalizes pixel values.
- Builds an encoder (Dense layers down to a small latent size) and a decoder (Dense layers back to original size).
- Trains with MSE reconstruction loss.
- Saves a grid comparing original images vs reconstructions.

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
cd practical_06_autoencoder_realworld
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
cd practical_06_autoencoder_realworld
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/reconstructions.png`

## Offline/data notes
- `sklearn` digits ships with scikit-learn; no internet/data download required.

## Suggested improvements (optional)
- Use a convolutional autoencoder instead of dense layers.
- Add PCA comparison (latent vectors vs PCA components).
