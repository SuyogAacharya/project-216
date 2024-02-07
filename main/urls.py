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
    view_score,   # Import view_score
    check_score,  # Import check_score
    take_quiz,    # Import take_quiz
    api_question, # Import api_question
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
    path('view_score/', view_score, name='view_score'),  # Add view_score URL
    path('api/check_score/', check_score, name='check_score'),  # Add check_score URL
    path('<int:id>/', take_quiz, name='take_quiz'),  # Add take_quiz URL
    path('api/<int:id>/', api_question, name='api_question'),  # Add api_question URL
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
