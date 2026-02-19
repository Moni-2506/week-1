
# data_cleaning.py


# 1️⃣ Raw dataset (contains duplicates & missing values)
data = [
    {'name': 'Alice', 'department': 'IT', 'salary': 70000},
    {'name': 'Bob', 'department': 'HR', 'salary': 50000},
    {'name': 'Charlie', 'department': 'IT', 'salary': None},  # Missing salary
    {'name': 'David', 'department': 'Finance', 'salary': 60000},
    {'name': 'Eva', 'department': 'HR', 'salary': 52000},
    {'name': 'Alice', 'department': 'IT', 'salary': 70000},  # Duplicate
    {'name': 'Frank', 'department': 'Finance', 'salary': None},  # Missing salary
]

# ----------------------------------
# 2️⃣ Remove missing values
# ----------------------------------
def remove_missing(data_list):
    return [row for row in data_list if row['salary'] is not None]

cleaned_data = remove_missing(data)

# ----------------------------------
# 3️⃣ Remove duplicates
# ----------------------------------
def remove_duplicates(data_list):
    unique = []
    seen = set()
    for row in data_list:
        identifier = (row['name'], row['department'], row['salary'])
        if identifier not in seen:
            seen.add(identifier)
            unique.append(row)
    return unique

cleaned_data = remove_duplicates(cleaned_data)

# ----------------------------------
# 4️⃣ Calculate overall average salary
# ----------------------------------
def calculate_average_salary(data_list):
    total = sum(row['salary'] for row in data_list)
    return total / len(data_list) if data_list else 0

overall_average = calculate_average_salary(cleaned_data)

# ----------------------------------
# 5️⃣ Aggregate: Average salary by department
# ----------------------------------
def average_by_department(data_list):
    dept_totals = {}
    dept_counts = {}

    for row in data_list:
        dept = row['department']
        salary = row['salary']

        if dept not in dept_totals:
            dept_totals[dept] = 0
            dept_counts[dept] = 0

        dept_totals[dept] += salary
        dept_counts[dept] += 1

    dept_averages = {}
    for dept in dept_totals:
        dept_averages[dept] = dept_totals[dept] / dept_counts[dept]

    return dept_averages

department_averages = average_by_department(cleaned_data)

# ----------------------------------
# 6️⃣ Display Results
# ----------------------------------
print("Cleaned Dataset:")
for row in cleaned_data:
    print(row)

print("\nOverall Average Salary:", round(overall_average, 2))

print("\nAverage Salary by Department:")
for dept, avg in department_averages.items():
    print(f"{dept}: {round(avg, 2)}")
