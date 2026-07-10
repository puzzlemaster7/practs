# Practical 4: Image Segmentation (U-Net on synthetic data)

## Full question (as given)
Write a program to implement deep learning Techniques for image segmentation. (OC2, OC3, OC4)

Trains a small U-Net-like model on a **synthetic segmentation dataset** (random circles/rectangles). No external dataset download required.

## Description
Builds and trains a small U-Net style CNN to segment foreground shapes from background on generated images.

## How the code works (high level)
- Generates training images and binary masks (circles/rectangles).
- Builds a lightweight U-Net-like model (downsampling + upsampling + skip connections).
- Trains using binary cross-entropy.
- Saves a grid of input / ground-truth mask / predicted mask.

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
cd practical_04_image_segmentation
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
cd practical_04_image_segmentation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/sample_predictions.png`

## Offline/data notes
- Uses generated synthetic data only; runs fully offline.

## Suggested improvements (optional)
- Add IoU/Dice metric printing for evaluation.
- Save model weights to `outputs/unet.keras`.
