from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('course_grid_2/', course_grid_2, name='course_grid_2'),
    path('course_grid_3/', course_grid_3, name='course_grid_3'),
    path('course_grid_4/', course_grid_4, name='course_grid_4'),
    path('team/', team, name='team'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('sidebar/', sidebar, name='sidebar'),
    path('questionbank/', questionbank, name='questionbank'),
    path('questionbank/<int:id>/', take_Questionbank_quiz, name='take_Questionbank_quiz'), 
    path('questionbank/score/', view_Questionbank_score, name='view_Questionbank_score'), 
    path('api/questionbank/<int:id>/', api_Questionbank_question, name='api_Questionbank_question'), 
    path('api/Questionbank_check-score/', check_Questionbank_score, name='Questionbank_check_score'), 
    path('profile/', profile, name='profile'),
    path('notice/', notice, name='notice'),
    path('modelexam/', modelexam, name='modelexam'),
    path('view_score/' , view_score , name="view_score"),
    path('api/check_score' , check_score , name="check_score"),
    path('<id>/' , take_quiz , name="take_quiz"),
    path('api/<id>/' , api_question , name="api_question"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
