from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson

# Create your views here.

@login_required(login_url='/login/')
def lessons_home_view(request):
    lessons = Lesson.objects.filter(order__gt=0).order_by('order')
    
    context = {
        'lessons': lessons,
    }
    return render(request, 'lessons/lessons_home.html', context)

def lesson_details(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)

    context = {
        'lesson': lesson
    }
    return render(request, 'lessons/lesson_detail.html', context)

