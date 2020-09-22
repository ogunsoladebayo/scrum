from os import name
from django.urls import path
from django.urls.conf import include
from . import views
app_name = 'ogunsoladebayoscrumy'
urlpatterns = [
    path('', views.get_grading_parameters, name='index'),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal/', views.add_goal),
    path('home/', views.home),
    path('accounts/', include('django.contrib.auth.urls'))

]
