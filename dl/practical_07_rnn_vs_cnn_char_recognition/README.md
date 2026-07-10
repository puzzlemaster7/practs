# Practical 7: Character recognition using RNN vs CNN (offline digits)

## Full question (as given)
Write a program for character recognition using RNN and compare it with CNN. (OC2, OC3, OC4)

## Description
Compares a CNN and an RNN on handwritten character-like data. To keep the practical fully offline, it uses the `sklearn` digits dataset (8x8 images).

## How the code works (high level)
- Loads `sklearn.datasets.load_digits()` and splits into train/test.
- CNN model: treats the image as a 2D grid and learns spatial filters (Conv2D).
- RNN model: treats the image as a sequence of rows (each row is one timestep) using a GRU.
- Trains both models for a few epochs and prints test accuracies.

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
cd practical_07_rnn_vs_cnn_char_recognition
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
cd practical_07_rnn_vs_cnn_char_recognition
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Output
- Terminal: CNN test accuracy, RNN test accuracy

## Offline/data notes
- `sklearn` digits ships with scikit-learn; no internet/data download required.

## Suggested improvements (optional)
- Save confusion matrices for both models.
- Increase epochs and add early stopping for better accuracy.
