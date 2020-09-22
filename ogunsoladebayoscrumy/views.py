from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ScrumyGoals, ScrumyHistory, GoalStatus
from random import randint
from .forms import SignupForm, CreateGoalForm, MoveGoalForm
from django.contrib.auth import hashers
from django.contrib.auth.models import Group

# Create your views here.


def index(request):
    group = Group.objects.get(name='Developer')
    success = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = hashers.make_password(
                form.cleaned_data['password'])
            new_user.save()
            group.user_set.add(new_user)
            success = True
        else:
            success = False
    else:
        form = SignupForm()
    return render(request, 'ogunsoladebayoscrumy/index.html', {'form': form, 'success': success})


def move_goal(request, goal_id):
    success = False
    user = request.user
    role = Group.objects.get(user=user)
    obj = ScrumyGoals.objects.get(goal_id=goal_id)
    goal_user = str(obj.user)

    if request.method == 'POST':
        form = MoveGoalForm(request.POST, user=user, role=str(role), goal_user=goal_user)
        if form.is_valid():
            status = form.cleaned_data['goal_status']
            obj.goal_status = status
            obj.save()
            success = True
        else:
            success = False
    else:
        form = MoveGoalForm(user=user, role=str(role), goal_user=goal_user)
    return render(request, 'ogunsoladebayoscrumy/movegoal.html', {'form': form, 'success': success, 'role': str(role), 'goal': obj})


def add_goal(request):
    success = False
    user = request.user
    role = Group.objects.get(user=user)

    if request.method == 'POST':
        form = CreateGoalForm(request.POST, user=user)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.goal_id = randint(1000, 9999)
            form.save()
            success = True
        else:
            print(form.errors)
            success = False
            return HttpResponse(form.errors)
    else:
        form = CreateGoalForm(user=user)
    return render(request, 'ogunsoladebayoscrumy/addgoal.html', {'form': form, 'success': success, 'role': role})


def home(request):
    user = request.user
    role = Group.objects.get(user=user)
    weekly_status = GoalStatus.objects.get(status_name='Weekly Goal')
    daily_status = GoalStatus.objects.get(status_name='Daily Goal')
    verify_status = GoalStatus.objects.get(status_name='Verify Goal')
    done_status = GoalStatus.objects.get(status_name='Done Goal')

    users = User.objects.all()

    weekly_goals = weekly_status.scrumygoals_set.all()
    daily_goals = daily_status.scrumygoals_set.all()
    verify_goals = verify_status.scrumygoals_set.all()
    done_goals = done_status.scrumygoals_set.all()

    data = {'role': role, 'users': users, 'weekly_goals': weekly_goals, 'daily_goals': daily_goals,
            'verify_goals': verify_goals, 'done_goals': done_goals}

    return render(request, 'ogunsoladebayoscrumy/home.html', data)
