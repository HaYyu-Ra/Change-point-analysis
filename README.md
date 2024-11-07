# 10 Academy: Artificial Intelligence Mastery - Week 10 Challenge

Change Point Analysis and Statistical Modeling of Time Series Data

# Project Overview

This project focuses on analyzing Brent oil price data to identify significant events that impact price fluctuations and to model these changes statistically. Using historical data and a robust time series modeling approach, the goal is to assist stakeholders—including investors, analysts, and policymakers—in understanding and responding to price changes caused by geopolitical, economic, and policy-related events.

# Business Objective

The primary objective is to detect changes in Brent oil prices due to key events like political decisions, conflicts in oil-producing regions, global economic sanctions, and changes in OPEC policies. By understanding the effects of these events, the project aims to provide actionable insights for:

# Investment strategies that optimize returns

Policy formulation that enhances economic stability.
Operational planning for energy companies to manage costs and secure supply chains.
Project Scope and Key Responsibilities
Identify Significant Events: Detect events that have historically impacted Brent oil prices.
Quantify Event Impact: Assess how specific events influence price fluctuations.
Deliver Data-Driven Insights: Generate actionable recommendations for investment, policy-making, and business planning.

# Data Summary

Source: Historical Brent oil price records from May 20, 1987, to September 30, 2022.
Data Fields:
Date: The date of the recorded price.
Price: Brent oil price in USD per barrel.

# Analytical Workflow

# Data Collection: Gather Brent oil price data and associated event information from credible sources

# Data Cleaning: Address missing values, format dates, and ensure consistency

# Exploratory Data Analysis (EDA): Visualize trends, correlations, and patterns between prices and significant events

Change Point Detection: Apply Bayesian Change Point Detection to identify shifts in price patterns.

# Statistical Modeling: Use models like ARIMA, GARCH, and Bayesian Structural Time Series for predictive analysis

Validation: Evaluate model accuracy with metrics such as AIC, BIC, and residual analysis.
Reporting: Summarize findings and insights using React dashboard templates and visualizations.

# Time Series Models Used

ARIMA (AutoRegressive Integrated Moving Average): Captures trends and seasonality for reliable forecasting.
GARCH (Generalized Autoregressive Conditional Heteroskedasticity): Models volatility clustering in financial time series.
Bayesian Change Point Detection: Provides a probabilistic framework to identify shifts in price trends due to external events.
Key Assumptions and Limitations
Assumptions: Stationarity in time series data, independence of exogenous variables.
Limitations: Data quality, unrecorded events, and unpredictability of global markets.

# Project Progress

As of this interim report, the following milestones have been completed:

Data Acquisition: Successfully obtained historical Brent oil price data, with preliminary data cleaning underway.
Exploratory Data Analysis (EDA): Initial trend visualizations and statistical summaries are complete.
Event Identification: A preliminary list of significant events impacting Brent oil prices has been compiled.
Change Point Detection Framework: Initial testing on simulated data validates the Bayesian Change Point Detection methodology.
Model Selection: Ongoing evaluation of time series models (ARIMA, GARCH, Bayesian Structural Time Series) to determine the best fit for the data.
Documentation: Analysis processes and findings are being systematically documented.

# Conclusion

This report establishes a structured workflow for analyzing Brent oil prices in relation to significant political and economic events. Through this analysis, we aim to offer valuable insights that aid stakeholders in navigating the complexities of the oil market.

# Repository Structure

data/: Contains the dataset used for analysis.
notebooks/: Jupyter notebooks documenting the EDA, change point detection, and modeling steps.
src/: Source code for data processing, model training, and evaluation.
reports/: Documentation of findings and interim reports.
dashboard/: Code for the React dashboard visualizing key results.
Getting Started
Clone the Repository:
bash
Copy code
git clone <https://github.com/HaYyu-Ra/Change-point-analysis.git>
cd Change-point-analysis
Install Dependencies:
Use requirements.txt to install required packages:

bash
Copy code
pip install -r requirements.txt
Run Notebooks:
Execute the Jupyter notebooks in notebooks/ to reproduce the analysis.

# References

Data Science Workflow: Data Science PM, Towards Data Science, KnowledgeHut, Medium Codex.
Change Point Analysis: Washington State University, Jagota Arun, Towards Data Science.
Bayesian Change Point Detection: Bayesian Changepoint Detection with PyMC3.
Bayesian Inference and MCMC: Introduction to Bayesian Statistics, MCMC for Probability.
Alternative Data Sources: Petroleum Trade - Imports from OPEC, Energy Consumption - Transportation Sector.
React Dashboard Templates: Flatlogic React Dashboard, Light Bootstrap Dashboard React, CoreUI Free React Admin Template.
