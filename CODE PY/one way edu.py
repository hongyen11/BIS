import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("C:/Users/notco/Downloads/education_career_success.csv")
df.columns = df.columns.str.strip()

# Output directory
output_dir = ("C:/Users/notco/Downloads/Education_EDA_OneWay")
os.makedirs(output_dir, exist_ok=True)

# Bar Chart: Internships

one_way_counts = df['Internships_Completed'].value_counts(normalize=True).sort_index() * 100

plt.figure(figsize=(6,4))
bars = plt.bar(one_way_counts.index.astype(str), one_way_counts.values)

for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1,
             f"{bar.get_height():.1f}%",
             ha='center')

plt.xlabel("Internships Completed")
plt.ylabel("Percentage")
plt.title("Distribution of Internships Completed")
plt.ylim(0,100)
plt.tight_layout()

plt.savefig(f"{output_dir}/Figure_OneWay_Internships.png", dpi=300)
plt.show()

# Histogram: Starting Salary

plt.figure(figsize=(6,4))
plt.hist(df['Starting_Salary'], bins=20)
plt.xlabel("Starting Salary")
plt.ylabel("Frequency")
plt.title("Distribution of Starting Salary")
plt.tight_layout()
plt.savefig(f"{output_dir}/OneWay_Salary_Histogram.png", dpi=300)
plt.show()

# Boxplot: Current Job Level

job_order = ["Entry", "Mid", "Senior"]

# Convert to ordered category and encode
df["Current_Job_Level_Num"] = (
    df["Current_Job_Level"]
      .astype("category")
      .cat.set_categories(job_order, ordered=True)
      .cat.codes
)

plt.figure(figsize=(5,4))
plt.boxplot(df["Current_Job_Level_Num"], vert=False)
plt.xlabel("Current Job Level (Encoded)")
plt.title("Boxplot of Current Job Level")
plt.tight_layout()

plt.savefig(f"{output_dir}/OneWay_CurrentJobLevel_Boxplot.png", dpi=300)
plt.show()

# Pie Chart: Career Satisfaction 

df['Satisfaction_Level'] = pd.cut(
    df['Career_Satisfaction'],
    bins=[0, 6, 8, 10],
    labels=['Low', 'Medium', 'High']
)

satisfaction_counts = df['Satisfaction_Level'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    satisfaction_counts.values,
    labels=satisfaction_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Career Satisfaction Levels")
plt.tight_layout()
plt.savefig(f"{output_dir}/OneWay_CareerSatisfaction_Pie.png", dpi=300)
plt.show()
