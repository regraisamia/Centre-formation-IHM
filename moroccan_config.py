# Moroccan Training Center Configuration
# Configuration spécifique pour le Centre de Formation Marocain

# Project Information
PROJECT_NAME = "Centre de Formation Professionnelle"
PROJECT_SHORT_NAME = "CFP"
PROJECT_VERSION = "2.0.0"
PROJECT_DESCRIPTION = "Système de gestion pour centre de formation professionnelle au Maroc"

# Moroccan Localization
COUNTRY = "Maroc"
CURRENCY = "MAD"  # Moroccan Dirham
PHONE_PREFIX = "+212"
LANGUAGE_CODE = "fr-MA"  # French Morocco
TIME_ZONE = "Africa/Casablanca"

# Moroccan Regions and Cities
MOROCCAN_REGIONS = [
    ("casablanca-settat", "Casablanca-Settat"),
    ("rabat-sale-kenitra", "Rabat-Salé-Kénitra"),
    ("fes-meknes", "Fès-Meknès"),
    ("marrakech-safi", "Marrakech-Safi"),
    ("oriental", "Oriental"),
    ("tanger-tetouan-al-hoceima", "Tanger-Tétouan-Al Hoceïma"),
    ("souss-massa", "Souss-Massa"),
    ("draa-tafilalet", "Drâa-Tafilalet"),
    ("beni-mellal-khenifra", "Béni Mellal-Khénifra"),
    ("laayoune-sakia-el-hamra", "Laâyoune-Sakia El Hamra"),
    ("dakhla-oued-ed-dahab", "Dakhla-Oued Ed-Dahab"),
    ("guelmim-oued-noun", "Guelmim-Oued Noun")
]

MAJOR_CITIES = [
    ("casablanca", "Casablanca"),
    ("rabat", "Rabat"),
    ("fes", "Fès"),
    ("marrakech", "Marrakech"),
    ("agadir", "Agadir"),
    ("tanger", "Tanger"),
    ("meknes", "Meknès"),
    ("oujda", "Oujda"),
    ("kenitra", "Kénitra"),
    ("tetouan", "Tétouan"),
    ("safi", "Safi"),
    ("mohammedia", "Mohammedia"),
    ("khouribga", "Khouribga"),
    ("beni-mellal", "Béni Mellal"),
    ("el-jadida", "El Jadida"),
    ("nador", "Nador"),
    ("taza", "Taza"),
    ("settat", "Settat")
]

# Training Center Specific Settings
FORMATION_TYPES = [
    ("technique", "Formation Technique"),
    ("management", "Management et Gestion"),
    ("langues", "Langues et Communication"),
    ("informatique", "Informatique et Digital"),
    ("commerce", "Commerce et Marketing"),
    ("artisanat", "Artisanat et Métiers"),
    ("sante", "Santé et Social"),
    ("tourisme", "Tourisme et Hôtellerie")
]

FORMATION_LEVELS = [
    ("debutant", "Débutant"),
    ("intermediaire", "Intermédiaire"),
    ("avance", "Avancé"),
    ("expert", "Expert"),
    ("certification", "Certification Professionnelle")
]

FORMATION_DURATIONS = [
    ("1-month", "1 mois"),
    ("2-months", "2 mois"),
    ("3-months", "3 mois"),
    ("4-months", "4 mois"),
    ("6-months", "6 mois"),
    ("9-months", "9 mois"),
    ("12-months", "1 an"),
    ("18-months", "1 an et demi"),
    ("24-months", "2 ans")
]

# Student Status (Moroccan Context)
STUDENT_STATUS_CHOICES = [
    (1, "Inscrit"),
    (2, "En Formation"),
    (3, "En Stage"),
    (4, "Diplômé"),
    (5, "Abandon"),
    (6, "Suspendu"),
    (7, "Transféré"),
    (8, "En Attente")
]

# Moroccan Education Levels
EDUCATION_LEVELS = [
    ("primaire", "Primaire"),
    ("college", "Collège"),
    ("lycee", "Lycée"),
    ("bac", "Baccalauréat"),
    ("bac+1", "Bac+1"),
    ("bac+2", "Bac+2 (DUT/BTS)"),
    ("bac+3", "Bac+3 (Licence)"),
    ("bac+4", "Bac+4 (Maîtrise)"),
    ("bac+5", "Bac+5 (Master/Ingénieur)"),
    ("doctorat", "Doctorat")
]

# Moroccan Professional Sectors
PROFESSIONAL_SECTORS = [
    ("agriculture", "Agriculture et Pêche"),
    ("industrie", "Industrie"),
    ("batiment", "Bâtiment et Travaux Publics"),
    ("commerce", "Commerce et Distribution"),
    ("transport", "Transport et Logistique"),
    ("tourisme", "Tourisme et Hôtellerie"),
    ("finance", "Banque et Finance"),
    ("telecom", "Télécommunications"),
    ("sante", "Santé"),
    ("education", "Éducation et Formation"),
    ("administration", "Administration Publique"),
    ("artisanat", "Artisanat"),
    ("energie", "Énergie et Mines"),
    ("textile", "Textile et Cuir")
]

# Moroccan Holidays (for scheduling)
MOROCCAN_HOLIDAYS = [
    ("new-year", "Nouvel An", "01-01"),
    ("independence", "Fête de l'Indépendance", "01-11"),
    ("labor-day", "Fête du Travail", "05-01"),
    ("throne-day", "Fête du Trône", "07-30"),
    ("revolution-day", "Révolution du Roi et du Peuple", "08-20"),
    ("youth-day", "Fête de la Jeunesse", "08-21"),
    ("green-march", "Marche Verte", "11-06"),
    ("independence-day", "Fête de l'Indépendance", "11-18")
    # Note: Islamic holidays are lunar-based and change each year
]

# Training Center Branding
BRAND_COLORS = {
    "primary": "#2E8B57",      # Moroccan Green
    "secondary": "#DC143C",     # Moroccan Red
    "accent": "#FFD700",        # Gold
    "success": "#27AE60",
    "warning": "#F39C12",
    "danger": "#E74C3C",
    "info": "#3498DB",
    "dark": "#2C3E50",
    "light": "#ECF0F1"
}

# Contact Information Template
DEFAULT_CENTER_INFO = {
    "name": "Centre de Formation Professionnelle Al Manar",
    "address": "123 Boulevard Mohammed V",
    "city": "Casablanca",
    "postal_code": "20000",
    "phone": "+212 5 22 12 34 56",
    "mobile": "+212 6 12 34 56 78",
    "email": "contact@cfp-almanar.ma",
    "website": "www.cfp-almanar.ma",
    "director": "Dr. Abdelaziz Bennani",
    "founded_year": "2018",
    "license_number": "CF-2018-CAS-001",
    "accreditation": "Ministère de l'Éducation Nationale du Maroc"
}

# Default Formations (Training Programs)
DEFAULT_FORMATIONS = [
    {
        "name": "Développement Web Full Stack",
        "code": "DW-FS-001",
        "duration": "6 mois",
        "level": "Intermédiaire",
        "sector": "informatique",
        "price": 8500,
        "description": "Formation complète en développement web moderne"
    },
    {
        "name": "Marketing Digital",
        "code": "MD-001",
        "duration": "4 mois",
        "level": "Débutant",
        "sector": "commerce",
        "price": 6500,
        "description": "Stratégies marketing digitales et réseaux sociaux"
    },
    {
        "name": "Gestion de Projet",
        "code": "GP-001",
        "duration": "3 mois",
        "level": "Intermédiaire",
        "sector": "management",
        "price": 5500,
        "description": "Méthodologies Agile et outils de gestion"
    },
    {
        "name": "Comptabilité Générale",
        "code": "CG-001",
        "duration": "5 mois",
        "level": "Débutant",
        "sector": "finance",
        "price": 7000,
        "description": "Comptabilité selon les normes marocaines"
    },
    {
        "name": "Design Graphique",
        "code": "DG-001",
        "duration": "4 mois",
        "level": "Créatif",
        "sector": "artisanat",
        "price": 6000,
        "description": "Adobe Creative Suite et identité visuelle"
    }
]

# Email Templates
EMAIL_TEMPLATES = {
    "welcome_student": {
        "subject": "Bienvenue au Centre de Formation",
        "template": "emails/welcome_student_ma.html"
    },
    "certificate_ready": {
        "subject": "Votre certificat est prêt",
        "template": "emails/certificate_ready_ma.html"
    },
    "payment_reminder": {
        "subject": "Rappel de paiement",
        "template": "emails/payment_reminder_ma.html"
    }
}

# SMS Templates (for Moroccan mobile operators)
SMS_TEMPLATES = {
    "enrollment_confirmation": "Félicitations! Votre inscription au {formation_name} est confirmée. Début: {start_date}. CFP Al Manar",
    "payment_reminder": "Rappel: Paiement de {amount} MAD dû le {due_date} pour {formation_name}. CFP Al Manar",
    "certificate_ready": "Votre certificat {certificate_name} est prêt. Venez le récupérer au centre. CFP Al Manar"
}

# Reporting Configuration
REPORT_SETTINGS = {
    "default_currency": "MAD",
    "date_format": "%d/%m/%Y",
    "number_format": "fr_MA",
    "logo_path": "images/logo-cfp.png",
    "watermark": "Centre de Formation Professionnelle"
}

# Integration Settings
INTEGRATION_SETTINGS = {
    "payment_gateway": "CMI",  # Centre Monétique Interbancaire
    "sms_provider": "ORANGE_MA",  # Orange Morocco
    "email_provider": "SMTP",
    "backup_storage": "LOCAL"
}

# Security Settings
SECURITY_SETTINGS = {
    "password_min_length": 8,
    "session_timeout": 3600,  # 1 hour
    "max_login_attempts": 5,
    "require_2fa": False,
    "allowed_file_types": [".pdf", ".doc", ".docx", ".jpg", ".jpeg", ".png"],
    "max_file_size": 5242880  # 5MB
}