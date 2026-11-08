from django.urls import path
from . import views


urlpatterns = [
    path('', views.lessons_home_view, name='lessons'),
    path('<slug:slug>/', views.lesson_details, name='lesson_detail'),
]
