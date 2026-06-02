import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("sample_light_curve.csv")

st.title("Exoplanet Transit Detector")

st.write("Detect dips in star brightness indicating possible exoplanets")

st.line_chart(df.set_index("time"))

brightness = df["brightness"].values

mean = np.mean(brightness)
std = np.std(brightness)

threshold = mean - 2.5 * std

st.write("Detection Threshold:", threshold)

transits = brightness < threshold

df["transit"] = transits

st.subheader("Detected Transit Points")

st.line_chart(df.set_index("time")[["brightness", "transit"]])