from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ScrumyGoals, ScrumyHistory, GoalStatus

# Create your views here.


def get_grading_parameters(request):
    return HttpResponse('This is a Scrum Application')


def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.filter(goal_id=goal_id)
    return HttpResponse(goal)
