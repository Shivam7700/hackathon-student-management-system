import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "grade_model.pkl")
DATA_PATH = os.path.join(os.path.dirname(__file__), "student_grades.csv")

def train_model():
    # Load dataset
    data = pd.read_csv(DATA_PATH)
    X = data[["attendance", "assignments", "previous_score"]]
    y = data["final_grade"]

    # Train Random Forest
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save the model
    joblib.dump(model, MODEL_PATH)
    print("✅ Model trained and saved at", MODEL_PATH)

def predict_grade(attendance, assignments, previous_score):
    # Clip inputs to 0-100
    attendance = max(0, min(100, attendance))
    assignments = max(0, min(100, assignments))
    previous_score = max(0, min(100, previous_score))

    # Train if model does not exist
    if not os.path.exists(MODEL_PATH):
        train_model()

    model = joblib.load(MODEL_PATH)
    prediction = model.predict([[attendance, assignments, previous_score]])

    # Clip prediction to 0-100
    return max(0, min(100, round(prediction[0], 2)))

# Test
if __name__ == "__main__":
    print(predict_grade(85, 80, 75))
