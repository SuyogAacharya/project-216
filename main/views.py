from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import   *

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

def questionbank(request):  
    return render(request, 'questionbank.html')

def notice(request):  
    return render(request, 'notice.html')

def modelexam(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'modelexam.html', context)

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

def api_question(request, id):
    raw_questions = Question.objects.filter(course=id)[:20]
    questions = []

    for raw_question in raw_questions:
        question = {
            'question': raw_question.question,
            'answer': raw_question.answer,
            'options': [raw_question.option_one, raw_question.option_two, raw_question.option_three, raw_question.option_four]
        }
        questions.append(question)

    return JsonResponse(questions, safe=False)

def take_quiz(request, id):
    context = {'id': id}
    return render(request, "modelexam.html", context)

