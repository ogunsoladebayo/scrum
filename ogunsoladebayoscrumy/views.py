from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ScrumyGoals, ScrumyHistory, GoalStatus
from random import randint

# Create your views here.


def get_grading_parameters(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name='Learn Django'))


def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal)


def add_goal(request):
    status = GoalStatus.objects.get(status_name='Weekly Goal')
    user = User.objects.get(username='louis')
    ScrumyGoals.objects.create(goal_name='Keep Learning Django', goal_id=randint(
        1000, 9999), created_by='Louis', moved_by='Louis', goal_status=status, user=user)
    return HttpResponse('Done')


def home(request):
    goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    goal = ', '.join([goal.goal_name for goal in goals])
    return(HttpResponse(goal))
