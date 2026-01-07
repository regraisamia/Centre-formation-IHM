#!/usr/bin/env python
import os
import sys
import django

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from configuration.models import Formation, Classes
import random

def assign_classes_to_formations():
    """Assigner les classes existantes aux formations"""
    
    formations = list(Formation.objects.all())
    classes = Classes.objects.all()
    
    print(f"Formations disponibles: {len(formations)}")
    print(f"Classes à assigner: {len(classes)}")
    
    if not formations:
        print("Aucune formation trouvée. Exécutez d'abord create_formations.py")
        return
    
    for classe in classes:
        if not classe.formation:
            # Assigner une formation aléatoire
            formation = random.choice(formations)
            classe.formation = formation
            classe.max_students = classe.max_students or 25
            classe.save()
            print(f"Classe {classe.classe_name} assignée à {formation.name}")
        else:
            print(f"Classe {classe.classe_name} déjà assignée à {classe.formation.name}")
    
    print("\nRésumé:")
    for formation in formations:
        count = formation.classes.count()
        print(f"- {formation.name}: {count} classe(s)")

if __name__ == '__main__':
    assign_classes_to_formations()
    print("Terminé!")