import unittest
import os
import pandas as pd
from unittest.mock import patch, MagicMock
from datetime import datetime
from your_module import (
    load_data,
    download_data,
    fetch_economic_data,
    merge_data_with_oil_prices,
    eda,
    change_point_detection,
    time_series_modeling,
    analyze_economic_factors,
    lstm_forecasting,
)


class TestBrentOilAnalysis(unittest.TestCase):

    @patch("your_module.pd.read_csv")
    def test_load_data_existing_file(self, mock_read_csv):
        # Mock the read_csv method to return a DataFrame
        mock_read_csv.return_value = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test load_data when file exists
        data = load_data()
        mock_read_csv.assert_called_once_with(
            "C:/Users/hayyu.ragea/AppData/Local/Programs/Python/Python312/Change point analysis/data/processed/cleaned_brent_oil_prices.csv",
            index_col="Date",
            parse_dates=True,
        )
        self.assertEqual(len(data), 2)

    @patch("your_module.yf.download")
    def test_download_data(self, mock_download):
        # Mock yf.download to return a fake dataset
        mock_download.return_value = pd.DataFrame(
            {"Close": [50, 60], "Open": [51, 61], "High": [52, 62], "Low": [49, 59]},
            index=pd.to_datetime(["2022-01-01", "2022-01-02"]),
        )

        # Test the download_data function
        data = download_data()
        self.assertEqual(data["Price"].iloc[0], 50)
        self.assertEqual(data["Price"].iloc[1], 60)

    @patch("your_module.Fred.get_series")
    def test_fetch_economic_data(self, mock_get_series):
        # Mock the API response for economic data
        mock_get_series.return_value = pd.Series(
            [2.0, 3.0], index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test fetch_economic_data
        economic_data = fetch_economic_data()
        self.assertEqual(economic_data.shape, (2, 4))
        self.assertIn("GDP_Growth", economic_data.columns)

    def test_merge_data_with_oil_prices(self):
        # Test merge_data_with_oil_prices function
        oil_data = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )
        economic_data = pd.DataFrame(
            {
                "GDP_Growth": [2.0, 3.0],
                "Inflation": [1.5, 1.7],
                "Unemployment": [5.0, 5.1],
                "USD_Index": [90, 91],
            },
            index=pd.to_datetime(["2022-01-01", "2022-01-02"]),
        )

        merged_data = merge_data_with_oil_prices(oil_data, economic_data)
        self.assertEqual(len(merged_data), 2)
        self.assertIn("GDP_Growth", merged_data.columns)

    @patch("matplotlib.pyplot.show")
    def test_eda(self, mock_show):
        # Create a dummy dataset for testing EDA
        data = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test EDA function (ensure it runs without errors)
        eda(data)
        mock_show.assert_called_once()

    @patch("ruptures.Binseg.predict")
    def test_change_point_detection(self, mock_predict):
        # Mock the prediction of change points
        mock_predict.return_value = [1]

        data = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test the change point detection
        change_points = change_point_detection(data)
        mock_predict.assert_called_once()
        self.assertEqual(change_points, [1])

    @patch("statsmodels.tsa.arima.model.ARIMA.fit")
    def test_time_series_modeling(self, mock_fit):
        # Mock ARIMA model fitting
        mock_fit.return_value = MagicMock()
        mock_fit.return_value.forecast.return_value = [55, 57]

        data = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test time_series_modeling
        fitted_model = time_series_modeling(data)
        mock_fit.assert_called_once()
        self.assertEqual(len(fitted_model.forecast(steps=2)), 2)

    @patch("statsmodels.api.OLS")
    def test_analyze_economic_factors(self, mock_OLS):
        # Mock regression analysis
        mock_OLS.return_value.fit.return_value.summary.return_value = "summary"

        merged_data = pd.DataFrame(
            {
                "Price": [50, 60],
                "GDP_Growth": [2.0, 3.0],
                "Inflation": [1.5, 1.7],
                "Unemployment": [5.0, 5.1],
                "USD_Index": [90, 91],
            }
        )

        # Test analyze_economic_factors
        analyze_economic_factors(merged_data)
        mock_OLS.assert_called_once()

    @patch("keras.models.Sequential.fit")
    def test_lstm_forecasting(self, mock_fit):
        # Mock the LSTM model fitting
        mock_fit.return_value = None

        data = pd.DataFrame(
            {"Price": [50, 60]}, index=pd.to_datetime(["2022-01-01", "2022-01-02"])
        )

        # Test lstm_forecasting
        lstm_forecasting(data)
        mock_fit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
