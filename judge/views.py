from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Problem,Submission
from .forms import ProblemForm, UserForm, UploadFileForm
from media.CodeChecker import comple, run, filechecker
import os

TEXT_FILE_TYPES = ['txt', ]
INPUT_FILE_TYPES = {'cpp', }


def create_problem(request):
    if not request.user.is_authenticated():
        return render(request, 'judge/login.html')
    else:
        form = ProblemForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
        context = {
            "form": form,
        }
        return render(request, 'judge/add_problem.html', context)


def detail(request, pcode):
    if not request.user.is_authenticated:
        return render(request, 'judge/login.html')
    else:
        user = request.user
        problem = get_object_or_404(Problem, pk=pcode)
        return render(request, 'judge/detail.html', {'problem': problem, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'judge/login.html')
    else:
        problems = Problem.objects.all()
        query = request.GET.get("q")
        if query:
            problems = problems.filter(
                Q(pcode__icontains=query) |
                Q(author__icontains=query)
            ).distinct()
            return render(request, 'judge/index.html', {
                'problems': problems,
            })
        else:
            return render(request, 'judge/index.html', {'problems': problems})


def submission(request, pcode):
    problem = get_object_or_404(Problem, pk=pcode)
    sub = Submission()
    sub.upload = request.FILES['cppFile']
    sub.user = request.user
    sub.problem = Problem.objects.get(pcode=pcode)
    sub.save()
    files = "/home/avinash/Desktop/CodeJudge/media"
    file = str(sub.upload.name)
    path = os.getcwd() 
    path = path + "/" + file
    fp = open(path, 'r+')
    os.system('cd '+ str(problem.pcode))
    #try:
    comple(file,'cpp')
    #except:
     #   return render(request,'judge/submission.html', {'error' : 'Problem not compiled!'})
    #try:
    run()
    #except:
    #return render(request,'judge/submission.html', {'error' : 'Run Time Error!'})
    if filechecker(files + "/" + str(problem.pcode)):
        print("Check")
        return render(request,'judge/submission.html', {'success': 'Accepted'})
    else:
        return render(request,'judge/submission.html', {'error': 'Wrong Answer'})
    
    return render(request, 'judge/submission.html', {'problem': problem})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'judge/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                problems = Problem.objects.filter(user=request.user)
                return render(request, 'judge/index.html', {'problems': problems})
            else:
                return render(request, 'judge/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'judge/login.html', {'error_message': 'Invalid login'})
    return render(request, 'judge/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                problems = Problem.objects.filter(user=request.user)
                return render(request, 'judge/index.html', {'problems': problems})
    context = {
        "form": form,
    }
    return render(request, 'judge/register.html', context)
