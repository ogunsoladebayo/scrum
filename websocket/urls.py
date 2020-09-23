from os import name
from django.urls import path
from django.urls.conf import include
from . import views
app_name = 'websocket'
urlpatterns = [
    path('test/', views.test, name='test'),
    path('connect/', views.connect, name='connect'),
    path('disconnect/', views.disconnect, name='disconnect'),
    path('send_message/', views.send_message, name='sendMessage'),
    path('get_messages/', views.get_messages, name='getMessages'),
]
