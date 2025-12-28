import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from student.models import Student, Address
from configuration.models import Classes
from django.contrib.auth import get_user_model

User = get_user_model()

# Create some addresses
addresses = []
cities = ["Casablanca", "Rabat", "Fès", "Marrakech", "Agadir"]
for city in cities:
    addr, created = Address.objects.get_or_create(
        street=f"123 Rue Mohammed V",
        city=city,
        defaults={'zip': 20000}
    )
    addresses.append(addr)

# Create some classes
formations = [
    "Développement Web",
    "Marketing Digital", 
    "Gestion de Projet",
    "Design Graphique",
    "Comptabilité"
]

classes = []
for formation in formations:
    classe, created = Classes.objects.get_or_create(
        classe_name=formation
    )
    classes.append(classe)

# Get admin user
admin_user = User.objects.get(username='admin')

# Create sample students
students_data = [
    {"fname": "Mohammed", "lname": "Alami", "matricule": "ST20240001"},
    {"fname": "Fatima", "lname": "Bennani", "matricule": "ST20240002"},
    {"fname": "Youssef", "lname": "Tazi", "matricule": "ST20240003"},
    {"fname": "Aicha", "lname": "Fassi", "matricule": "ST20240004"},
    {"fname": "Omar", "lname": "Idrissi", "matricule": "ST20240005"},
    {"fname": "Khadija", "lname": "Kettani", "matricule": "ST20240006"},
    {"fname": "Ahmed", "lname": "Berrada", "matricule": "ST20240007"},
    {"fname": "Zahra", "lname": "Lahlou", "matricule": "ST20240008"},
    {"fname": "Khalid", "lname": "Benali", "matricule": "ST20240009"},
    {"fname": "Maryam", "lname": "Chraibi", "matricule": "ST20240010"},
]

import random

for student_data in students_data:
    student, created = Student.objects.get_or_create(
        matricule=student_data["matricule"],
        defaults={
            'fname': student_data["fname"],
            'lname': student_data["lname"],
            'bday': date(1995, random.randint(1, 12), random.randint(1, 28)),
            'gender': random.choice([1, 2]),
            'status': 1,
            'classe': random.choice(classes),
            'address': random.choice(addresses),
            'creator': admin_user
        }
    )
    if created:
        print(f"Created student: {student_data['fname']} {student_data['lname']}")

print(f"Total students in database: {Student.objects.count()}")
print(f"Total classes in database: {Classes.objects.count()}")