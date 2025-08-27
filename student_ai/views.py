from django.shortcuts import render
from .predictor import predict_grade
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

from .student_recs_data import recommend

import os
import google.generativeai as genai
from django.shortcuts import render
from dotenv import load_dotenv

# --- Grade Prediction ---
def grade_prediction(request):
    prediction = None
    if request.method == "POST":
        attendance = float(request.POST.get("attendance"))
        assignments = float(request.POST.get("assignments"))
        previous_score = float(request.POST.get("previous_score"))

        prediction = predict_grade(attendance, assignments, previous_score)

    return render(request, "student_ai/prediction.html", {"prediction": prediction})


# --- Performance Analysis ---
from django.shortcuts import render

def performance_analysis(request):
    analysis = None
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        # Here, you can fetch all results and analyze
        # Example: simple mock analysis
        analysis = {
            "average_score": 85,
            "highest_score": 95,
            "lowest_score": 70,
            "trend": "Improving",
        }
    return render(request, "student_ai/performance.html", {"analysis": analysis})



# --- Recommendations ---
def recommendations(request):
    recs = None
    error = None

    if request.method == "POST":
        student_id_raw = request.POST.get("student_id")

        if student_id_raw.isdigit():  # ✅ only allow numbers
            student_id = int(student_id_raw)
            recs = recommend(student_id)
        else:
            error = "❌ Please enter a valid numeric Student ID."

    return render(request, "student_ai/recommendation.html", {"recs": recs, "error": error})

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def chatbot(request):
    response = None
    if request.method == "POST":
        user_message = request.POST.get("message")

        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(history=[])
        result = chat.send_message(user_message)

        response = result.text

    return render(request, "student_ai/chatbot.html", {"response": response})