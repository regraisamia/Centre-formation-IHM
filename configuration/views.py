from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.contrib.auth import logout, authenticate, login
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from datetime import datetime, timedelta
from django.db.models import Count
import xlsxwriter

# Apps imports
from common.utils import *

# import models
from user.models import User
from configuration.models import Classes, Formation, Subjects
from student.models import Student

@login_required
def classes_list(request):
    """Liste des classes avec leurs formations"""
    classes = Classes.objects.select_related('formation').annotate(
        student_count=Count('student_classe')
    ).order_by('formation__name', 'classe_name')
    
    context = {
        'classes': classes,
        'formations': Formation.objects.all(),
        'total_classes': classes.count(),
        'total_students': Student.objects.count(),
    }
    return render(request, 'classes_list.html', context)

@login_required
def formations_list(request):
    """Liste des formations"""
    formations = Formation.objects.annotate(
        total_students=Count('classes__student_classe'),
        total_classes=Count('classes')
    ).order_by('name')
    
    context = {
        'formations': formations,
        'total_formations': formations.count(),
        'total_students': Student.objects.count(),
    }
    return render(request, 'formations_list.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def add_formation(request):
    """Ajouter une nouvelle formation"""
    try:
        formation = Formation.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description', ''),
            duration_months=int(request.POST.get('duration_months', 6)),
            price=float(request.POST.get('price', 0)),
            max_students_per_class=int(request.POST.get('max_students', 25))
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Formation ajoutée avec succès!',
            'formation': {
                'id': formation.id,
                'name': formation.name
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        })

@csrf_exempt
@require_http_methods(["POST"])
def add_classe(request):
    """Ajouter une nouvelle classe"""
    try:
        classe = Classes.objects.create(
            classe_name=request.POST.get('classe_name'),
            formation_id=request.POST.get('formation') if request.POST.get('formation') else None,
            max_students=int(request.POST.get('max_students', 25))
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Classe ajoutée avec succès!',
            'classe': {
                'id': classe.id,
                'name': classe.classe_name
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        })