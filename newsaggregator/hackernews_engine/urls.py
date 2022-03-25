#from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'stories'
urlpatterns = [
    path('api/', views.WordCountApi.as_view()),
]