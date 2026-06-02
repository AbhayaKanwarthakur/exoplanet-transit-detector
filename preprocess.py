import numpy as np
import pandas as pd

np.random.seed(42)

time = np.arange(0, 500)


brightness = 1 + 0.02 * np.sin(time / 10) + np.random.normal(0, 0.01, len(time))


for t in range(100, 120):
    brightness[t] -= 0.08

for t in range(300, 320):
    brightness[t] -= 0.06

df = pd.DataFrame({
    "time": time,
    "brightness": brightness
})

df.to_csv("sample_light_curve.csv", index=False)

print("Light curve generated.")