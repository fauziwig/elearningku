from django.test import TestCase
from .models import Material, Question, Choice

class MaterialModelTest(TestCase):
    def setUp(self):
        self.material = Material.objects.create(title="Sample Material", content="This is a sample content.")

    def test_material_creation(self):
        self.assertEqual(self.material.title, "Sample Material")
        self.assertEqual(self.material.content, "This is a sample content.")

class QuestionModelTest(TestCase):
    def setUp(self):
        self.material = Material.objects.create(title="Sample Material", content="This is a sample content.")
        self.question = Question.objects.create(material=self.material, question_text="What is this?")

    def test_question_creation(self):
        self.assertEqual(self.question.question_text, "What is this?")
        self.assertEqual(self.question.material, self.material)

class ChoiceModelTest(TestCase):
    def setUp(self):
        self.material = Material.objects.create(title="Sample Material", content="This is a sample content.")
        self.question = Question.objects.create(material=self.material, question_text="What is this?")
        self.choice = Choice.objects.create(question=self.question, choice_text="Sample Choice", is_correct=True)

    def test_choice_creation(self):
        self.assertEqual(self.choice.choice_text, "Sample Choice")
        self.assertTrue(self.choice.is_correct)
        self.assertEqual(self.choice.question, self.question)