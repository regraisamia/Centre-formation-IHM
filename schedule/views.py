from django.shortcuts import render, get_object_or_404, redirect
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

# Apps imports
from common.utils import *

# import models
from schedule.models import Schedule
from configuration.models import Classes
from student.models import Student
from user.models import User

@login_required
def schedule_list(request):
    context = {
        'total_sessions': 45,
        'active_formations': 8,
        'active_trainers': 12,
        'available_rooms': 6
    }
    return render(request, 'schedule_list.html', context)
		
		
		
		

	
