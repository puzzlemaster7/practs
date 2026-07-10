# Practical 3(b): Multiclass classification (2 hidden layers)

## Full question (as given)
**Convolutional Neural Networks (Classification) (OC2, OC3, OC4)**  
b. Using a deep feed-forward network with two hidden layers for performing multiclass classification and predicting the class.

## What this runs
- Creates a synthetic 3-class dataset (`make_blobs`)
- Trains a feed-forward network with two hidden layers
- Prints test accuracy + confusion matrix and saves a plot

## Description
Demonstrates multiclass classification using a dense neural network with two hidden layers and a softmax output.

## How the code works (high level)
- Generates a 2D, 3-class dataset via `sklearn.datasets.make_blobs`.
- Standardizes features with `StandardScaler`.
- Trains a dense network with `softmax` output and `sparse_categorical_crossentropy` loss.
- Computes confusion matrix and saves it as an image.

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
cd practical_03_cnn_classification\b_multiclass_classification
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
cd practical_03_cnn_classification/b_multiclass_classification
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- `outputs/confusion_matrix.png`

## Offline/data notes
- Uses generated synthetic data only; runs fully offline.

## Suggested improvements (optional)
- Save the trained model to `outputs/model.keras`.
- Add a small function to predict the class for a custom input point.
