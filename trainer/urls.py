from django.urls import path
from . import views


urlpatterns = [
    path('', views.trainer_home_view, name='trainer'),

]
