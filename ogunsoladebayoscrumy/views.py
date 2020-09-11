from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ScrumyGoals, ScrumyHistory, GoalStatus
from random import randint

# Create your views here.


def get_grading_parameters(request):
    return HttpResponse(ScrumyGoals.objects.filter(goal_name='Learn Django'))


def move_goal(request, goal_id):
    try:
        obj = ScrumyGoals.objects.get(goal_id= goal_id)
    except Exception as e:
        return render(request, 'ogunsoladebayoscrumy/exception.html', {'error': 'A record with that goal id does not exist'})
    else:
        return HttpResponse(obj.goal_name)

def add_goal(request):
    status = GoalStatus.objects.get(status_name='Weekly Goal')
    user = User.objects.get(username='louis')
    ScrumyGoals.objects.create(goal_name='Keep Learning Django', goal_id=randint(
        1000, 9999), created_by='Louis', moved_by='Louis', goal_status=status, user=user)
    return HttpResponse('Done')


def home(request):
    goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    goal_name = ', '.join([goal.goal_name for goal in goals])
    goal_id = ', '.join([str(goal.goal_id) for goal in goals])
    user = ScrumyGoals.objects.get(goal_name = 'Learn Django').user
    # print
    delimeters = {'goal_name': goal_name, 'goal_id': goal_id, 'first_name': user}
    return render(request, 'ogunsoladebayoscrumy/home.html', delimeters)
