
# dataset_pure_python.py
# ----------------------------------
# Data operations without CSV, Pandas, or NumPy
# ----------------------------------

# 1️⃣ Hardcoded dataset (list of dictionaries)
students = [
    {'name': 'Alice', 'Math': 85, 'Science': 92, 'English': 88},
    {'name': 'Bob', 'Math': 72, 'Science': 78, 'English': 80},
    {'name': 'Charlie', 'Math': 90, 'Science': 85, 'English': 95},
    {'name': 'David', 'Math': 60, 'Science': 70, 'English': 65},
    {'name': 'Eva', 'Math': 88, 'Science': 94, 'English': 90},
    {'name': 'Frank', 'Math': 75, 'Science': 80, 'English': 85},
]

# -----------------------------
# 2️⃣ Compute total and sum of squares for each student
# -----------------------------
for student in students:
    math, science, english = student['Math'], student['Science'], student['English']
    student['Total'] = math + science + english
    student['SumSquares'] = math**2 + science**2 + english**2

# -----------------------------
# 3️⃣ Curve scores (+5%)
# -----------------------------
for student in students:
    student['Math'] = round(student['Math'] * 1.05, 2)
    student['Science'] = round(student['Science'] * 1.05, 2)
    student['English'] = round(student['English'] * 1.05, 2)
    # Recalculate Total after curving
    student['Total'] = student['Math'] + student['Science'] + student['English']

# -----------------------------
# 4️⃣ Filter top students (Total >= 240)
# -----------------------------
top_students = [s for s in students if s['Total'] >= 240]

# -----------------------------
# 5️⃣ Display results
# -----------------------------
print("All Students with Total & SumSquares:")
for s in students:
    print(s)

print("\nTop Students (Total >= 240):")
for s in top_students:
    print(s)
