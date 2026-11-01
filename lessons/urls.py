from django.urls import path
from . import views


urlpatterns = [
    path('', views.lessons_home_view, name='lessons'),
]
