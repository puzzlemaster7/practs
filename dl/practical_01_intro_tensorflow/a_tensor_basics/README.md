# Practical 1(a): Tensor basics in TensorFlow

## Full question (as given)
**Introduction to TensorFlow (OC1)**  
a.  
- Create tensors with different shapes and data types.  
- Perform basic operations like addition, subtraction, multiplication, and division on tensors.  
- Reshape, slice, and index tensors to extract specific elements or sections.  
- Performing matrix multiplication and finding eigenvectors and eigenvalues using TensorFlow

## What this runs
- Creates tensors of different shapes/dtypes
- Basic ops: add/sub/mul/div
- Reshape, slice, index
- Matrix multiplication
- Eigenvalues + eigenvectors

## Description
Demonstrates common TensorFlow tensor operations and linear algebra APIs (`tf.linalg`), printing results to the terminal.

## How the code works (high level)
- Uses `tf.constant`, `tf.ones`, and `tf.range` to create tensors.
- Uses Python operators (`+ - * /`) which map to TensorFlow ops.
- Uses `tf.reshape` and standard slicing/indexing to access tensor parts.
- Uses `tf.matmul` for matrix multiplication.
- Uses `tf.linalg.eigh` (symmetric eigendecomposition) to get eigenvalues/eigenvectors.

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
1) Install Python + venv:
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
python3 --version
```

## 3) Run (Windows 10/11)
```powershell
cd practical_01_intro_tensorflow\a_tensor_basics
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
cd practical_01_intro_tensorflow/a_tensor_basics
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
python main.py
```

## Notes
- Output is printed in the terminal.
- This practical is fully offline (no dataset downloads).

## Suggested improvements (optional)
- Add a `--save` option to write outputs to a text file for journal submission.
- Add a small unit test file to validate expected tensor shapes/values.
