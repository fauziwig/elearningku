from django.shortcuts import render
from django.http import HttpResponse
from .models import Material, Question

def course_list(request):
    material_list = Material.objects.all()
    return render(request, 'material_list.html', {'material_list': material_list})

def course_detail(request, course_id):
    material = Material.objects.get(id=course_id)
    return render(request, 'material_detail.html', {'material': material})

def quiz_detail(request, course_id):
    material = Material.objects.get(id=course_id)
    questions = material.questions.all()
    return render(request, 'quiz.html', {'material': material, 'questions': questions})

def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        # Logic to handle quiz submission
        return HttpResponse("Quiz submitted successfully.")
    return HttpResponse("Invalid request method.")