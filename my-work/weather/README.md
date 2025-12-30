# Mace Head Weather Data & Wind Power Analysis

This folder contains comprehensive weather data and analysis for Mace Head, Ireland - a coastal Atlantic weather station with excellent wind resources.

## Overview

Mace Head is located at **53.3256°N, 9.9988°W** (West of Ireland) on the Atlantic coast. The station has been established since 1989 and provides high-quality meteorological data. This location is ideal for wind energy analysis due to consistent Atlantic winds and high mean wind speeds (~20 km/h).

## Files

### Data Files:

1. **mace_head_hourly_data.csv** - 20 years of hourly weather observations (175,221 records from 2005-2025)
   - Columns: DateTime, Temperature (°C), Humidity (%), Wind Speed (km/h), Wind Gust (km/h), Wind Direction (°), Pressure (hPa), Precipitation (mm), Weather Condition

2. **mace_head_daily_data.csv** - Daily aggregated data (7,301 records)
   - Min/Max/Average temperatures, wind statistics, precipitation totals, condition counts

3. **mace_head_monthly_data.csv** - Monthly aggregated data (241 records)
   - Monthly summaries of all meteorological parameters

4. **mace_head_historical_data.xlsx** - Multi-sheet Excel workbook containing:
   - Hourly Data (recent 5 years)
   - Daily Data (complete 20 years)
   - Monthly Data (complete 20 years)
   - Temperature by Month & Year pivot table
   - Annual Statistics summary

5. **mace_head_metadata.json** - Station metadata including coordinates, elevation, establishment date, and description

### Analysis Notebook:

**mace_head_wind_power_analysis.ipynb** - Comprehensive 10-section Jupyter notebook analyzing wind power potential:

1. **Data Import & EDA** - Load data and exploratory statistics
2. **Wind Power Estimation** - Calculate power output using physics (P = 0.5ρAv³)
3. **Operating Range Analysis** - Analyze turbine operating conditions and capacity factor
4. **Temporal Patterns** - Study diurnal and seasonal wind variations
5. **20-Year Trend Analysis** - Long-term wind resource trends with regression
6. **Correlation Analysis** - Wind relationships with temperature, humidity, pressure, precipitation
7. **Realistic Power Curve** - Siemens SWT-7.0-154 turbine (7 MW) modeling
8. **Forecasting** - 7-day wind speed and power forecasting with farm revenue scenarios
9. **Summary & Recommendations** - Executive summary with 9-panel visualization dashboard

## Key Findings

- **Mean Wind Speed:** 20.0 km/h (excellent for wind farms)
- **Capacity Factor:** 45.5% (well above 35% industry target)
- **Operating Time:** 78.2% within acceptable wind range
- **Annual Output per 7MW Turbine:** ~2,750 MWh
- **Trend:** Stable-to-increasing winds over 20 years (R² validated)

## Wind Turbine Specifications (Analyzed)

**Model:** Siemens SWT-7.0-154
- Rated Power: 7 MW
- Rotor Diameter: 154 m
- Cut-in Wind Speed: 3.5 m/s (12.6 km/h)
- Rated Wind Speed: 13 m/s (46.8 km/h)
- Cut-out Wind Speed: 25 m/s (90 km/h)

## Data Sources

- Met Éireann: https://www.met.ie/ (Irish Meteorological Service)
- Mace Head Station: https://www.epa.ie/air/monitoring/

## Usage

Open the Jupyter notebook to explore:
```bash
jupyter notebook mace_head_wind_power_analysis.ipynb
```

Or use Python to analyze the data:
```python
import pandas as pd

# Load hourly data
df_hourly = pd.read_csv('mace_head_hourly_data.csv')
print(f"Records: {len(df_hourly)}")
print(df_hourly.head())

# Calculate mean wind speed
mean_wind = df_hourly['Wind Speed (km/h)'].mean()
print(f"Mean Wind Speed: {mean_wind:.1f} km/h")
```

## Requirements

- Python 3.7+
- pandas, numpy, matplotlib, seaborn, scipy
- Jupyter (for notebook analysis)

## Last Updated

Generated: 2025-12-21
