# Practical 8: Autoencoder using handwritten digits (offline)

## Full question (as given)
Write a program to develop Autoencoders using MNIST Handwritten Digits (OC2, OC3, OC4)

Trains an autoencoder on the `sklearn` digits dataset (8x8 images) and saves a reconstruction grid.

## Description
Implements an autoencoder for handwritten digits. The code uses `sklearn` digits to run fully offline, but the concept is the same as MNIST.

## How the code works (high level)
- Loads the digits dataset and normalizes it.
- Trains a dense autoencoder to reconstruct digit images.
- Saves an image grid of originals vs reconstructions.

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
cd practical_08_autoencoder_mnist
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
cd practical_08_autoencoder_mnist
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/digits_recon.png`

## Offline/data notes
- Fully offline (no MNIST download). If you specifically need MNIST, you can swap the loader to `tf.keras.datasets.mnist.load_data()`.

## Suggested improvements (optional)
- Add latent-space visualization (t-SNE/UMAP) of the encoder output.
- Save the model file to `outputs/autoencoder.keras`.
