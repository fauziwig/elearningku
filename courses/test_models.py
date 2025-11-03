import pytest
from courses.models import Material, Question, Choice

@pytest.mark.django_db
class TestMaterial:
    def test_create_material(self):
        material = Material.objects.create(
            title='Python Basics',
            content='Introduction to Python programming'
        )
        assert material.title == 'Python Basics'
        assert material.content == 'Introduction to Python programming'
        assert material.created_at is not None
        assert material.updated_at is not None

    def test_material_str_representation(self):
        material = Material.objects.create(
            title='Django Tutorial',
            content='Learn Django framework'
        )
        assert str(material) == 'Django Tutorial'

    def test_material_with_image(self):
        material = Material.objects.create(
            title='Test Material',
            content='Test content'
        )
        assert not material.image

@pytest.mark.django_db
class TestQuestion:
    def test_create_question(self, material):
        question = Question.objects.create(
            material=material,
            question_text='What is Python?'
        )
        assert question.question_text == 'What is Python?'
        assert question.material == material
        assert question.created_at is not None

    def test_question_str_representation(self, material):
        question = Question.objects.create(
            material=material,
            question_text='What is Django?'
        )
        assert str(question) == 'What is Django?'

    def test_question_related_to_material(self, material):
        question1 = Question.objects.create(
            material=material,
            question_text='Question 1'
        )
        question2 = Question.objects.create(
            material=material,
            question_text='Question 2'
        )
        assert material.questions.count() == 2
        assert question1 in material.questions.all()
        assert question2 in material.questions.all()

    def test_question_cascade_delete(self, material):
        question = Question.objects.create(
            material=material,
            question_text='Test Question'
        )
        material_id = material.id
        material.delete()
        assert not Question.objects.filter(id=question.id).exists()

@pytest.mark.django_db
class TestChoice:
    def test_create_choice(self, question):
        choice = Choice.objects.create(
            question=question,
            choice_text='Answer A',
            is_correct=True
        )
        assert choice.choice_text == 'Answer A'
        assert choice.is_correct is True
        assert choice.question == question

    def test_choice_str_representation(self, question):
        choice = Choice.objects.create(
            question=question,
            choice_text='Answer B',
            is_correct=False
        )
        assert str(choice) == 'Answer B'

    def test_multiple_choices_per_question(self, question):
        choice1 = Choice.objects.create(
            question=question,
            choice_text='Choice 1',
            is_correct=True
        )
        choice2 = Choice.objects.create(
            question=question,
            choice_text='Choice 2',
            is_correct=False
        )
        choice3 = Choice.objects.create(
            question=question,
            choice_text='Choice 3',
            is_correct=False
        )
        assert question.choices.count() == 3
        correct_choices = question.choices.filter(is_correct=True)
        assert correct_choices.count() == 1
        assert correct_choices.first() == choice1

    def test_choice_cascade_delete(self, question):
        choice = Choice.objects.create(
            question=question,
            choice_text='Test Choice',
            is_correct=False
        )
        choice_id = choice.id
        question.delete()
        assert not Choice.objects.filter(id=choice_id).exists()
