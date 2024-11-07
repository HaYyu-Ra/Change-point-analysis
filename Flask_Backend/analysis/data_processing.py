# analysis/data_processing.py
import pandas as pd


def load_brent_data(file_path):
    return pd.read_csv(file_path)


def load_events_data(file_path):
    return pd.read_csv(file_path)


def load_merged_data(file_path):
    return pd.read_csv(file_path)
