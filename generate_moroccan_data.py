#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moroccan Sample Data Generator for Centre de Formation
This script generates realistic Moroccan data for the training center
"""

import random
from datetime import datetime, timedelta
import json

# Moroccan Names Data
MOROCCAN_FIRST_NAMES_MALE = [
    "Mohammed", "Ahmed", "Youssef", "Omar", "Hassan", "Khalid", "Abdelaziz", "Rachid",
    "Said", "Mustapha", "Abderrahim", "Abdelkader", "Noureddine", "Abdellatif", "Driss",
    "Karim", "Hamid", "Brahim", "Abdellah", "Jamal", "Larbi", "Abdessamad", "Amine",
    "Mehdi", "Tarik", "Hicham", "Othmane", "Zakaria", "Ismail", "Ayoub", "Bilal"
]

MOROCCAN_FIRST_NAMES_FEMALE = [
    "Fatima", "Aicha", "Khadija", "Zahra", "Hafsa", "Maryam", "Amina", "Salma",
    "Nadia", "Laila", "Souad", "Rajae", "Zineb", "Siham", "Karima", "Samira",
    "Latifa", "Houria", "Malika", "Naima", "Ghizlane", "Imane", "Sanaa", "Widad",
    "Btissam", "Kenza", "Loubna", "Hasna", "Chaimae", "Oumaima", "Yasmine", "Rim"
]

MOROCCAN_LAST_NAMES = [
    "Alami", "Bennani", "Tazi", "Fassi", "Idrissi", "Kettani", "Berrada", "Lahlou",
    "Benali", "Chraibi", "Benjelloun", "Sefrioui", "Benkirane", "Lamrani", "Filali",
    "Benabdellah", "Benomar", "Benslimane", "Bensaid", "Bentaleb", "Benyahia", "Bensouda",
    "El Alaoui", "El Fassi", "El Idrissi", "El Kettani", "El Berrada", "El Lahlou",
    "Ouali", "Ouazzani", "Oulad", "Qadiri", "Rifai", "Sabri", "Tahiri", "Wazzani",
    "Ziani", "Zouiten", "Amrani", "Andaloussi", "Bouchaib", "Cherkaoui", "Douiri",
    "Ghali", "Hajji", "Jaidi", "Kabbaj", "Lazrak", "Maaninou", "Naciri", "Rachidi"
]

MOROCCAN_CITIES = [
    "Casablanca", "Rabat", "Fès", "Marrakech", "Agadir", "Tanger", "Meknès", "Oujda",
    "Kenitra", "Tétouan", "Safi", "Mohammedia", "Khouribga", "Beni Mellal", "El Jadida",
    "Nador", "Taza", "Settat", "Berrechid", "Khemisset", "Inezgane", "Ksar El Kebir",
    "Larache", "Guelmim", "Berkane", "Taourirt", "Bouskoura", "Fquih Ben Salah",
    "Dcheira El Jihadia", "Oued Zem", "Sidi Slimane", "Youssoufia", "Sidi Kacem",
    "Azrou", "Midelt", "Ifrane", "Errachidia", "Ouarzazate", "Zagora", "Tiznit"
]

MOROCCAN_REGIONS = [
    "Casablanca-Settat", "Rabat-Salé-Kénitra", "Fès-Meknès", "Marrakech-Safi",
    "Oriental", "Tanger-Tétouan-Al Hoceïma", "Souss-Massa", "Drâa-Tafilalet",
    "Béni Mellal-Khénifra", "L'Oriental", "Laâyoune-Sakia El Hamra", "Dakhla-Oued Ed-Dahab"
]

FORMATIONS_DATA = [
    {
        "name": "Développement Web Full Stack",
        "duration": "6 mois",
        "level": "Débutant à Avancé",
        "description": "Formation complète en développement web avec HTML, CSS, JavaScript, PHP, MySQL",
        "price": 8500
    },
    {
        "name": "Marketing Digital",
        "duration": "4 mois",
        "level": "Intermédiaire",
        "description": "SEO, SEM, réseaux sociaux, email marketing, analytics",
        "price": 6500
    },
    {
        "name": "Gestion de Projet",
        "duration": "3 mois",
        "level": "Tous niveaux",
        "description": "Méthodologies Agile, Scrum, outils de gestion de projet",
        "price": 5500
    },
    {
        "name": "Comptabilité et Finance",
        "duration": "5 mois",
        "level": "Débutant",
        "description": "Comptabilité générale, fiscalité marocaine, logiciels comptables",
        "price": 7000
    },
    {
        "name": "Design Graphique",
        "duration": "4 mois",
        "level": "Créatif",
        "description": "Photoshop, Illustrator, InDesign, identité visuelle",
        "price": 6000
    },
    {
        "name": "Ressources Humaines",
        "duration": "3 mois",
        "level": "Professionnel",
        "description": "Recrutement, gestion des talents, droit du travail marocain",
        "price": 5800
    },
    {
        "name": "Intelligence Artificielle",
        "duration": "8 mois",
        "level": "Avancé",
        "description": "Machine Learning, Deep Learning, Python, TensorFlow",
        "price": 12000
    },
    {
        "name": "Cybersécurité",
        "duration": "6 mois",
        "level": "Technique",
        "description": "Sécurité réseau, ethical hacking, audit sécurité",
        "price": 9500
    },
    {
        "name": "E-commerce",
        "duration": "3 mois",
        "level": "Business",
        "description": "Création boutique en ligne, logistique, paiement en ligne",
        "price": 4500
    },
    {
        "name": "Langues Étrangères",
        "duration": "6 mois",
        "level": "Tous niveaux",
        "description": "Anglais, Français, Espagnol - Business et conversation",
        "price": 3500
    }
]

TRAINER_SPECIALIZATIONS = [
    "Développement Web", "Marketing Digital", "Gestion de Projet", "Design",
    "Comptabilité", "Ressources Humaines", "Intelligence Artificielle",
    "Cybersécurité", "E-commerce", "Langues", "Communication", "Leadership"
]

def generate_moroccan_phone():
    """Generate a realistic Moroccan phone number"""
    prefixes = ["06", "07", "05"]  # Moroccan mobile prefixes
    prefix = random.choice(prefixes)
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f"+212 {prefix[1:]} {number[:2]} {number[2:4]} {number[4:6]} {number[6:8]}"

def generate_cin():
    """Generate a realistic Moroccan CIN (Carte d'Identité Nationale)"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return f"{random.choice(letters)}{random.randint(100000, 999999)}"

def generate_email(first_name, last_name):
    """Generate a realistic email address"""
    domains = ["gmail.com", "yahoo.fr", "hotmail.com", "outlook.com", "live.com"]
    separators = [".", "_", ""]
    
    first = first_name.lower().replace(" ", "")
    last = last_name.lower().replace(" ", "")
    separator = random.choice(separators)
    domain = random.choice(domains)
    
    # Sometimes add numbers
    if random.choice([True, False]):
        number = random.randint(1, 99)
        return f"{first}{separator}{last}{number}@{domain}"
    else:
        return f"{first}{separator}{last}@{domain}"

def generate_students(count=50):
    """Generate realistic Moroccan student data"""
    students = []
    
    for i in range(count):
        gender = random.choice(["M", "F"])
        if gender == "M":
            first_name = random.choice(MOROCCAN_FIRST_NAMES_MALE)
        else:
            first_name = random.choice(MOROCCAN_FIRST_NAMES_FEMALE)
        
        last_name = random.choice(MOROCCAN_LAST_NAMES)
        
        # Generate birth date (18-35 years old)
        birth_year = random.randint(1988, 2005)
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)
        birth_date = f"{birth_year}-{birth_month:02d}-{birth_day:02d}"
        
        student = {
            "matricule": f"ST{2024}{i+1:04d}",
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "birth_date": birth_date,
            "cin": generate_cin(),
            "phone": generate_moroccan_phone(),
            "email": generate_email(first_name, last_name),
            "city": random.choice(MOROCCAN_CITIES),
            "region": random.choice(MOROCCAN_REGIONS),
            "address": f"{random.randint(1, 999)} Rue {random.choice(['Hassan II', 'Mohammed V', 'Al Massira', 'Zerktouni', 'Anfa', 'Maarif'])}",
            "formation": random.choice(FORMATIONS_DATA)["name"],
            "enrollment_date": f"2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "status": random.choice(["Actif", "En Formation", "Diplômé", "Suspendu"])
        }
        
        students.append(student)
    
    return students

def generate_trainers(count=15):
    """Generate realistic Moroccan trainer data"""
    trainers = []
    
    for i in range(count):
        gender = random.choice(["M", "F"])
        if gender == "M":
            first_name = random.choice(MOROCCAN_FIRST_NAMES_MALE)
        else:
            first_name = random.choice(MOROCCAN_FIRST_NAMES_FEMALE)
        
        last_name = random.choice(MOROCCAN_LAST_NAMES)
        
        trainer = {
            "employee_id": f"TR{2024}{i+1:03d}",
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "phone": generate_moroccan_phone(),
            "email": generate_email(first_name, last_name),
            "city": random.choice(MOROCCAN_CITIES),
            "specialization": random.choice(TRAINER_SPECIALIZATIONS),
            "experience_years": random.randint(2, 15),
            "education": random.choice([
                "Master en Informatique",
                "Ingénieur Commercial",
                "Master en Marketing",
                "Doctorat en Sciences",
                "MBA",
                "Master en Design",
                "Ingénieur Système"
            ]),
            "hire_date": f"20{random.randint(20, 24)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
            "salary": random.randint(8000, 25000)  # MAD
        }
        
        trainers.append(trainer)
    
    return trainers

def save_sample_data():
    """Generate and save all sample data to JSON files"""
    
    # Generate data
    students_data = generate_students(100)
    trainers_data = generate_trainers(20)
    
    # Prepare complete dataset
    sample_data = {
        "center_info": {
            "name": "Centre de Formation Professionnelle Al Manar",
            "address": "123 Boulevard Mohammed V, Casablanca 20000",
            "phone": "+212 5 22 12 34 56",
            "email": "contact@cfp-almanar.ma",
            "website": "www.cfp-almanar.ma",
            "director": "Dr. Abdelaziz Bennani",
            "founded": "2018",
            "license": "CF-2018-CAS-001"
        },
        "formations": FORMATIONS_DATA,
        "students": students_data,
        "trainers": trainers_data,
        "cities": MOROCCAN_CITIES,
        "regions": MOROCCAN_REGIONS,
        "statistics": {
            "total_students": len(students_data),
            "total_trainers": len(trainers_data),
            "total_formations": len(FORMATIONS_DATA),
            "success_rate": "87%",
            "employment_rate": "92%"
        }
    }
    
    # Save to JSON file
    with open('moroccan_sample_data.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)
    
    print("✅ Données marocaines générées avec succès!")
    print(f"📊 {len(students_data)} stagiaires générés")
    print(f"👨‍🏫 {len(trainers_data)} formateurs générés")
    print(f"🎓 {len(FORMATIONS_DATA)} formations disponibles")
    print("📁 Fichier sauvegardé: moroccan_sample_data.json")

if __name__ == "__main__":
    save_sample_data()