
# console_visualization.py
# ----------------------------------
# Dataset Visualization (No matplotlib, pure Python)
# ----------------------------------

# Sample dataset
employees = [
    {'name': 'Alice', 'department': 'IT', 'salary': 70000},
    {'name': 'Bob', 'department': 'HR', 'salary': 50000},
    {'name': 'Charlie', 'department': 'IT', 'salary': 75000},
    {'name': 'David', 'department': 'Finance', 'salary': 60000},
    {'name': 'Eva', 'department': 'HR', 'salary': 52000},
]

# ----------------------------------
# 1️⃣ Bar Chart (Salary by Employee)
# ----------------------------------
print("\nSALARY BAR CHART")
print("-" * 40)

for emp in employees:
    bar = "#" * (emp['salary'] // 2000)  # Scale down for display
    print(f"{emp['name']:10} | {bar} ({emp['salary']})")

# ----------------------------------
# 2️⃣ Department Distribution
# ----------------------------------
print("\nDEPARTMENT DISTRIBUTION")
print("-" * 40)

dept_count = {}

for emp in employees:
    dept = emp['department']
    dept_count[dept] = dept_count.get(dept, 0) + 1

for dept, count in dept_count.items():
    bar = "*" * count
    print(f"{dept:10} | {bar} ({count})")

# ----------------------------------
# 3️⃣ Salary Statistics
# ----------------------------------
print("\nSALARY STATISTICS")
print("-" * 40)

salaries = [emp['salary'] for emp in employees]

average_salary = sum(salaries) / len(salaries)
max_salary = max(salaries)
min_salary = min(salaries)

print(f"Average Salary : {average_salary}")
print(f"Highest Salary : {max_salary}")
print(f"Lowest Salary  : {min_salary}")
