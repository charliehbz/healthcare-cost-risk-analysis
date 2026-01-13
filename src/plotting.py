"""Plotting utilities for exploratory analysis and model diagnostics."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd


def plot_distributions(data: pd.DataFrame, columns: list[str]) -> None:
    """Placeholder distribution plotter."""
    data[columns].hist(figsize=(10, 6))
    plt.tight_layout()


def obs_vs_pred(y_true: pd.Series, y_pred: pd.Series) -> None:
    """Placeholder observed vs predicted plot."""
    plt.figure(figsize=(6, 6))
    plt.scatter(y_true, y_pred, alpha=0.6)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], "r--")
    plt.xlabel("Observed")
    plt.ylabel("Predicted")
    plt.tight_layout()
