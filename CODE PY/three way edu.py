import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

df = pd.read_csv("C:/Users/notco/Downloads/education_career_success.csv")
df.columns = df.columns.str.strip()

output_dir = ("C:/Users/notco/Downloads/Education_EDA_ThreeWay")
os.makedirs(output_dir, exist_ok=True)

# Create categorical variables
df['GPA_Level'] = pd.cut(
    df['University_GPA'],
    bins=[0, 3.2, 3.6, 4.0],
    labels=['Low', 'Medium', 'High']
)

df['Soft_Skills_Level'] = pd.cut(
    df['Soft_Skills_Score'],
    bins=[0, 6.5, 8.5, 10],
    labels=['Low', 'Medium', 'High']
)

# THREE-WAY HEATMAP (GPA Level × Internships → Avg Starting Salary)
pivot_salary = pd.pivot_table(
    df,
    values='Starting_Salary',
    index='GPA_Level',
    columns='Internships_Completed',
    aggfunc='mean'
)

plt.figure(figsize=(7,4))
plt.imshow(pivot_salary, aspect='auto')
plt.colorbar(label='Average Starting Salary')

plt.xticks(
    ticks=range(len(pivot_salary.columns)),
    labels=pivot_salary.columns
)
plt.yticks(
    ticks=range(len(pivot_salary.index)),
    labels=pivot_salary.index
)

plt.xlabel("Internships Completed")
plt.ylabel("GPA Level")
plt.title("Heatmap of Starting Salary by GPA Level and Internships")
plt.tight_layout()
plt.savefig(f"{output_dir}\\ThreeWay_Heatmap_Salary.png", dpi=300)
plt.show()

# THREE-WAY SCATTER PLOT (Internships × Salary, coloured by GPA Level)
colors = {'Low': 'red', 'Medium': 'orange', 'High': 'green'}

plt.figure(figsize=(7,5))

for gpa in df['GPA_Level'].dropna().unique():
    subset = df[df['GPA_Level'] == gpa]
    plt.scatter(
        subset['Internships_Completed'],
        subset['Starting_Salary'],
        alpha=0.6,
        label=f"{gpa} GPA",
        c=colors[gpa]
    )

plt.xlabel("Internships Completed")
plt.ylabel("Starting Salary")
plt.title("Starting Salary vs Internships by GPA Level")
plt.legend()
plt.tight_layout()
plt.savefig(f"{output_dir}\\ThreeWay_Scatter_Salary.png", dpi=300)
plt.show()

# THREE-WAY COMPARATIVE BAR CHART (Soft Skills × Internships → Avg Job Offers)
job_skill = df.groupby(
    ['Soft_Skills_Level', 'Internships_Completed']
)['Job_Offers'].mean().unstack()

job_skill.plot(kind='bar', figsize=(8,4))

plt.xlabel("Soft Skills Level")
plt.ylabel("Average Job Offers")
plt.title("Average Job Offers by Soft Skills Level and Internships")
plt.legend(title="Internships Completed", bbox_to_anchor=(1.05,1))
plt.tight_layout()
plt.savefig(f"{output_dir}\\ThreeWay_Bar_JobOffers.png", dpi=300)
plt.show()
