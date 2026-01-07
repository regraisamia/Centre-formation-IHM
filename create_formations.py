#!/usr/bin/env python
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from configuration.models import Formation, Classes

def create_formations():
    """Créer des formations de test"""
    
    formations_data = [
        {
            'name': 'Développement Web',
            'description': 'Formation complète en développement web moderne avec HTML, CSS, JavaScript, PHP et MySQL.',
            'duration_months': 6,
            'price': 3500.00,
            'max_students_per_class': 25
        },
        {
            'name': 'Marketing Digital',
            'description': 'Stratégies marketing digitales, SEO, réseaux sociaux et e-commerce.',
            'duration_months': 4,
            'price': 2800.00,
            'max_students_per_class': 20
        },
        {
            'name': 'Gestion de Projet',
            'description': 'Méthodologies Agile, Scrum, management d\'équipe et outils de gestion.',
            'duration_months': 3,
            'price': 2200.00,
            'max_students_per_class': 30
        },
        {
            'name': 'Comptabilité',
            'description': 'Formation complète en comptabilité générale et analytique avec logiciels spécialisés.',
            'duration_months': 5,
            'price': 3200.00,
            'max_students_per_class': 25
        },
        {
            'name': 'Bureautique',
            'description': 'Maîtrise des outils bureautiques: Word, Excel, PowerPoint, et outils collaboratifs.',
            'duration_months': 2,
            'price': 1200.00,
            'max_students_per_class': 30
        }
    ]
    
    print("Création des formations...")
    
    for formation_data in formations_data:
        formation, created = Formation.objects.get_or_create(
            name=formation_data['name'],
            defaults=formation_data
        )
        if created:
            print(f"Formation créée: {formation.name}")
        else:
            print(f"Formation existe déjà: {formation.name}")
    
    print(f"\nTotal formations: {Formation.objects.count()}")

if __name__ == '__main__':
    create_formations()
    print("Terminé!")