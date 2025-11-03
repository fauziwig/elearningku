import pytest
from django.urls import reverse
from courses.models import Material, Question, Choice

@pytest.mark.django_db
class TestCourseListView:
    def test_course_list_page_loads(self, client):
        url = reverse('material_list')
        response = client.get(url)
        assert response.status_code == 200
        assert 'material_list' in response.context

    def test_course_list_displays_materials(self, client):
        Material.objects.create(title='Course 1', content='Content 1')
        Material.objects.create(title='Course 2', content='Content 2')
        
        url = reverse('material_list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context['material_list']) == 2

    def test_course_list_empty(self, client):
        url = reverse('material_list')
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.context['material_list']) == 0

@pytest.mark.django_db
class TestCourseDetailView:
    def test_course_detail_page_loads(self, client, material):
        url = reverse('material_detail', args=[material.id])
        response = client.get(url)
        assert response.status_code == 200
        assert response.context['material'] == material

    def test_course_detail_shows_correct_content(self, client, material):
        url = reverse('material_detail', args=[material.id])
        response = client.get(url)
        assert material.title in response.content.decode()

    def test_course_detail_invalid_id(self, client):
        url = reverse('material_detail', args=[9999])
        with pytest.raises(Exception):
            response = client.get(url)

@pytest.mark.django_db
class TestQuizDetailView:
    def test_quiz_detail_page_loads(self, client, material, question):
        url = reverse('quiz', args=[material.id])
        response = client.get(url)
        assert response.status_code == 200
        assert 'material' in response.context
        assert 'questions' in response.context

    def test_quiz_displays_questions(self, client, material, question, choices):
        url = reverse('quiz', args=[material.id])
        response = client.get(url)
        assert response.status_code == 200
        assert question in response.context['questions']

    def test_quiz_invalid_material_id(self, client):
        url = reverse('quiz', args=[9999])
        with pytest.raises(Exception):
            response = client.get(url)

@pytest.mark.django_db
class TestSubmitQuizView:
    def test_submit_quiz_with_correct_answer(self, client, material, question, choices):
        url = reverse('submit_quiz', args=[material.id])
        correct_choice = choices[0]
        data = {
            f'question_{question.id}': correct_choice.id
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert response.url == reverse('quiz_result', args=[material.id])

    def test_submit_quiz_with_wrong_answer(self, client, material, question, choices):
        url = reverse('submit_quiz', args=[material.id])
        wrong_choice = choices[1]
        data = {
            f'question_{question.id}': wrong_choice.id
        }
        response = client.post(url, data)
        assert response.status_code == 302

    def test_submit_quiz_stores_result_in_session(self, client, material, question, choices):
        url = reverse('submit_quiz', args=[material.id])
        correct_choice = choices[0]
        data = {
            f'question_{question.id}': correct_choice.id
        }
        client.post(url, data)
        session = client.session
        assert 'quiz_result' in session
        assert 'score' in session['quiz_result']
        assert 'total' in session['quiz_result']
        assert 'passed' in session['quiz_result']

    def test_submit_quiz_get_method_returns_error(self, client, material):
        url = reverse('submit_quiz', args=[material.id])
        response = client.get(url)
        assert response.status_code == 200
        assert 'Invalid request method' in response.content.decode()

@pytest.mark.django_db
class TestQuizResultView:
    def test_quiz_result_page_loads_with_session_data(self, client, material, question, choices):
        session = client.session
        session['quiz_result'] = {
            'user_answers': {question.id: choices[0].id},
            'score': 1,
            'total': 1,
            'passed': True
        }
        session.save()
        
        url = reverse('quiz_result', args=[material.id])
        response = client.get(url)
        assert response.status_code == 200
        assert response.context['score'] == 1
        assert response.context['total'] == 1
        assert response.context['passed'] is True

    def test_quiz_result_redirects_without_session_data(self, client, material):
        url = reverse('quiz_result', args=[material.id])
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse('quiz', args=[material.id])

    def test_quiz_result_clears_session_after_display(self, client, material, question, choices):
        session = client.session
        session['quiz_result'] = {
            'user_answers': {question.id: choices[0].id},
            'score': 1,
            'total': 1,
            'passed': True
        }
        session.save()
        
        url = reverse('quiz_result', args=[material.id])
        client.get(url)
        
        session = client.session
        assert 'quiz_result' not in session

@pytest.mark.django_db
class TestQuizScoring:
    def test_quiz_score_all_correct(self, client, material):
        q1 = Question.objects.create(material=material, question_text='Q1')
        q2 = Question.objects.create(material=material, question_text='Q2')
        
        c1_correct = Choice.objects.create(question=q1, choice_text='C1 Correct', is_correct=True)
        c1_wrong = Choice.objects.create(question=q1, choice_text='C1 Wrong', is_correct=False)
        c2_correct = Choice.objects.create(question=q2, choice_text='C2 Correct', is_correct=True)
        c2_wrong = Choice.objects.create(question=q2, choice_text='C2 Wrong', is_correct=False)
        
        url = reverse('submit_quiz', args=[material.id])
        data = {
            f'question_{q1.id}': c1_correct.id,
            f'question_{q2.id}': c2_correct.id
        }
        client.post(url, data)
        
        session = client.session
        assert session['quiz_result']['score'] == 2
        assert session['quiz_result']['total'] == 2
        assert session['quiz_result']['passed'] is True

    def test_quiz_score_all_wrong(self, client, material):
        q1 = Question.objects.create(material=material, question_text='Q1')
        q2 = Question.objects.create(material=material, question_text='Q2')
        
        c1_correct = Choice.objects.create(question=q1, choice_text='C1 Correct', is_correct=True)
        c1_wrong = Choice.objects.create(question=q1, choice_text='C1 Wrong', is_correct=False)
        c2_correct = Choice.objects.create(question=q2, choice_text='C2 Correct', is_correct=True)
        c2_wrong = Choice.objects.create(question=q2, choice_text='C2 Wrong', is_correct=False)
        
        url = reverse('submit_quiz', args=[material.id])
        data = {
            f'question_{q1.id}': c1_wrong.id,
            f'question_{q2.id}': c2_wrong.id
        }
        client.post(url, data)
        
        session = client.session
        assert session['quiz_result']['score'] == 0
        assert session['quiz_result']['total'] == 2
        assert session['quiz_result']['passed'] is False

    def test_quiz_score_partial(self, client, material):
        q1 = Question.objects.create(material=material, question_text='Q1')
        q2 = Question.objects.create(material=material, question_text='Q2')
        q3 = Question.objects.create(material=material, question_text='Q3')
        
        c1_correct = Choice.objects.create(question=q1, choice_text='C1 Correct', is_correct=True)
        c2_correct = Choice.objects.create(question=q2, choice_text='C2 Correct', is_correct=True)
        c3_wrong = Choice.objects.create(question=q3, choice_text='C3 Wrong', is_correct=False)
        
        url = reverse('submit_quiz', args=[material.id])
        data = {
            f'question_{q1.id}': c1_correct.id,
            f'question_{q2.id}': c2_correct.id,
            f'question_{q3.id}': c3_wrong.id
        }
        client.post(url, data)
        
        session = client.session
        assert session['quiz_result']['score'] == 2
        assert session['quiz_result']['total'] == 3
        assert session['quiz_result']['passed'] is True
