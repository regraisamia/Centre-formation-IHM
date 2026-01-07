# Installation et Lancement du Projet

## Prérequis
- Python 3.7+
- MySQL (XAMPP recommandé)
- Git

## Installation

### 1. Cloner le projet
```bash
git clone https://github.com/regraisamia/Centre-formation-IHM.git
cd Centre-formation-IHM
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration de la base de données
- Démarrer XAMPP (Apache + MySQL)
- Ouvrir phpMyAdmin : http://localhost/phpmyadmin
- Créer une base de données : `studx_database`
- Encodage : `utf8mb4_general_ci`

### 5. Migrations et données
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python populate_data.py
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

## Accès à l'application
- **Interface principale** : http://localhost:8000
- **Login par défaut** : `admin` / `admin123`

## Fonctionnalités
- ✅ Gestion des étudiants (CRUD)
- ✅ Recherche et filtrage
- ✅ Changement statut paiement
- ✅ Interface moderne et responsive
- ✅ Pas d'admin Django (interface personnalisée)

## Dépannage
Si erreur de base de données, vérifier :
- XAMPP MySQL démarré
- Base `studx_database` créée
- Configuration dans `settings.py`