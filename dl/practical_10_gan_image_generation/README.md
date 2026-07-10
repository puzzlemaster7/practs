# Practical 10: GAN for image generation (offline digits)

## Full question (as given)
Applying Generative Adversarial Networks for image generation and unsupervised tasks. (OC2, OC3, OC4)

Trains a simple GAN on the `sklearn` digits dataset (8x8 images) and saves a grid of generated images.

## Description
Trains two networks:
- Generator: creates fake digit-like images from random noise
- Discriminator: predicts whether an image is real or fake

## How the code works (high level)
- Loads digits images and scales them to `[-1, 1]` for `tanh` generator output.
- Alternates between:
  - training the discriminator to classify real vs fake images
  - training the generator to fool the discriminator
- Saves a grid of generated samples to `outputs/generated_grid.png`.

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
cd practical_10_gan_image_generation
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
cd practical_10_gan_image_generation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/generated_grid.png`

## Offline/data notes
- `sklearn` digits ships with scikit-learn; no internet/data download required.

## Suggested improvements (optional)
- Use DCGAN (conv layers) for higher-quality samples.
- Save intermediate grids every N steps for your journal.
