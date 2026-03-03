import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("mental_health_digital_behavior_data.csv")

# Quick preview
print(df.head())

# ---- Analysis 1: Screen Time vs Mood ----
plt.figure()
plt.scatter(df["daily_screen_time_min"], df["mood_score"])
plt.xlabel("Daily Screen Time (minutes)")
plt.ylabel("Mood Score")
plt.title("Screen Time vs Mood")
plt.show()

# ---- Analysis 2: Sleep vs Mood ----
plt.figure()
plt.scatter(df["sleep_hours"], df["mood_score"])
plt.xlabel("Sleep Hours")
plt.ylabel("Mood Score")
plt.title("Sleep vs Mood")
plt.show()

print("Analysis complete.")
