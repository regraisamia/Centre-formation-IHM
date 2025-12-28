from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from student.models import Student
from configuration.models import Classes
from user.models import User

@login_required
def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'active_students': Student.objects.filter(status=1).count(),
        'total_formations': Classes.objects.count(),
        'total_trainers': User.objects.filter(role=2).count(),
    }
    return render(request, 'modern_dashboard.html', context)
