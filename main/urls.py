from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    index,
    about,
    course_grid_2,
    course_grid_3,
    course_grid_4,
    team,
    signup,
    signin,
    sidebar,
    questionbank,
    defult_page,
    notice,
    modelexam,
    take_quiz,
    api_question,
      # Add the import for course_detail
)

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
    path('defult_page/', defult_page, name='defult_page'),
    path('notice/', notice, name='notice'),
    path('modelexam/', modelexam, name='modelexam'),
    path('<id>/', take_quiz, name='take_quiz'),
    path('api/<id>/', api_question, name='api_question'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
