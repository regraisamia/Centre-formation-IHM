#!/usr/bin/env python
"""
Comprehensive data population script for Centre de Formation Al Manar
Run this after setting up the database to populate with realistic Moroccan data
"""

import os
import sys
import django
from datetime import datetime, timedelta
import random

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from django.contrib.auth import get_user_model
from student.models import Student, Address, Parents, Student_Notes, Note_Category, Attendances
from configuration.models import Classes, Subjects, Location, SubjectsSet
from user.models import User

def create_admin_user():
    """Create admin user"""
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@almanar.ma',
            password='admin123',
            first_name='Administrateur',
            last_name='Al Manar'
        )
        print("✓ Admin user created (username: admin, password: admin123)")
    else:
        print("✓ Admin user already exists")

def create_locations():
    """Create training locations"""
    locations_data = [
        ('Salle A1', 30),
        ('Salle B2', 20),
        ('Salle C3', 50),
        ('Lab Info', 25),
        ('Amphithéâtre', 100),
    ]
    
    for name, capacity in locations_data:
        Location.objects.get_or_create(
            location=name,
            defaults={'capacity': capacity}
        )
    print("✓ Training locations created")

def create_subjects():
    """Create subjects"""
    subjects_data = [
        ('DEV001', 'Développement Web', 'HTML, CSS, JavaScript, PHP, MySQL'),
        ('MKT001', 'Marketing Digital', 'SEO, SEM, Réseaux sociaux, Analytics'),
        ('GPR001', 'Gestion de Projet', 'Méthodologies Agile, Scrum, Management'),
        ('DES001', 'Design Graphique', 'Photoshop, Illustrator, InDesign'),
        ('CPT001', 'Comptabilité', 'Comptabilité générale et analytique'),
        ('BUR001', 'Bureautique', 'Word, Excel, PowerPoint, Access'),
        ('ANG001', 'Anglais Professionnel', 'Anglais des affaires et technique'),
        ('COM001', 'Communication', 'Techniques de communication et présentation'),
        ('ENT001', 'Entrepreneuriat', 'Création et gestion d\'entreprise'),
        ('IA001', 'Intelligence Artificielle', 'Machine Learning, Python, Data Science'),
    ]
    
    for code, name, desc in subjects_data:
        Subjects.objects.get_or_create(
            code=code,
            defaults={'name': name, 'description': desc}
        )
    print("✓ Subjects created")

def create_formations():
    """Create training programs (Classes)"""
    formations_data = [
        'Développement Web Full Stack',
        'Marketing Digital Avancé',
        'Gestion de Projet Certifiante',
        'Design Graphique Professionnel',
        'Comptabilité et Finance',
        'Bureautique Avancée',
        'Intelligence Artificielle',
        'Entrepreneuriat et Innovation',
    ]
    
    for name in formations_data:
        Classes.objects.get_or_create(
            classe_name=name,
            defaults={'is_active': True}
        )
    print("✓ Training programs created")

def create_addresses():
    """Create addresses for students"""
    moroccan_cities = [
        'Casablanca', 'Rabat', 'Fès', 'Marrakech', 'Agadir', 'Tanger',
        'Meknès', 'Oujda', 'Kenitra', 'Tétouan', 'Safi', 'Mohammedia'
    ]
    
    addresses = []
    for i in range(50):
        city = random.choice(moroccan_cities)
        address = Address.objects.create(
            street=f"Rue {random.randint(1, 200)} {random.choice(['Hassan II', 'Mohammed V', 'Al Massira', 'Zerktouni', 'Anfa'])}",
            city=city,
            zip=random.randint(10000, 99999)
        )
        addresses.append(address)
    
    print("✓ Addresses created")
    return addresses

def create_students(addresses):
    """Create students with Moroccan names"""
    moroccan_first_names = [
        'Mohammed', 'Fatima', 'Ahmed', 'Aicha', 'Youssef', 'Khadija',
        'Omar', 'Zineb', 'Hassan', 'Salma', 'Karim', 'Nadia',
        'Rachid', 'Laila', 'Abdelaziz', 'Samira', 'Mustapha', 'Houda',
        'Said', 'Malika', 'Khalid', 'Rajae', 'Abderrahim', 'Souad',
        'Brahim', 'Amina', 'Driss', 'Latifa', 'Hamid', 'Zahra'
    ]
    
    moroccan_last_names = [
        'Alami', 'Bennani', 'Tazi', 'Fassi', 'Idrissi', 'Kettani',
        'Berrada', 'Chraibi', 'Benali', 'Lahlou', 'Benjelloun', 'Sefrioui',
        'Mekouar', 'Benkirane', 'Lamrani', 'Benabdellah', 'Filali', 'Benomar',
        'Cherkaoui', 'Benslimane', 'Bensaid', 'Bensouda', 'Bentaleb', 'Benyahia'
    ]
    
    formations = list(Classes.objects.all())
    
    for i in range(30):
        first_name = random.choice(moroccan_first_names)
        last_name = random.choice(moroccan_last_names)
        
        # Generate matricule
        matricule = f"ST2024{str(i+1).zfill(4)}"
        
        # Random birth date (18-35 years old)
        birth_date = datetime.now().date() - timedelta(days=random.randint(18*365, 35*365))
        
        student = Student.objects.create(
            fname=first_name,
            lname=last_name,
            matricule=matricule,
            bday=birth_date,
            gender=random.choice([1, 2]),  # 1=Male, 2=Female based on GENDER choices
            address=random.choice(addresses),
            classe=random.choice(formations) if random.random() > 0.1 else None  # 90% have a formation
        )
    
    print("✓ Students created")

def create_note_categories():
    """Create note categories"""
    categories = [
        'Examen Final',
        'Contrôle Continu',
        'Projet',
        'Participation',
        'Stage',
    ]
    
    for name in categories:
        Note_Category.objects.get_or_create(
            name=name
        )
    
    print("✓ Note categories created")

def create_sample_notes():
    """Create sample notes for students"""
    students = Student.objects.all()
    categories = Note_Category.objects.all()
    
    for student in students[:15]:  # Add notes for first 15 students
        for category in categories:
            if random.random() > 0.3:  # 70% chance of having a note
                Student_Notes.objects.create(
                    student=student,
                    note_category=category,
                    title=f"Note {category.name}",
                    content=f"Note pour {student.fname} {student.lname} en {category.name}"
                )
    
    print("✓ Sample notes created")

def create_attendance_records():
    """Create attendance records"""
    students = Student.objects.filter(classe__isnull=False)
    
    # Create attendance for last 30 days
    for i in range(30):
        date = datetime.now().date() - timedelta(days=i)
        
        for student in students[:10]:  # First 10 active students
            if random.random() > 0.2:  # 80% attendance rate
                attendance_type = random.choice([0, 1, 2])  # Based on ATTENDANCES_TYPE
                Attendances.objects.get_or_create(
                    student=student,
                    start_date=date,
                    defaults={'type': attendance_type}
                )
    
    print("✓ Attendance records created")

def main():
    """Main function to populate all data"""
    print("🚀 Starting data population for Centre de Formation Al Manar...")
    print("=" * 60)
    
    try:
        create_admin_user()
        create_locations()
        create_subjects()
        create_formations()
        addresses = create_addresses()
        create_students(addresses)
        create_note_categories()
        create_sample_notes()
        create_attendance_records()
        
        print("=" * 60)
        print("✅ Data population completed successfully!")
        print("\n📊 Summary:")
        print(f"   • Students: {Student.objects.count()}")
        print(f"   • Formations: {Classes.objects.count()}")
        print(f"   • Subjects: {Subjects.objects.count()}")
        print(f"   • Locations: {Location.objects.count()}")
        print(f"   • Notes: {Student_Notes.objects.count()}")
        print(f"   • Attendance records: {Attendances.objects.count()}")
        print("\n🔐 Admin Login:")
        print("   Username: admin")
        print("   Password: admin123")
        print("   URL: http://localhost:8000/admin/")
        
    except Exception as e:
        print(f"❌ Error during data population: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()