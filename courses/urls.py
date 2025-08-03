from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='material_list'),
    path('<int:course_id>/', views.course_detail, name='material_detail'),
    path('<int:course_id>/quiz/', views.quiz_detail, name='quiz'),
    path('<int:course_id>/quiz/submit/', views.submit_quiz, name='submit_quiz'),
    path('<int:course_id>/quiz/result/', views.quiz_result, name='quiz_result'),
]