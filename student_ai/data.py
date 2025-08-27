import pandas as pd
import random

# Generate a synthetic dataset with 100 students
data = []
for _ in range(100):
    attendance = random.randint(50, 100)
    assignments = random.randint(40, 100)
    previous_score = random.randint(40, 100)
    
    # Simple rule to generate final grade (can be adjusted)
    final_grade = round(0.4 * previous_score + 0.3 * assignments + 0.3 * attendance)
    final_grade = max(0, min(100, final_grade))  # Ensure 0-100

    data.append([attendance, assignments, previous_score, final_grade])

df = pd.DataFrame(data, columns=["attendance", "assignments", "previous_score", "final_grade"])
df.to_csv("student_grades.csv", index=False)
print("✅ Dataset saved as student_grades.csv")
