from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'
urlpatterns = [
    path('hello_world/',hello_world,name='hello_world'),
    path('hello_world1/', hello_world, name='111hello_world'),

]