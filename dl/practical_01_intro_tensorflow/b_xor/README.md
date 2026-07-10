# Practical 1(b): XOR using TensorFlow

## Full question (as given)
**Introduction to TensorFlow (OC1)**  
b. Program to solve the XOR problem.

## What this runs
- Builds a small `tf.keras` MLP
- Trains on XOR truth table
- Prints accuracy and predictions

## Description
Shows how a small neural network can learn XOR (a non-linearly separable problem) using hidden layers and non-linear activations.

## How the code works (high level)
- Creates the XOR truth table as NumPy arrays.
- Builds a `tf.keras.Sequential` model with 2 hidden layers.
- Trains with Adam + binary cross entropy.
- Prints predicted probabilities and hard 0/1 predictions for each input pair.

## Dependencies
- Python 3.10+ recommended
- TensorFlow (CPU)

## 1) One-time setup (Windows 10/11)
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

## 2) One-time setup (Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

## 3) Run (Windows 10/11)
```powershell
cd practical_01_intro_tensorflow\b_xor
py -m venv .venv
.\.venv\Scripts\activate.bat
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

### PowerShell note
If you prefer PowerShell activation, the file is `.\.venv\Scripts\Activate.ps1` (often blocked by execution policy on college PCs).

### If activation is blocked (works everywhere)
Run everything through the venv interpreter (no activation needed):
```powershell
.\.venv\Scripts\python -m pip install -U pip
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python main.py
```

## 4) Run (Ubuntu)
```bash
cd practical_01_intro_tensorflow/b_xor
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Offline/data notes
- No external data files are needed; the dataset is embedded in the code.

## Suggested improvements (optional)
- Save training loss curve to `outputs/loss.png`.
- Add early stopping to stop training once accuracy reaches 100%.
