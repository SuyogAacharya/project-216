from django.contrib import admin
from .models import *

class MedicalCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_months', 'seats_available', 'team_members', 'price')
    search_fields = ('title', 'description')

class CACourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_months', 'seats_available', 'team_members', 'price')
    search_fields = ('title', 'description')

admin.site.register(MedicalCourse, MedicalCourseAdmin)
admin.site.register(CACourse, CACourseAdmin)  # Corrected registration
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)
admin.site.register(QuestionbankCourse)
admin.site.register(QuestionbankQuestion)
admin.site.register(QuestionbankScoreBoard)
admin.site.register(TeamMember)
admin.site.register(Notice)
