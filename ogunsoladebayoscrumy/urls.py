from os import name
from django.urls import path
from django.urls.conf import include
from . import views
app_name = 'ogunsoladebayoscrumy'
urlpatterns = [
    path('', views.index, name='index'),
    path('movegoal/<int:goal_id>', views.move_goal, name='movegoal'),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('slack/', views.slack)

]
