from django.urls import path
from . import views


urlpatterns = [
    path('', views.famous_home_view, name='famous'),
]
