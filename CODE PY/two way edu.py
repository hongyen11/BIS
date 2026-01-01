import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("C:/Users/notco/Downloads/education_career_success.csv")
df.columns = df.columns.str.strip()

output_dir = ("C:/Users/notco/Downloads/Education_EDA_TwoWay")
os.makedirs(output_dir, exist_ok=True)

# Grouped Bar: Job Offers by Internships

job_by_intern = df.groupby('Internships_Completed')['Job_Offers'].mean()

plt.figure(figsize=(6,4))
plt.bar(job_by_intern.index.astype(str), job_by_intern.values)
plt.xlabel("Internships Completed")
plt.ylabel("Average Job Offers")
plt.title("Average Job Offers by Internships")
plt.tight_layout()
plt.savefig(f"{output_dir}/TwoWay_Internships_JobOffers_Bar.png", dpi=300)
plt.show()

# Line Chart: Salary vs Internships

salary_by_intern = df.groupby('Internships_Completed')['Starting_Salary'].mean()

plt.figure(figsize=(6,4))
plt.plot(salary_by_intern.index, salary_by_intern.values, marker='o')
plt.xlabel("Internships Completed")
plt.ylabel("Average Starting Salary")
plt.title("Starting Salary Trend by Internships")
plt.tight_layout()
plt.savefig(f"{output_dir}/TwoWay_Internships_Salary_Line.png", dpi=300)
plt.show()

# Boxplot: Salary by GPA Level

df['GPA_Level'] = pd.cut(
    df['University_GPA'],
    bins=[0, 3.2, 3.6, 4.0],
    labels=['Low', 'Medium', 'High']
)

salary_gpa = [
    df[df['GPA_Level'] == level]['Starting_Salary']
    for level in df['GPA_Level'].dropna().unique()
]

plt.figure(figsize=(6,4))
plt.boxplot(salary_gpa, labels=df['GPA_Level'].dropna().unique())
plt.xlabel("GPA Level")
plt.ylabel("Starting Salary")
plt.title("Starting Salary by GPA Level")
plt.tight_layout()
plt.savefig(f"{output_dir}/TwoWay_GPA_Salary_Box.png", dpi=300)
plt.show()

# Heatmap-Style Table: Job Offers vs GPA Level

pivot = pd.pivot_table(
    df,
    values='Job_Offers',
    index='GPA_Level',
    columns='Internships_Completed',
    aggfunc='mean'
)

plt.figure(figsize=(7,4))
plt.imshow(pivot, aspect='auto')
plt.colorbar(label='Average Job Offers')
plt.xticks(range(len(pivot.columns)), pivot.columns)
plt.yticks(range(len(pivot.index)), pivot.index)
plt.xlabel("Internships Completed")
plt.ylabel("GPA Level")
plt.title("Heatmap of Job Offers by GPA and Internships")
plt.tight_layout()
plt.savefig(f"{output_dir}/TwoWay_Heatmap_JobOffers.png", dpi=300)
plt.show()
