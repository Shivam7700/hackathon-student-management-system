import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "student_recs.csv")

def get_recommendations(student_id):
    """
    Fetch recommendations for a student based on their ID.
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("Student recommendations dataset not found.")

    data = pd.read_csv(DATA_PATH)
    
    # Find the student
    student = data[data["student_id"] == student_id]
    if student.empty:
        return ["No recommendations found for this Student ID."]
    
    # Convert string representation of list back to Python list
    recs = eval(student.iloc[0]["recommendations"])
    return recs
