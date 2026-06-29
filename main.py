import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Messy_Employee_Dataset_500_Rows.xlsx")

print("Dataset Loaded Successfully")
print(df.head())
print("\nDataset Information")

print(df.info())

print("\nMissing Values")

print(df.isnull().sum())

duplicates = df.duplicated().sum()

print("\nDuplicate Records:", duplicates)

salary_mean = df["Salary"].mean()

df["Salary"] = df["Salary"].fillna(salary_mean)

experience_median = df["Experience"].median()

df["Experience"] = df["Experience"].fillna(experience_median)

before_rows = len(df)

df = df.drop_duplicates()

after_rows = len(df)

print("\nDuplicates Removed:", before_rows - after_rows)

df["Department"] = df["Department"].str.upper()

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

print("\nSummary Statistics")

print(df.describe())

department_counts = df["Department"].value_counts()

department_counts.plot(
    kind="bar"
)

plt.title("Employees by Department")

plt.xlabel("Department")

plt.ylabel("Number of Employees")

plt.show()

df.to_excel(
    "Cleaned_Employee_Dataset.xlsx",
    index=False
)

print("\nCleaned Dataset Saved Successfully")

with open("Automation_Report.txt","w") as report:

    report.write("DATA CLEANING REPORT\n")

    report.write("===================\n\n")

    report.write(
        f"Total Records: {len(df)}\n"
    )

    report.write(
        f"Missing Salary Fixed\n"
    )

    report.write(
        f"Missing Experience Fixed\n"
    )

    report.write(
        f"Duplicates Removed\n"
    )

print("Report Generated Successfully")