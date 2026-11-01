from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def trainer_home_view(request):
    return render(request, 'trainer/trainer_home.html')

