from django.contrib import admin
from .models import Question, Choice

# Define an inline model for the Choice model
class ChoiceInline(admin.TabularInline):  # Or use StackedInline if you prefer a stacked layout
    model = Choice
    extra = 1  # This adds an empty choice form (set to the number you need)
    # Optional: fields to display in the inline form
    fields = ('choice_text', 'votes')  # Adjust this to the fields you want to display

# Register the Question model and add the inline model for Choices
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]  # Add the inline model here

# Register both Question and Choice
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
