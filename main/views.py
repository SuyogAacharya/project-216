from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import ProfileForm
import json

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def course_grid_2(request):
    medical_courses = MedicalCourse.objects.all()  
    return render(request, 'course-grid-2.html',  {'medical_courses': medical_courses})


def course_grid_3(request):
    ca_courses = CACourse.objects.all() 
    return render(request, 'course-grid-3.html' , {'ca_courses': ca_courses})
    
def course_grid_4(request):  
    return render(request, 'course-grid-4.html')

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProfileForm
from .models import StudentProfile

def profile(request):
    # Fetch the existing profile if it exists
    student_profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:profile'))  # Redirect to the same page after saving
    else:
        form = ProfileForm(instance=student_profile)
    
    context = {
        'form': form,
        'student_profile': student_profile
    }
    return render(request, 'profile.html', context)


def team(request): 
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'team.html', context)

def sidebar(request):  
    return render(request, 'sidebar.html')

def notice(request):
    notices = Notice.objects.all()  # Retrieve all notices
    return render(request, 'notice.html', {'notices': notices})  

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:sidebar')
        else:
            return render(request, 'signin.html', {'error_message': 'Invalid credentials'})

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password1
            )
            user.save()
            messages.success(request, 'Account created successfully. You can now sign in.')
            return redirect('main:signin')
        else:
            pass

    return render(request, 'signup.html')

def modelexam(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'modelexam.html', context)

def api_question(request, id):
    raw_questions = Question.objects.filter(course=id)[:20]
    questions = []
    
    for raw_question in raw_questions:
        question = {
            'id': raw_question.id,
            'question': raw_question.question,
            'answer': raw_question.answer,
            'marks': raw_question.marks,
            'options': [raw_question.option_one, raw_question.option_two, raw_question.option_three, raw_question.option_four]
        }
        questions.append(question)
        
    return JsonResponse(questions, safe=False)

@login_required(login_url='/login')
def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score': score}
    return render(request, 'score.html', context)

@login_required(login_url='/login')
def take_quiz(request, id):
    context = {'id': id}
    return render(request, 'quiz.html', context)

@csrf_exempt
@login_required(login_url='/login')
def check_score(request):
    data = json.loads(request.body)
    user = request.user
    course_id = data.get('course_id')
    solutions = json.loads(data.get('data'))
    course = Course.objects.get(id=course_id)
    score = 0
    for solution in solutions:
        question = Question.objects.get(id=solution.get('question_id'))
        if question.answer == solution.get('option'):
            score += question.marks
   
    score_board = ScoreBoard(course=course, score=score, user=user)
    score_board.save() 
    
    return JsonResponse({'message': 'success', 'status': True})

def questionbank(request):
    Questionbank_courses = QuestionbankCourse.objects.all()
    context = {'Questionbank_courses': Questionbank_courses}
    return render(request, 'questionbank.html', context)

@csrf_exempt
def api_Questionbank_question(request, id):
    raw_Questionbank_questions = QuestionbankQuestion.objects.filter(Questionbankcourse=id)[:20]
    questions = []
    
    for raw_Questionbank_question in raw_Questionbank_questions:
        question = {
            'id': raw_Questionbank_question.id,
            'question': raw_Questionbank_question.question,
            'answer': raw_Questionbank_question.answer,
            'marks': raw_Questionbank_question.marks,
            'options': [raw_Questionbank_question.option_one, raw_Questionbank_question.option_two, raw_Questionbank_question.option_three, raw_Questionbank_question.option_four]
        }
        questions.append(question)
        
    return JsonResponse(questions, safe=False)

@login_required(login_url='/login')
def view_Questionbank_score(request):
    user = request.user
    Questionbank_scores = QuestionbankScoreBoard.objects.filter(user=user).select_related('course')
    context = {'Questionbank_scores': Questionbank_scores}
    return render(request, 'Qscore.html', context)

def take_Questionbank_quiz(request, id):
    context = {'id': id}
    return render(request, 'Qquiz.html', context)

@login_required(login_url='/login')
@csrf_exempt
def check_Questionbank_score(request):
    data = json.loads(request.body)
    user = request.user
    Questionbank_course_id = data.get('course_id')
    Questionbank_solutions = json.loads(data.get('data'))
    Questionbank_course = QuestionbankCourse.objects.get(id=Questionbank_course_id)
    score = 0
    for solution in Questionbank_solutions:
        question = QuestionbankQuestion.objects.get(id=solution.get('question_id'))
        if question.answer == solution.get('option'):
            score += question.marks
   
    Questionbank_score_board = QuestionbankScoreBoard(course=Questionbank_course, score=score, user=user)
    Questionbank_score_board.save() 
    
    return JsonResponse({'message': 'success', 'status': True})
