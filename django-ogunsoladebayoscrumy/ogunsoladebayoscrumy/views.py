from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ScrumyGoals, ScrumyHistory, GoalStatus
from random import randint

# Create your views here.


def get_grading_parameters(request):
    return HttpResponse(ScrumyGoals.objects.get(goal_name='Learn Django').goal_name)


def move_goal(request, goal_id):
    try:
        obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
        return render(request, 'ogunsoladebayoscrumy/exception.html', {'error': 'A record with that goal id does not exist'})
    else:
        return HttpResponse(obj.goal_name)


def add_goal(request):
    status = GoalStatus.objects.get(status_name='Daily Goal')
    user = User.objects.get(username='louis')
    ScrumyGoals.objects.create(goal_name='Keep Learning Django', goal_id=randint(
        1000, 9999), created_by='Louis', moved_by='Louis', goal_status=status, user=user)
    return HttpResponse('Done')


def home(request):
    weekly_status = GoalStatus.objects.get(status_name='Weekly Goal')
    daily_status = GoalStatus.objects.get(status_name='Daily Goal')
    verify_status = GoalStatus.objects.get(status_name='Verify Goal')
    done_status = GoalStatus.objects.get(status_name='Done Goal')

    users = User.objects.all()

    weekly_goals = weekly_status.scrumygoals_set.all()
    daily_goals = daily_status.scrumygoals_set.all()
    verify_goals = verify_status.scrumygoals_set.all()
    done_goals = done_status.scrumygoals_set.all()

    data = {'users': users, 'weekly_goals': weekly_goals, 'daily_goals': daily_goals,
            'verify_goals': verify_goals, 'done_goals': done_goals}

    return render(request, 'ogunsoladebayoscrumy/home.html', data)
