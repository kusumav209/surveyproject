
from django.contrib import admin
from .models import Survey, Response


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'survey',
        'selected_option',
        'rating',
        'submitted_at'
    )

    search_fields = ('name', 'email', 'feedback')

    list_filter = ('rating', 'selected_option', 'submitted_at')

    ordering = ('-submitted_at',)
