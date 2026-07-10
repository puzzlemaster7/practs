# Practical 3(a): Binary classification (deep neural network)

## Full question (as given)
**Convolutional Neural Networks (Classification) (OC2, OC3, OC4)**  
a. Implementing deep neural network for performing binary classification task

## What this runs
- Creates a synthetic binary dataset (`make_moons`)
- Trains a small deep network
- Prints accuracy + saves a decision boundary plot

## Description
Demonstrates a deep feed-forward network performing binary classification on a non-linear dataset.

## How the code works (high level)
- Generates a 2D dataset with `sklearn.datasets.make_moons`.
- Standardizes features with `StandardScaler`.
- Trains a dense neural network with ReLU activations.
- Evaluates on a held-out test set and saves a decision boundary visualization.

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
cd practical_03_cnn_classification\a_binary_classification
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
cd practical_03_cnn_classification/a_binary_classification
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/decision_boundary.png`

## Offline/data notes
- Uses generated synthetic data only; runs fully offline.

## Suggested improvements (optional)
- Save training curves (loss/accuracy) to `outputs/`.
- Add command-line arguments for epochs and learning rate.
