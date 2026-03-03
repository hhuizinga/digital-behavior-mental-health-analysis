import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

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

# ---- Simple Mood Risk Classification ----

# Create binary target: low mood (1) vs not low (0)
df["low_mood"] = (df["mood_score"] < df["mood_score"].median()).astype(int)

# Features (behavior inputs)
X = df[[
    "daily_screen_time_min",
    "sleep_hours",
    "anxiety_level",
    "focus_score"
]]

# Target
y = df["low_mood"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Analysis complete.")
