from django.contrib import admin
from .models import Material, Question, Choice, QuizAttempt, QuizAnswer

class QuizAnswerInline(admin.TabularInline):
    model = QuizAnswer
    extra = 0
    readonly_fields = ('question', 'selected_choice', 'is_correct')
    can_delete = False

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'material', 'score', 'total_questions', 'percentage', 'passed', 'completed_at')
    list_filter = ('passed', 'completed_at', 'material')
    search_fields = ('user__username', 'material__title')
    readonly_fields = ('user', 'material', 'score', 'total_questions', 'passed', 'completed_at', 'percentage')
    inlines = [QuizAnswerInline]
    
    def percentage(self, obj):
        return f"{obj.percentage}%"
    percentage.short_description = 'Persentase'

@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'question', 'selected_choice', 'is_correct')
    list_filter = ('is_correct', 'attempt__material')
    search_fields = ('attempt__user__username', 'question__question_text')
    readonly_fields = ('attempt', 'question', 'selected_choice', 'is_correct')

admin.site.register(Material)
admin.site.register(Question)
admin.site.register(Choice)