from django.contrib import admin
from .models import Course, Question, ScoreBoard, TeamMember, Notice

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)
admin.site.register(TeamMember)
admin.site.register(Notice)
