import pandas as pd
import re

# Sample simulated SCADA logs
logs = [
    "2025-07-01 14:02:15 - SENSOR_01 - Temperature: 45.2°C",
    "2025-07-01 14:02:20 - SENSOR_02 - Pressure: 102.3 psi",
    "2025-07-01 14:02:25 - SENSOR_03 - Voltage: 250V",
    "2025-07-01 14:02:30 - SENSOR_01 - Temperature: 120.0°C",  # Anomalous
    "2025-07-01 14:02:35 - SENSOR_04 - ERROR: Timeout",
    "2025-07-01 14:02:40 - SENSOR_02 - Pressure: 98.7 psi",
    "2025-07-01 14:02:45 - SENSOR_04 - ERROR: Unauthorized command"  # Suspicious
]

def parse_log(log):
    pattern = r'(?P<timestamp>[\d\-:\s]+) - (?P<sensor>SENSOR_\d+) - (?P<message>.+)'
    match = re.match(pattern, log)
    return match.groupdict() if match else None

parsed_logs = [parse_log(line) for line in logs if parse_log(line)]
df = pd.DataFrame(parsed_logs)

# Simple anomaly logic
def is_anomaly(row):
    if "ERROR" in row["message"]:
        return True
    if "Temperature" in row["message"]:
        temp = float(re.search(r'([\d.]+)', row["message"]).group())
        return temp > 100.0
    return False

df["is_anomaly"] = df.apply(is_anomaly, axis=1)

# Display anomalies
print("=== Anomalous Events Detected ===")
print(df[df["is_anomaly"]])

# Save to CSV (optional)
df.to_csv("scada_anomaly_report.csv", index=False)
