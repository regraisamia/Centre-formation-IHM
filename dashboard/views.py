from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse
from student.models import Student
from configuration.models import Classes, Subjects
from user.models import User
from datetime import datetime, timedelta
import csv

@login_required
def dashboard(request):
    # Statistiques réelles
    total_students = Student.objects.count()
    active_students = Student.objects.filter(status=1).count()
    total_classes = Classes.objects.count()
    total_subjects = Subjects.objects.count()
    
    # Étudiants récents (derniers 30 jours)
    recent_students = Student.objects.filter(
        created_at__gte=datetime.now() - timedelta(days=30)
    ).select_related('classe', 'address').order_by('-created_at')[:5]
    
    context = {
        'total_students': total_students,
        'active_students': active_students,
        'total_classes': total_classes,
        'total_subjects': total_subjects,
        'recent_students': recent_students,
    }
    return render(request, 'modern_dashboard.html', context)

@login_required
def download_report(request):
    # Créer un rapport CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="rapport_etudiants.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Matricule', 'Prénom', 'Nom', 'Classe', 'Date Inscription'])
    
    students = Student.objects.select_related('classe').all()
    for student in students:
        writer.writerow([
            student.matricule,
            student.fname,
            student.lname,
            student.classe.classe_name if student.classe else 'Non assigné',
            student.created_at.strftime('%d/%m/%Y') if student.created_at else ''
        ])
    
    return response
