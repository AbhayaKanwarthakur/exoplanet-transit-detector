import pandas as pd
import numpy as np

df = pd.read_csv("sample_light_curve.csv")

brightness = df["brightness"].values
time = df["time"].values

mean = np.mean(brightness)
std = np.std(brightness)

threshold = mean - 2.5 * std

transits = brightness < threshold

transit_times = time[transits]

print("Possible transit events detected at:")
print(transit_times)

events = []
current_event = []

for t in transit_times:
    if not current_event:
        current_event.append(t)
    elif t - current_event[-1] <= 2:
        current_event.append(t)
    else:
        events.append(current_event)
        current_event = [t]

if current_event:
    events.append(current_event)

print("\nDetected Transit Events:")
for i, e in enumerate(events):
    print(f"Event {i+1}: Start {e[0]} End {e[-1]}")