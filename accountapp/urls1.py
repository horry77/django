from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'
urlpatterns = [
    path('hello_world111/',hello_world,name='hello_worl1111111d'),

]
