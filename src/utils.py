"""Utility helpers for data loading and evaluation."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd


def load_data(path: str | Path) -> pd.DataFrame:
    """Load the insurance dataset from a CSV path."""
    return pd.read_csv(path)


def train_test_split(
    data: pd.DataFrame, test_size: float = 0.2, random_state: int | None = None
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Placeholder split helper (replace with sklearn in later iterations)."""
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")
    if random_state is not None:
        data = data.sample(frac=1, random_state=random_state)
    split_index = int(len(data) * (1 - test_size))
    return data.iloc[:split_index], data.iloc[split_index:]


def rmse(y_true: pd.Series, y_pred: pd.Series) -> float:
    """Compute root mean squared error between two Series."""
    return ((y_true - y_pred) ** 2).mean() ** 0.5
