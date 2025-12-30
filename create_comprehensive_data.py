import os
import django
from datetime import date, datetime
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from student.models import Student, Address, Parents, Relationship
from configuration.models import Classes, Subjects
from user.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Moroccan trainer data
trainers_data = [
    {"first_name": "Mohammed", "last_name": "Alami", "specialization": "Développement Web", "email": "m.alami@cfp-almanar.ma"},
    {"first_name": "Fatima", "last_name": "Bennani", "specialization": "Marketing Digital", "email": "f.bennani@cfp-almanar.ma"},
    {"first_name": "Youssef", "last_name": "Tazi", "specialization": "Design Graphique", "email": "y.tazi@cfp-almanar.ma"},
    {"first_name": "Aicha", "last_name": "Fassi", "specialization": "Gestion de Projet", "email": "a.fassi@cfp-almanar.ma"},
    {"first_name": "Omar", "last_name": "Idrissi", "specialization": "Comptabilité", "email": "o.idrissi@cfp-almanar.ma"},
    {"first_name": "Khadija", "last_name": "Kettani", "specialization": "Ressources Humaines", "email": "k.kettani@cfp-almanar.ma"},
    {"first_name": "Ahmed", "last_name": "Berrada", "specialization": "Cybersécurité", "email": "a.berrada@cfp-almanar.ma"},
    {"first_name": "Zahra", "last_name": "Lahlou", "specialization": "Intelligence Artificielle", "email": "z.lahlou@cfp-almanar.ma"},
]

# More Moroccan students
additional_students = [
    {"fname": "Khalid", "lname": "Benali", "matricule": "ST20240011"},
    {"fname": "Maryam", "lname": "Chraibi", "matricule": "ST20240012"},
    {"fname": "Rachid", "lname": "Benjelloun", "matricule": "ST20240013"},
    {"fname": "Salma", "lname": "Sefrioui", "matricule": "ST20240014"},
    {"fname": "Abdelaziz", "lname": "Benkirane", "matricule": "ST20240015"},
    {"fname": "Nadia", "lname": "Lamrani", "matricule": "ST20240016"},
    {"fname": "Mustapha", "lname": "Filali", "matricule": "ST20240017"},
    {"fname": "Laila", "lname": "Benabdellah", "matricule": "ST20240018"},
    {"fname": "Said", "lname": "Benomar", "matricule": "ST20240019"},
    {"fname": "Souad", "lname": "Benslimane", "matricule": "ST20240020"},
    {"fname": "Brahim", "lname": "Bensaid", "matricule": "ST20240021"},
    {"fname": "Rajae", "lname": "Bentaleb", "matricule": "ST20240022"},
    {"fname": "Abdellah", "lname": "Benyahia", "matricule": "ST20240023"},
    {"fname": "Zineb", "lname": "Bensouda", "matricule": "ST20240024"},
    {"fname": "Jamal", "lname": "El Alaoui", "matricule": "ST20240025"},
]

# Moroccan formations with detailed info
formations_detailed = [
    {"name": "Développement Web Full Stack", "description": "Formation complète en développement web moderne"},
    {"name": "Marketing Digital Avancé", "description": "Stratégies marketing digitales et réseaux sociaux"},
    {"name": "Design Graphique Professionnel", "description": "Adobe Creative Suite et identité visuelle"},
    {"name": "Gestion de Projet Agile", "description": "Méthodologies Agile, Scrum et leadership"},
    {"name": "Comptabilité et Finance", "description": "Comptabilité générale et fiscalité marocaine"},
    {"name": "Ressources Humaines", "description": "Recrutement et gestion des talents"},
    {"name": "Cybersécurité", "description": "Sécurité informatique et ethical hacking"},
    {"name": "Intelligence Artificielle", "description": "Machine Learning et Deep Learning"},
    {"name": "E-commerce", "description": "Création et gestion de boutiques en ligne"},
    {"name": "Langues Étrangères", "description": "Anglais, Français et Espagnol business"},
]

# Moroccan cities for addresses
moroccan_cities = [
    "Casablanca", "Rabat", "Fès", "Marrakech", "Agadir", "Tanger", 
    "Meknès", "Oujda", "Kenitra", "Tétouan", "Safi", "Mohammedia"
]

def create_trainers():
    """Create trainer user accounts"""
    print("Creating trainers...")
    
    for trainer_data in trainers_data:
        username = f"{trainer_data['first_name'].lower()}.{trainer_data['last_name'].lower()}"
        
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'first_name': trainer_data['first_name'],
                'last_name': trainer_data['last_name'],
                'email': trainer_data['email'],
                'is_staff': True,
                'is_active': True,
                'role': 2  # Teacher role
            }
        )
        
        if created:
            user.set_password('trainer123')
            user.save()
            print(f"  ✓ Created trainer: {trainer_data['first_name']} {trainer_data['last_name']}")

def create_detailed_formations():
    """Create detailed formations"""
    print("Creating detailed formations...")
    
    for formation in formations_detailed:
        classe, created = Classes.objects.get_or_create(
            classe_name=formation['name']
        )
        if created:
            print(f"  ✓ Created formation: {formation['name']}")

def create_more_students():
    """Create additional students"""
    print("Creating additional students...")
    
    admin_user = User.objects.get(username='admin')
    formations = list(Classes.objects.all())
    
    # Create more addresses
    addresses = []
    for city in moroccan_cities:
        for i in range(2):
            street = f"{random.randint(1, 999)} {random.choice(['Rue Hassan II', 'Avenue Mohammed V', 'Boulevard Al Massira', 'Rue Zerktouni'])}"
            addr, created = Address.objects.get_or_create(
                street=street,
                city=city,
                defaults={'zip': random.randint(10000, 99999)}
            )
            addresses.append(addr)
    
    for student_data in additional_students:
        student, created = Student.objects.get_or_create(
            matricule=student_data["matricule"],
            defaults={
                'fname': student_data["fname"],
                'lname': student_data["lname"],
                'bday': date(random.randint(1995, 2005), random.randint(1, 12), random.randint(1, 28)),
                'gender': random.choice([1, 2]),
                'status': random.choice([1, 1, 1, 4]),  # Mostly active, some graduated
                'classe': random.choice(formations) if formations else None,
                'address': random.choice(addresses) if addresses else None,
                'creator': admin_user,
                'comment': f'Téléphone: +212 {random.choice([6, 7])} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)} {random.randint(10, 99)}'
            }
        )
        
        if created:
            print(f"  ✓ Created student: {student_data['fname']} {student_data['lname']}")

def create_parents():
    """Create parent records for students"""
    print("Creating parents...")
    
    admin_user = User.objects.get(username='admin')
    students = Student.objects.all()
    
    moroccan_parent_names = [
        ("Mohammed", "Alami"), ("Fatima", "Bennani"), ("Ahmed", "Tazi"),
        ("Aicha", "Fassi"), ("Omar", "Idrissi"), ("Khadija", "Kettani"),
        ("Youssef", "Berrada"), ("Maryam", "Lahlou"), ("Khalid", "Benali"),
        ("Nadia", "Chraibi"), ("Said", "Benjelloun"), ("Laila", "Sefrioui")
    ]
    
    for student in students[:15]:  # Create parents for first 15 students
        # Create father
        father_name = random.choice(moroccan_parent_names)
        father, created = Parents.objects.get_or_create(
            fname=father_name[0],
            lname=student.lname,  # Same family name
            defaults={
                'bday': date(random.randint(1960, 1980), random.randint(1, 12), random.randint(1, 28)),
                'gender': 1,  # Male
                'status': 1,  # Active
                'address': student.address,
                'creator': admin_user
            }
        )
        
        if created:
            # Create relationship
            Relationship.objects.get_or_create(
                student=student,
                parent=father,
                defaults={
                    'relation': 1,  # Father
                    'is_ICE': True,
                    'is_InCharge': True
                }
            )
            print(f"  ✓ Created father for {student.fname}: {father.fname} {father.lname}")

def create_subjects():
    """Create subjects for formations"""
    print("Creating subjects...")
    
    subjects_data = [
        {"code": "HTML-CSS", "name": "HTML et CSS"},
        {"code": "JS", "name": "JavaScript"},
        {"code": "PHP", "name": "PHP et MySQL"},
        {"code": "REACT", "name": "React.js"},
        {"code": "SEO", "name": "Référencement SEO"},
        {"code": "SEM", "name": "Publicité en ligne"},
        {"code": "SOCIAL", "name": "Réseaux sociaux"},
        {"code": "PS", "name": "Adobe Photoshop"},
        {"code": "AI", "name": "Adobe Illustrator"},
        {"code": "AGILE", "name": "Méthodologie Agile"},
        {"code": "SCRUM", "name": "Framework Scrum"},
        {"code": "COMPTA", "name": "Comptabilité générale"},
    ]
    
    for subject_data in subjects_data:
        subject, created = Subjects.objects.get_or_create(
            code=subject_data['code'],
            defaults={'name': subject_data['name']}
        )
        if created:
            print(f"  ✓ Created subject: {subject_data['name']}")

def main():
    """Main function to create all data"""
    print("🇲🇦 Creating comprehensive Moroccan training center data...")
    
    create_trainers()
    create_detailed_formations()
    create_more_students()
    create_parents()
    create_subjects()
    
    # Final statistics
    total_students = Student.objects.count()
    total_trainers = User.objects.filter(role=2).count()
    total_formations = Classes.objects.count()
    total_parents = Parents.objects.count()
    total_subjects = Subjects.objects.count()
    
    print(f"\n✅ Data creation completed!")
    print(f"📊 Students: {total_students}")
    print(f"👨🏫 Trainers: {total_trainers}")
    print(f"🎓 Formations: {total_formations}")
    print(f"👨👩 Parents: {total_parents}")
    print(f"📚 Subjects: {total_subjects}")

if __name__ == "__main__":
    main()