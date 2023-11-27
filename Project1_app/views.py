from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from Project1_app.models import Workout
from Project1_app.forms import WorkoutForm, createUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import WorkoutFilter


# Create your views here.


def index(request):
    # Render index.html
    workouts = Workout.objects.all()
    myFilter = WorkoutFilter(request.GET, queryset=workouts)
    workouts = myFilter.qs
    context = {'workouts': workouts, 'myFilter': myFilter}
    return render(request, 'Project1_app/base_template.html', context)


class CreatePage(generic.ListView):
    model = Workout


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username OR password incorrect')

    context = {}
    return render(request, 'Project1_app/login_page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form = createUserForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        #else:
            #messages.info('Missing Data. Please check input fields and try again')

    context = {'form': form}
    return render(request, 'Project1_app/register_page.html', context)


@login_required(login_url='login')
def createWorkout(request):
    form = WorkoutForm
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, "Project1_app/workout_form.html", context)


@login_required(login_url='login')
def updateWorkout(request, pk):
    workout = Workout.objects.get(id=pk)
    form = WorkoutForm(instance=workout)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "Project1_app/workout_form.html", context)


@login_required(login_url='login')
def deleteWorkout(request, pk):
    workout = Workout.objects.get(id=pk)
    if request.method == "POST":
        workout.delete()
        return redirect('/')
    context = {'item': workout}
    return render(request, "Project1_app/delete_workout.html", context)
