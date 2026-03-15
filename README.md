# 🌾 General Mills (GIS) Stock Direction Predictor

## Project Overview
Predicts whether General Mills (GIS) stock will go UP or DOWN 
in the next quarter using SEC EDGAR fundamentals and BLS CPI 
inflation data.

## Live App
🔗 [Click here to use the app](https://gis-stock-predictor-dljoixmrvelg59ta6pxdya.streamlit.app/)

## Data Sources
- **SEC EDGAR**: `data.sec.gov/api/xbrl/companyfacts/CIK0000040704.json`
- **BLS CPI**: `api.bls.gov/publicAPI/v1/timeseries/data/CUUR0000SA0`
- **yfinance**: GIS historical prices (unofficial supplement)

## Models Used
- Logistic Regression (83.33% validation accuracy)
- Decision Tree with hyperparameter tuning (83.33%)
- Random Forest with hyperparameter tuning (100% validation, 63.16% test)

## Repository Contents
- `streamlit_app.py` — Deployment app
- `general_mills_data_pipeline.ipynb` — Data acquisition notebook
- `GIS_Stock_Prediction.rmp` — RapidMiner pipeline
- `gis_data_with_dates.csv` — Processed dataset

## Video Walkthrough
🎥 [Video link](YOUR_VIDEO_LINK_HERE)

## Disclaimer
For educational purposes only. Not financial advice.
