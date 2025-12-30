import os
import django
from datetime import date
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from student.models import Student, Address
from configuration.models import Classes
from user.models import User

# Create more students
students_data = [
    {"fname": "Khalid", "lname": "Benali", "matricule": "ST20240011"},
    {"fname": "Maryam", "lname": "Chraibi", "matricule": "ST20240012"},
    {"fname": "Rachid", "lname": "Benjelloun", "matricule": "ST20240013"},
    {"fname": "Salma", "lname": "Sefrioui", "matricule": "ST20240014"},
    {"fname": "Abdelaziz", "lname": "Benkirane", "matricule": "ST20240015"},
]

# Create trainers
trainers_data = [
    {"first_name": "Mohammed", "last_name": "Alami", "username": "m.alami"},
    {"first_name": "Fatima", "last_name": "Bennani", "username": "f.bennani"},
    {"first_name": "Youssef", "last_name": "Tazi", "username": "y.tazi"},
]

admin_user = User.objects.get(username='admin')
formations = list(Classes.objects.all())

# Create addresses
cities = ["Casablanca", "Rabat", "Fes", "Marrakech", "Agadir"]
addresses = []
for city in cities:
    addr, created = Address.objects.get_or_create(
        street=f"123 Avenue Mohammed V",
        city=city,
        defaults={'zip': 20000}
    )
    addresses.append(addr)

# Add students
for student_data in students_data:
    student, created = Student.objects.get_or_create(
        matricule=student_data["matricule"],
        defaults={
            'fname': student_data["fname"],
            'lname': student_data["lname"],
            'bday': date(1995, random.randint(1, 12), random.randint(1, 28)),
            'gender': random.choice([1, 2]),
            'status': 1,
            'classe': random.choice(formations) if formations else None,
            'address': random.choice(addresses),
            'creator': admin_user
        }
    )
    if created:
        print(f"Created student: {student_data['fname']} {student_data['lname']}")

# Add trainers
for trainer_data in trainers_data:
    user, created = User.objects.get_or_create(
        username=trainer_data['username'],
        defaults={
            'first_name': trainer_data['first_name'],
            'last_name': trainer_data['last_name'],
            'email': f"{trainer_data['username']}@cfp-almanar.ma",
            'is_staff': True,
            'is_active': True,
            'role': 2
        }
    )
    if created:
        user.set_password('trainer123')
        user.save()
        print(f"Created trainer: {trainer_data['first_name']} {trainer_data['last_name']}")

print(f"Total students: {Student.objects.count()}")
print(f"Total trainers: {User.objects.filter(role=2).count()}")
print(f"Total formations: {Classes.objects.count()}")
print("Data creation completed!")