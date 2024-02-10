from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def course_grid_2(request):  
    return render(request, 'course-grid-2.html')

def course_grid_3(request):  
    return render(request, 'course-grid-3.html')

def course_grid_4(request):  
    return render(request, 'course-grid-4.html')

def team(request): 
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'team.html', context)

def sidebar(request):  
    return render(request, 'sidebar.html')

def defult_page(request):  
    return render(request, 'defult_page.html')


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
    context = {'courses' : courses}
    return render(request , 'modelexam.html' , context)
    
def api_question(request , id):
    raw_questions = Question.objects.filter(course =id)[:20]
    questions = []
    
    for raw_question in raw_questions:
        question = {}
        question['id'] = raw_question.id
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        question['marks'] = raw_question.marks
        options = []
        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        if raw_question.option_three != '':
            options.append(raw_question.option_three)
        
        if raw_question.option_four != '':
            options.append(raw_question.option_four)
        
        question['options'] = options
         
        questions.append(question)
        
        
    return JsonResponse(questions , safe=False)
@login_required(login_url='/login')
def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context = {'score' : score}
    return render(request,'score.html' , context)

@login_required(login_url='/login')
def take_quiz(request , id):
    context = {'id' : id}
    return render(request , 'quiz.html'  , context)

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
        question = Question.objects.filter(id = solution.get('question_id')).first()
      
        if (question.answer) == solution.get('option'):
            score = score + question.marks
   
    score_board = ScoreBoard(course = course , score = score  , user = user)
    score_board.save() 
    
    return JsonResponse({'message' : 'success' , 'status':True})



def questionbank(request):
    Questionbank_courses = QuestionbankCourse.objects.all()
    context = {'Questionbank_courses': Questionbank_courses}
    return render(request, 'questionbank.html', context)

@csrf_exempt
def api_Questionbank_question(request, Id):
    raw_Questionbank_questions = QuestionbankQuestion.objects.filter(Questionbankcourse=Id)[:20]
    questions = []
    
    for raw_Questionbank_question in raw_Questionbank_question:
        question = {}
        question['Id'] = raw_Questionbank_question.Id
        question['question'] = raw_Questionbank_question.question
        question['answer'] = raw_Questionbank_question.answer
        question['marks'] = raw_Questionbank_question.marks
        options = []
        options.append(raw_Questionbank_question.option_one)
        options.append(raw_Questionbank_question.option_two)
        if raw_Questionbank_question.option_three != '':
            options.append(raw_Questionbank_question.option_three)
        
        if raw_Questionbank_question.option_four != '':
            options.append(raw_Questionbank_question.option_four)
        
        question['options'] = options
         
        Questionbank_questions.append(question)
        
    return JsonResponse(Questionbank_questions, safe=False)

@login_required(login_url='/login')
def view_Questionbank_score(request):
    user = request.user
    Questionbank_scores = QuestionbankScoreBoard.objects.filter(user=user).select_related('course')
    context = {'Questionbank_scores': Questionbank_scores}
    return render(request, 'Qscore.html', context)


def take_Questionbank_quiz(request, Id):
    context = {'Id': Id}
    return render(request, 'Qquiz.html', context)

@login_required(login_url='/login')
@csrf_exempt
def check_Questionbank_score(request):
    data = json.loads(request.body)
    user = request.user
    Questionbank_course_Id = data.get('course_Id')
    Questionbank_solutions = json.loads(data.get('data'))
    Questionbank_course = Questionbank_Course.objects.get(Id=Questionbank_question_Id)
    
    if (Questionbank_question.answer) == solution.get('option'):
            score = score + Questionbank_question.marks
   
    Questionbank_score_board = SuyogScoreBoard(Questionbank_course=Questionbank_course, score=score, user=user)
    Questionbank_score_board.save() 
    
    return JsonResponse({'message': 'success', 'status': True})

