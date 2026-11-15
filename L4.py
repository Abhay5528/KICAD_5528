import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read exported LTspice data
df = pd.read_csv("Vout_5V.txt", sep="\t")

# Extract voltage values
vin = df.iloc[:, 0]
vout = df.iloc[:, 1]

# Plot VTC
plt.figure(figsize=(9, 6))
plt.plot(vin, vout, linewidth=2, color='blue')

plt.xlabel("Input Voltage VIN (V)")
plt.ylabel("Output Voltage VOUT (V)")
plt.title("CMOS Inverter Voltage Transfer Characteristic")

plt.grid(True)
plt.tight_layout()

plt.savefig("VTC.png", dpi=300)
plt.show()