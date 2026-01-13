# Reproducibility Guide

## Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## Install requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Launch Jupyter and run notebooks

```bash
jupyter notebook
```

Open the notebooks in the `notebooks/` directory and run them top to bottom.

## Dataset

Download the dataset and save it as `data/insurance.csv`. Do not commit the dataset file.
