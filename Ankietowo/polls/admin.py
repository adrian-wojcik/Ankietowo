from django.contrib import admin
from .models import Question, Choice
from .forms import QuestionForm


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'create_date', 'was_published_recently')
    list_filter = ['create_date']
    search_fields = ['question_text']

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ('create_date',)
        return super().add_view(request, form_url, extra_context)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
