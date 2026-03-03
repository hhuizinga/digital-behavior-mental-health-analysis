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

# ---- Correlation Analysis ----
print("\nCorrelation Matrix:")
corr_matrix = df[[
    "daily_screen_time_min",
    "sleep_hours",
    "mood_score",
    "anxiety_level",
    "focus_score"
]].corr()

print(corr_matrix)

# Optional: visualize correlation heatmap
plt.figure()
plt.imshow(corr_matrix)
plt.colorbar()
plt.title("Correlation Matrix Heatmap")
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.tight_layout()
plt.show()
