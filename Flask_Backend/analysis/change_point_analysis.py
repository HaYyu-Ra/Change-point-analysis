# analysis/change_point_analysis.py
import pandas as pd
import numpy as np
from scipy.stats import zscore


def detect_change_points(data, threshold=2):
    """
    Detects significant changes in Brent oil price data.
    """
    data["Price_Z"] = zscore(data["Price"])
    data["Change_Point"] = np.where(data["Price_Z"].abs() > threshold, 1, 0)
    return data
