from django.contrib import admin
from .models import Course, Question, TeamMember, Notice 

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(TeamMember)
admin.site.register(Notice)  
