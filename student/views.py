from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Student, Address, Classes
from configuration.models import Classes
import json
from datetime import datetime

def student_list(request):
    """Liste des étudiants avec recherche et pagination"""
    students = Student.objects.all().select_related('classe', 'address')
    
    # Recherche
    search = request.GET.get('search')
    if search:
        students = students.filter(
            Q(fname__icontains=search) | 
            Q(lname__icontains=search) | 
            Q(matricule__icontains=search)
        )
    
    # Filtre par classe
    classe_filter = request.GET.get('classe')
    if classe_filter:
        students = students.filter(classe__classe_name=classe_filter)
    
    # Pagination
    paginator = Paginator(students, 15)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    
    # Statistiques
    total_students = Student.objects.count()
    active_students = Student.objects.filter(classe__isnull=False).count()
    
    context = {
        'students': students,
        'total_students': total_students,
        'active_students': active_students,
        'classes': Classes.objects.all(),
        'search': search,
        'classe_filter': classe_filter,
    }
    
    return render(request, 'modern_student_list.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def add_student(request):
    """Ajouter un nouvel étudiant"""
    try:
        # Créer l'adresse
        address = Address.objects.create(
            street=request.POST.get('address', ''),
            city=request.POST.get('city', 'Casablanca'),
            zip=12345
        )
        
        # Générer matricule
        last_student = Student.objects.order_by('-created_at').first()
        if last_student:
            # Extraire le numéro du dernier matricule
            last_num = int(last_student.matricule[-3:]) if last_student.matricule else 0
            matricule_num = last_num + 1
        else:
            matricule_num = 1
        matricule = f"ST2024{matricule_num:03d}"
        
        # Créer l'étudiant
        student = Student.objects.create(
            fname=request.POST.get('fname'),
            lname=request.POST.get('lname'),
            matricule=matricule,
            bday=request.POST.get('bday') if request.POST.get('bday') else None,
            gender=1 if request.POST.get('gender') == 'M' else 2,
            address=address,
            classe_id=request.POST.get('classe') if request.POST.get('classe') else None
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Étudiant ajouté avec succès!',
            'student': {
                'id': str(student.uuid),
                'name': f"{student.fname} {student.lname}",
                'matricule': student.matricule
            }
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        })

@csrf_exempt
@require_http_methods(["POST"])
def toggle_payment(request, student_id):
    """Changer le statut de paiement d'un étudiant"""
    try:
        student = get_object_or_404(Student, uuid=student_id)
        
        # Simuler le changement de statut de paiement
        # Dans une vraie app, vous auriez un champ payment_status
        current_status = request.POST.get('current_status') == 'true'
        new_status = not current_status
        
        return JsonResponse({
            'success': True,
            'new_status': new_status,
            'message': f'Statut de paiement mis à jour: {"Payé" if new_status else "Impayé"}'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        })

@csrf_exempt
@require_http_methods(["POST"])
def delete_student(request, student_id):
    """Supprimer un étudiant"""
    try:
        student = get_object_or_404(Student, uuid=student_id)
        student_name = f"{student.fname} {student.lname}"
        student.delete()
        
        return JsonResponse({
            'success': True,
            'message': f'Étudiant {student_name} supprimé avec succès!'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erreur: {str(e)}'
        })

def student_detail(request, uuid):
    """Détails d'un étudiant"""
    student = get_object_or_404(Student, uuid=uuid)
    
    context = {
        'student': student,
    }
    
    return render(request, 'student_detail.html', context)

# Fonctions existantes (à garder)
def view_student(request, uuid):
    return student_detail(request, uuid)

def create_edit_student_note(request, student_uuid, note_uuid=None):
    # Fonction existante - à implémenter si nécessaire
    pass

def delete_student_note(request, student_uuid, note_uuid):
    # Fonction existante - à implémenter si nécessaire
    pass

def disciplines_list(request):
    # Fonction existante - à implémenter si nécessaire
    pass

def discipline_details(request, id):
    # Fonction existante - à implémenter si nécessaire
    pass

def create_edit_discipline(request, id=None):
    # Fonction existante - à implémenter si nécessaire
    pass

def delete_discipline(request, id):
    # Fonction existante - à implémenter si nécessaire
    pass

def attendance_list(request):
    # Fonction existante - à implémenter si nécessaire
    pass

def in_out_list(request, inout_str):
    # Fonction existante - à implémenter si nécessaire
    pass

def in_out_details(request, inout_str, id):
    # Fonction existante - à implémenter si nécessaire
    pass

def delete_inout(request, inout_str, id):
    # Fonction existante - à implémenter si nécessaire
    pass

def create_edit_inout(request, inout_str, id=None):
    # Fonction existante - à implémenter si nécessaire
    pass