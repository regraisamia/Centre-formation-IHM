#!/usr/bin/env python
"""
Complete Setup Script for StudX Training Center Management System
This script will:
1. Create the MySQL database
2. Run migrations
3. Create a superuser
4. Populate with sample Moroccan data
"""

import os
import sys
import django
import mysql.connector
from mysql.connector import Error

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line
from student.models import Student, Address, Parents, Relationship
from configuration.models import Classes, Subjects, SubjectsSet, Location
from datetime import datetime, date
import random

User = get_user_model()

def create_database():
    """Create MySQL database if it doesn't exist"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Change if you have a password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS studx_database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("✓ Database 'studx_database' created successfully")
            cursor.close()
            connection.close()
            
    except Error as e:
        print(f"✗ Error creating database: {e}")
        return False
    return True

def run_migrations():
    """Run Django migrations"""
    try:
        print("Running migrations...")
        execute_from_command_line(['manage.py', 'makemigrations'])
        execute_from_command_line(['manage.py', 'migrate'])
        print("✓ Migrations completed successfully")
        return True
    except Exception as e:
        print(f"✗ Error running migrations: {e}")
        return False

def create_superuser():
    """Create superuser if it doesn't exist"""
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@almanar.ma',
                password='admin123',
                first_name='Administrateur',
                last_name='Al Manar'
            )
            print("✓ Superuser created: username='admin', password='admin123'")
        else:
            print("✓ Superuser already exists")
        return True
    except Exception as e:
        print(f"✗ Error creating superuser: {e}")
        return False

def create_sample_data():
    """Create sample data for the training center"""
    try:
        print("Creating sample data...")
        
        # Create Locations
        locations = [
            {'name': 'Salle A - Informatique', 'description': 'Salle équipée de 20 ordinateurs'},
            {'name': 'Salle B - Formation', 'description': 'Salle de formation générale'},
            {'name': 'Laboratoire', 'description': 'Laboratoire de pratique'},
            {'name': 'Amphithéâtre', 'description': 'Grande salle de conférence'},
        ]
        
        for loc_data in locations:
            Location.objects.get_or_create(
                location_name=loc_data['name'],
                defaults={'location_description': loc_data['description']}
            )
        
        # Create Subjects
        subjects_data = [
            {'name': 'Développement Web Frontend', 'desc': 'HTML, CSS, JavaScript, React'},
            {'name': 'Développement Web Backend', 'desc': 'PHP, Python, Node.js, Bases de données'},
            {'name': 'Marketing Digital', 'desc': 'SEO, SEM, Réseaux sociaux, Analytics'},
            {'name': 'Gestion de Projet', 'desc': 'Méthodologies Agile, Scrum, Management'},
            {'name': 'Design Graphique', 'desc': 'Photoshop, Illustrator, InDesign'},
            {'name': 'Comptabilité', 'desc': 'Comptabilité générale et analytique'},
            {'name': 'Ressources Humaines', 'desc': 'Gestion RH, Recrutement, Formation'},
            {'name': 'Intelligence Artificielle', 'desc': 'Machine Learning, Deep Learning'},
        ]
        
        created_subjects = []\n        for subj_data in subjects_data:\n            subject, created = Subjects.objects.get_or_create(\n                subject_name=subj_data['name'],\n                defaults={'subject_description': subj_data['desc']}\n            )\n            created_subjects.append(subject)\n        \n        # Create Subject Sets\n        subject_sets = [\n            {\n                'name': 'Formation Développement Web Complet',\n                'subjects': ['Développement Web Frontend', 'Développement Web Backend']\n            },\n            {\n                'name': 'Formation Marketing Digital',\n                'subjects': ['Marketing Digital', 'Design Graphique']\n            },\n            {\n                'name': 'Formation Gestion d\\'Entreprise',\n                'subjects': ['Gestion de Projet', 'Comptabilité', 'Ressources Humaines']\n            }\n        ]\n        \n        for set_data in subject_sets:\n            subject_set, created = SubjectsSet.objects.get_or_create(\n                subject_set_name=set_data['name']\n            )\n            if created:\n                for subj_name in set_data['subjects']:\n                    try:\n                        subject = Subjects.objects.get(subject_name=subj_name)\n                        subject_set.subjects.add(subject)\n                    except Subjects.DoesNotExist:\n                        pass\n        \n        # Create Classes (Formations)\n        formations = [\n            {\n                'name': 'Développement Web Full Stack',\n                'description': 'Formation complète en développement web moderne avec React et Django'\n            },\n            {\n                'name': 'Marketing Digital Avancé',\n                'description': 'Maîtrisez les outils et stratégies du marketing digital'\n            },\n            {\n                'name': 'Gestion de Projet Agile',\n                'description': 'Apprenez les méthodologies agiles et le management de projet'\n            },\n            {\n                'name': 'Design UX/UI',\n                'description': 'Conception d\\'interfaces utilisateur modernes et ergonomiques'\n            },\n            {\n                'name': 'Intelligence Artificielle',\n                'description': 'Introduction au Machine Learning et Deep Learning'\n            }\n        ]\n        \n        created_classes = []\n        for form_data in formations:\n            classe, created = Classes.objects.get_or_create(\n                classe_name=form_data['name'],\n                defaults={'classe_description': form_data['description']}\n            )\n            created_classes.append(classe)\n        \n        # Create Addresses\n        moroccan_cities = [\n            'Casablanca', 'Rabat', 'Fès', 'Marrakech', 'Agadir', 'Tanger',\n            'Meknès', 'Oujda', 'Kenitra', 'Tétouan', 'Safi', 'Mohammedia'\n        ]\n        \n        addresses = []\n        for i in range(20):\n            address = Address.objects.create(\n                street=f\"{random.randint(1, 999)} Rue {random.choice(['Hassan II', 'Mohammed V', 'Al Massira', 'Zerktouni', 'Anfa'])}\",\n                city=random.choice(moroccan_cities),\n                zip_code=f\"{random.randint(10000, 99999)}\",\n                country='Maroc'\n            )\n            addresses.append(address)\n        \n        # Create Parents\n        moroccan_first_names_male = [\n            'Mohammed', 'Ahmed', 'Youssef', 'Omar', 'Hassan', 'Khalid', 'Abdelaziz',\n            'Rachid', 'Mustapha', 'Abderrahim', 'Said', 'Karim', 'Noureddine'\n        ]\n        \n        moroccan_first_names_female = [\n            'Fatima', 'Aicha', 'Khadija', 'Zineb', 'Amina', 'Laila', 'Nadia',\n            'Samira', 'Malika', 'Houda', 'Siham', 'Rajae', 'Btissam'\n        ]\n        \n        moroccan_last_names = [\n            'Alami', 'Bennani', 'Tazi', 'Fassi', 'Idrissi', 'Kettani', 'Berrada',\n            'Lahlou', 'Benali', 'Chraibi', 'Benjelloun', 'Sefrioui', 'Mekouar'\n        ]\n        \n        professions = [\n            'Ingénieur', 'Médecin', 'Professeur', 'Commerçant', 'Fonctionnaire',\n            'Avocat', 'Architecte', 'Pharmacien', 'Entrepreneur', 'Consultant'\n        ]\n        \n        parents = []\n        for i in range(30):\n            gender = random.choice(['M', 'F'])\n            first_name = random.choice(moroccan_first_names_male if gender == 'M' else moroccan_first_names_female)\n            \n            parent = Parents.objects.create(\n                fname=first_name,\n                lname=random.choice(moroccan_last_names),\n                cin=f\"{random.choice(['A', 'B', 'C', 'D'])}{random.randint(100000, 999999)}\",\n                profession=random.choice(professions),\n                address=random.choice(addresses)\n            )\n            parents.append(parent)\n        \n        # Create Students\n        student_first_names_male = [\n            'Amine', 'Youssef', 'Mehdi', 'Hamza', 'Othmane', 'Ismail', 'Ayoub',\n            'Zakaria', 'Anass', 'Bilal', 'Tarik', 'Saad', 'Hicham'\n        ]\n        \n        student_first_names_female = [\n            'Salma', 'Imane', 'Yasmine', 'Dounia', 'Rim', 'Ghita', 'Manal',\n            'Chaimae', 'Hajar', 'Wissal', 'Loubna', 'Sanae', 'Ikram'\n        ]\n        \n        for i in range(50):\n            gender = random.choice(['M', 'F'])\n            first_name = random.choice(student_first_names_male if gender == 'M' else student_first_names_female)\n            \n            # Generate birth date (18-30 years old)\n            birth_year = random.randint(1994, 2006)\n            birth_month = random.randint(1, 12)\n            birth_day = random.randint(1, 28)\n            \n            student = Student.objects.create(\n                fname=first_name,\n                lname=random.choice(moroccan_last_names),\n                cin=f\"{random.choice(['A', 'B', 'C', 'D', 'E'])}{random.randint(100000, 999999)}\",\n                birth_date=date(birth_year, birth_month, birth_day),\n                gender=gender,\n                matricule=f\"ST2024{str(i+1).zfill(3)}\",\n                address=random.choice(addresses),\n                classe=random.choice(created_classes) if random.random() > 0.1 else None  # 90% have a class\n            )\n            \n            # Create parent relationship\n            if parents and random.random() > 0.2:  # 80% have parent info\n                parent = random.choice(parents)\n                Relationship.objects.create(\n                    student=student,\n                    parent=parent,\n                    relationship_type=random.choice(['Père', 'Mère', 'Tuteur'])\n                )\n        \n        print(f\"✓ Sample data created successfully:\")\n        print(f\"  - {Location.objects.count()} locations\")\n        print(f\"  - {Subjects.objects.count()} subjects\")\n        print(f\"  - {SubjectsSet.objects.count()} subject sets\")\n        print(f\"  - {Classes.objects.count()} formations\")\n        print(f\"  - {Address.objects.count()} addresses\")\n        print(f\"  - {Parents.objects.count()} parents\")\n        print(f\"  - {Student.objects.count()} students\")\n        \n        return True\n        \n    except Exception as e:\n        print(f\"✗ Error creating sample data: {e}\")\n        import traceback\n        traceback.print_exc()\n        return False\n\ndef main():\n    \"\"\"Main setup function\"\"\"\n    print(\"=\"*60)\n    print(\"StudX Training Center Management System - Complete Setup\")\n    print(\"=\"*60)\n    \n    # Step 1: Create database\n    if not create_database():\n        return\n    \n    # Step 2: Run migrations\n    if not run_migrations():\n        return\n    \n    # Step 3: Create superuser\n    if not create_superuser():\n        return\n    \n    # Step 4: Create sample data\n    if not create_sample_data():\n        return\n    \n    print(\"\\n\" + \"=\"*60)\n    print(\"✓ SETUP COMPLETED SUCCESSFULLY!\")\n    print(\"=\"*60)\n    print(\"\\nYour StudX Training Center is ready to use:\")\n    print(\"\\n🌐 Access your application:\")\n    print(\"   http://localhost:8000/\")\n    print(\"\\n👤 Admin Panel:\")\n    print(\"   http://localhost:8000/admin/\")\n    print(\"   Username: admin\")\n    print(\"   Password: admin123\")\n    print(\"\\n📊 Features available:\")\n    print(\"   - Modern responsive dashboard\")\n    print(\"   - Student management with Moroccan sample data\")\n    print(\"   - Formation/course management\")\n    print(\"   - Planning and scheduling\")\n    print(\"   - Enhanced admin interface\")\n    print(\"\\n🚀 To start the server:\")\n    print(\"   python manage.py runserver\")\n    print(\"\\n\" + \"=\"*60)\n\nif __name__ == '__main__':\n    main()