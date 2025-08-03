from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Material, Question, Choice

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

def submit_quiz(request, course_id):
    if request.method == 'POST':
        # Collect user answers
        material = get_object_or_404(Material, id=course_id)
        questions = material.questions.all()
        user_answers = {}
        score = 0
        total = questions.count()
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                user_answers[question.id] = int(selected_choice_id)
                try:
                    choice = Choice.objects.get(id=selected_choice_id, question=question)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass
        passed = score >= (total // 2)  # Example: pass if at least half correct
        # Store user_answers in session or pass via GET/POST if needed
        request.session['quiz_result'] = {
            'user_answers': user_answers,
            'score': score,
            'total': total,
            'passed': passed,
        }
        return redirect('quiz_result', course_id=course_id)
    return HttpResponse("Invalid request method.")

def quiz_result(request, course_id):
    material = get_object_or_404(Material, id=course_id)
    questions = material.questions.all()
    result = request.session.get('quiz_result')
    if not result:
        return redirect('quiz', course_id=course_id)
    user_answers = result.get('user_answers', {})
    score = result.get('score', 0)
    total = result.get('total', questions.count())
    passed = result.get('passed', False)
    # Remove result from session after displaying
    del request.session['quiz_result']
    return render(request, 'quiz_result.html', {
        'material': material,
        'questions': questions,
        'user_answers': user_answers,
        'score': score,
        'total': total,
        'passed': passed,
    })