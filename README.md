# Exoplanet Transit Detector

## Overview
This project detects possible exoplanet transits by analyzing stellar light curve data. A transit is identified when a planet passes in front of a star, causing a temporary dip in brightness.

The system simulates light curve data and detects dips using statistical thresholding.

---

## Features
- Synthetic light curve generation
- Transit detection using statistical anomaly detection
- Visualization using Streamlit
- Simple and interpretable detection logic

---

## How It Works
1. Generate star brightness time-series data
2. Introduce simulated transit dips
3. Detect anomalies using mean and standard deviation threshold
4. Group nearby dips into transit events

---

## Project Structure# exoplanet-transit-detector
Simulate a star brightness signal with dips.
