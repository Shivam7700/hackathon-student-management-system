import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "student_recs_dataset.csv")

def load_data():
    """Load the dataset for recommendations."""
    if not os.path.exists(DATA_PATH):
        # Example dataset if CSV does not exist yet
        data = pd.DataFrame({
            "student_id": [1, 2, 3, 4, 5],
            "attendance": [80, 60, 95, 70, 85],
            "assignments": [75, 50, 90, 60, 80],
            "previous_score": [70, 55, 92, 65, 83],
            "final_grade": [72, 58, 93, 67, 84],
        })
        data.to_csv(DATA_PATH, index=False)
    else:
        data = pd.read_csv(DATA_PATH)
    return data


def recommend(student_id: int):
    """Return recommendations for a given student_id."""
    data = load_data()

    # Select student row
    student = data[data["student_id"] == student_id]

    if student.empty:
        return ["❌ No recommendations found for this Student ID."]

    student = student.iloc[0]  # extract the row
    recs = []

    # Rule-based recommendations
    if student["attendance"] < 75:
        recs.append("📌 Improve attendance to boost performance.")
    else:
        recs.append("✅ Good attendance, keep it up!")

    if student["assignments"] < 70:
        recs.append("📌 Focus on completing assignments regularly.")
    else:
        recs.append("✅ Assignment performance is strong.")

    if student["previous_score"] < 60:
        recs.append("📌 Seek extra help from teachers to strengthen weak subjects.")
    else:
        recs.append("✅ Previous scores indicate strong understanding.")

    # Final grade based recommendation
    if student["final_grade"] < 65:
        recs.append("⚠️ Final grade is below average, consistent study needed.")
    else:
        recs.append("🌟 Final grade is satisfactory, aim for excellence!")

    return recs
