from django.urls import path
from . import views


urlpatterns = [
    path('', views.trainer_home_view, name='trainer'),

    # path for creating a new puzzle, button calls this in trainer_home.html
    path('play/new/', views.generate_and_play_puzzle, name='generate_puzzle'),

    # route to a puzzle. a user can create a new puzzle, or play a puzzle
    # created by someone else (probably by viewing their users home page)
    path('trainer/<int:puzzle_id>/', views.view_puzzle, name='view_puzzle'),
]
