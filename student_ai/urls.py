from django.urls import path
from . import views

urlpatterns = [
    path("grade-prediction/", views.grade_prediction, name="grade_prediction"),
    path("performance-analysis/", views.performance_analysis, name="performance_analysis"),
    path("recommendations/", views.recommendations, name="recommendations"),
    path("chatbot/", views.chatbot, name="chatbot"),
]