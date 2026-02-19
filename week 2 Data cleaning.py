
# Sample raw data (could be from CSV or API)
raw_data = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 30, "score": 72},
    {"name": "Charlie", "age": 25, "score": 90},
    {"name": "Alice", "age": 25, "score": 85},  # duplicate
    {"name": "David", "age": 22, "score": 60},
]

# 1️⃣ Remove duplicates
def remove_duplicates(data):
    """Remove duplicate dictionaries from a list."""
    unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]
    return unique_data

# 2️⃣ Filter data (e.g., only age >= 25 and score >= 70)
def filter_data(data, min_age=25, min_score=70):
    """Filter out entries based on age and score thresholds."""
    return [d for d in data if d["age"] >= min_age and d["score"] >= min_score]

# 3️⃣ Data transformation (e.g., increase score by 5%)
def increase_score(data, percentage=5):
    """Increase the 'score' field by a percentage."""
    for d in data:
        d["score"] = round(d["score"] * (1 + percentage / 100), 2)
    return data

# -----------------------------
# Run Data Cleaning Pipeline
# -----------------------------
clean_data = remove_duplicates(raw_data)
filtered_data = filter_data(clean_data)
final_data = increase_score(filtered_data)

print("Raw Data:\n", raw_data)
print("\nCleaned & Filtered Data:\n", final_data)
