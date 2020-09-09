from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_grading_parameters),
    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal/', views.add_goal),
    path('home/', views.home)
]
