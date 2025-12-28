from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from student.models import Student, Parents, Address
from configuration.models import Classes, Subjects
from user.models import User
import json
import random
from datetime import datetime, date

class Command(BaseCommand):
    help = 'Load Moroccan sample data for the training center'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='moroccan_sample_data.json',
            help='JSON file containing sample data'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🇲🇦 Chargement des données marocaines...'))
        
        try:
            # Load JSON data
            with open(options['file'], 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Create formations (classes)
            self.create_formations(data['formations'])
            
            # Create addresses
            addresses = self.create_addresses(data['cities'])
            
            # Create students
            self.create_students(data['students'], addresses)
            
            # Create trainers (users)
            self.create_trainers(data['trainers'])
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Données chargées avec succès!\n'
                    f'📊 {len(data["students"])} stagiaires créés\n'
                    f'👨🏫 {len(data["trainers"])} formateurs créés\n'
                    f'🎓 {len(data["formations"])} formations créées'
                )
            )
            
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR(
                    f'❌ Fichier {options["file"]} non trouvé. '
                    'Exécutez d\'abord generate_moroccan_data.py'
                )
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Erreur lors du chargement: {str(e)}')
            )

    def create_formations(self, formations_data):
        """Create formation classes"""
        self.stdout.write('📚 Création des formations...')
        
        for formation in formations_data:
            classe, created = Classes.objects.get_or_create(
                classe_name=formation['name'],
                defaults={
                    'description': formation['description'],
                    'level': formation['level'],
                    'duration': formation['duration']
                }
            )
            if created:
                self.stdout.write(f'  ✓ Formation créée: {formation["name"]}')

    def create_addresses(self, cities):
        """Create sample addresses"""
        self.stdout.write('🏠 Création des adresses...')
        
        addresses = []
        streets = [
            'Avenue Mohammed V', 'Boulevard Hassan II', 'Rue Al Massira',
            'Avenue des FAR', 'Rue Zerktouni', 'Boulevard Anfa',
            'Avenue Maarif', 'Rue Ibn Sina', 'Boulevard Ghandi',
            'Avenue Al Qods', 'Rue Patrice Lumumba', 'Avenue Lalla Yacout'
        ]
        
        for city in cities[:20]:  # Create addresses for first 20 cities
            for i in range(3):  # 3 addresses per city
                street = f"{random.randint(1, 999)} {random.choice(streets)}"
                address, created = Address.objects.get_or_create(
                    street=street,
                    city=city,
                    defaults={'zip': random.randint(10000, 99999)}
                )
                addresses.append(address)
                
        self.stdout.write(f'  ✓ {len(addresses)} adresses créées')
        return addresses

    def create_students(self, students_data, addresses):
        """Create student records"""
        self.stdout.write('👨‍🎓 Création des stagiaires...')
        
        formations = list(Classes.objects.all())
        
        for student_data in students_data:
            try:
                # Parse birth date
                birth_date = datetime.strptime(student_data['birth_date'], '%Y-%m-%d').date()
                
                # Get or create student
                student, created = Student.objects.get_or_create(
                    matricule=student_data['matricule'],
                    defaults={
                        'fname': student_data['first_name'],
                        'lname': student_data['last_name'],
                        'bday': birth_date,
                        'gender': 1 if student_data['gender'] == 'M' else 2,  # Assuming 1=Male, 2=Female
                        'classe': random.choice(formations) if formations else None,
                        'address': random.choice(addresses) if addresses else None,
                        'status': 1,  # Active
                        'comment': f'CIN: {student_data.get("cin", "N/A")}, Téléphone: {student_data.get("phone", "N/A")}'
                    }
                )
                
                if created:
                    self.stdout.write(f'  ✓ Stagiaire créé: {student_data["first_name"]} {student_data["last_name"]}')
                    
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(
                        f'  ⚠️ Erreur création stagiaire {student_data["first_name"]}: {str(e)}'
                    )
                )

    def create_trainers(self, trainers_data):
        """Create trainer user accounts"""
        self.stdout.write('👨‍🏫 Création des formateurs...')
        
        User = get_user_model()
        
        for trainer_data in trainers_data:
            try:
                username = f"{trainer_data['first_name'].lower()}.{trainer_data['last_name'].lower()}".replace(' ', '')
                email = trainer_data.get('email', f'{username}@cfp-almanar.ma')
                
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        'first_name': trainer_data['first_name'],
                        'last_name': trainer_data['last_name'],
                        'email': email,
                        'is_staff': True,
                        'is_active': True,
                        'role': 2  # Assuming 2 = Teacher role
                    }
                )
                
                if created:
                    user.set_password('password123')  # Default password
                    user.save()
                    self.stdout.write(f'  ✓ Formateur créé: {trainer_data["first_name"]} {trainer_data["last_name"]}')
                    
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(
                        f'  ⚠️ Erreur création formateur {trainer_data["first_name"]}: {str(e)}'
                    )
                )