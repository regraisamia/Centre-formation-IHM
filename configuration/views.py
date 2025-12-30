from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from datetime import datetime, timedelta
from django.db.models import Count
import xlsxwriter

# Apps imports
from common.utils import *

# import models
from user.models import User
from configuration.models import Classes
from student.models import Student

@login_required
def classes_list(request):
    classes_obj_list = Classes.objects.all()
    
    # Add statistics
    total_formations = classes_obj_list.count()
    total_students_enrolled = Student.objects.count()
    
    context = {
        'formations': classes_obj_list,
        'total_formations': total_formations,
        'total_students_enrolled': total_students_enrolled,
        'avg_duration': '4.5',
        'success_rate': '87'
    }
    
    return render(request, 'formations_list.html', context)
	