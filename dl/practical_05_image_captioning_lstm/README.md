# Practical 5: Image Captioning with LSTM (toy example)

## Full question (as given)
Write a program to predict a caption for a sample image using LSTM. (OC2, OC3, OC4)

This is a **small, offline, toy** image-captioning demo:
- Generates a tiny dataset of synthetic images (colored shapes)
- Trains a CNN encoder + LSTM decoder
- Predicts a caption for a sample image

This is meant for learning the pipeline, not for high accuracy on real datasets.

## Description
Implements a minimal “encoder-decoder” captioning pipeline: a CNN encodes an image into a feature vector and an LSTM decodes a short caption token-by-token.

## How the code works (high level)
- Creates a tiny vocabulary (`red/green/blue`, `square/circle` plus special tokens).
- Generates synthetic images (colored shapes) and matching captions (e.g., `"red circle"`).
- Trains with teacher forcing: model predicts the next token in the sequence.
- Uses greedy decoding to generate a caption for a new sample image and prints it.

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
cd practical_05_image_captioning_lstm
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
cd practical_05_image_captioning_lstm
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- Terminal: training loss + predicted caption
- `outputs/sample_image.png`

## Offline/data notes
- No external dataset download; synthetic images are generated in code.

## Suggested improvements (optional)
- Replace greedy decoding with beam search.
- Save a few training examples + predictions to `outputs/` for your journal.
