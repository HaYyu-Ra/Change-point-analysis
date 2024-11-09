import unittest
import os
import pandas as pd
from your_module import (
    load_data,
    fetch_economic_data,
    merge_data_with_oil_prices,
    eda,
    change_point_detection,
    time_series_modeling,
    analyze_economic_factors,
    lstm_forecasting,
)


class TestBrentOilAnalysis(unittest.TestCase):

    def test_load_data(self):
        data = load_data()
        self.assertTrue(isinstance(data, pd.DataFrame))
        self.assertIn("Price", data.columns)

    def test_fetch_economic_data(self):
        economic_data = fetch_economic_data()
        self.assertTrue(isinstance(economic_data, pd.DataFrame))
        self.assertIn("GDP_Growth", economic_data.columns)

    def test_merge_data_with_oil_prices(self):
        oil_data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        economic_data = pd.DataFrame(
            {"GDP_Growth": [2.1, 2.3, 2.2]},
            index=pd.date_range("2020-01-01", periods=3),
        )
        merged_data = merge_data_with_oil_prices(oil_data, economic_data)
        self.assertEqual(merged_data.shape[1], 2)  # Ensure 2 columns after merge

    def test_eda(self):
        data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        # Testing EDA (could check print statements, or visualization if needed)

    def test_change_point_detection(self):
        data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        change_points = change_point_detection(data)
        self.assertTrue(isinstance(change_points, list))

    def test_time_series_modeling(self):
        data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        model = time_series_modeling(data)
        self.assertTrue(hasattr(model, "summary"))

    def test_analyze_economic_factors(self):
        data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        economic_data = pd.DataFrame(
            {"GDP_Growth": [2.1, 2.3, 2.2]},
            index=pd.date_range("2020-01-01", periods=3),
        )
        merged_data = merge_data_with_oil_prices(data, economic_data)
        analyze_economic_factors(merged_data)  # No return, just ensures it runs

    def test_lstm_forecasting(self):
        data = pd.DataFrame(
            {"Price": [50, 55, 60]}, index=pd.date_range("2020-01-01", periods=3)
        )
        lstm_forecasting(data)  # Ensure no errors occur during LSTM forecasting


if __name__ == "__main__":
    unittest.main()
