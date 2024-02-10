from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)
admin.site.register(QuestionbankCourse)
admin.site.register(QuestionbankQuestion)
admin.site.register(QuestionbankScoreBoard)
admin.site.register(TeamMember)
admin.site.register(Notice)
