# Practical 2: Linear Regression (TensorFlow)

## Full question (as given)
**Linear Regression (OC2, OC3, OC4)**  
a.  
- Implement a simple linear regression model using TensorFlow's low-level API (or `tf.keras`).  
- Train the model on a toy dataset (e.g., housing prices vs. square footage).  
- Visualize the loss function and the learned linear relationship.  
- Make predictions on new data points.

Implements linear regression using `tf.keras`, trains on a toy dataset (house area vs price), saves plots, and prints predictions.

See `requirements.txt` and run instructions below.

## Description
Trains a single-neuron model to learn `price ≈ w * sqft + b` on a small toy housing dataset stored locally as CSV.

## How the code works (high level)
- Loads `data/housing_toy.csv` into NumPy arrays.
- Builds a `tf.keras.Sequential` model with one `Dense(1)` layer.
- Trains using MSE loss (mean squared error).
- Saves:
  - Loss curve (`outputs/loss_curve.png`)
  - Scatter plot + learned regression line (`outputs/fit_line.png`)
- Runs predictions for a few new square-footage values.

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

## 2) Run (Windows 10/11)
```powershell
cd practical_02_linear_regression
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

## 3) One-time setup (Ubuntu)
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

## 4) Run (Ubuntu)
```bash
cd practical_02_linear_regression
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Outputs
- Terminal: final loss, learned weights, predictions
- Files in `outputs/`:
  - `loss_curve.png`
  - `fit_line.png`

## Offline/data notes
- The dataset is included as `data/housing_toy.csv`, so this practical runs fully offline.

## Suggested improvements (optional)
- Add a CLI argument to choose a different CSV (keep same column names).
- Add a `report.md` template that embeds the generated plots for submission.
