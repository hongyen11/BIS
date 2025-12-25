import pandas as pd

df = pd.read_csv("C:/Users/notco/Downloads/education_career_success.csv")

# Inspect structure and data types
print("Dataset Information:")
df.info()
print("\n")

# Check for missing values
print("Missing Values Check:")
print(df.isnull().sum())
print("\n")

# Remove non-analytical identifier
df.drop(columns=["Student_ID"], inplace=True)
print("Student_ID column removed\n")

# Descriptive statistics
desc = df.describe().T
desc["IQR"] = desc["75%"] - desc["25%"]

desc_stats = desc[[
    "mean",
    "std",
    "min",
    "25%",
    "50%",
    "75%",
    "max",
    "IQR"
]]

print(desc_stats)

print("Final Cleaned Dataset Info:")
df.info()
