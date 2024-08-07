from django.urls import path
from . import views

app_name= "questions"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("success/", views.success, name="success"),
    path("allvocab/", views.allvocab, name="allvocab"),
    # ex: /questions/5-5/
    path("<str:question_code>/", views.detail, name="detail"),
]