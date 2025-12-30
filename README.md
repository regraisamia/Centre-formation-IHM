# Centre de Formation Al Manar - Système de Gestion

[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

## 📋 Description

**Centre de Formation Al Manar** est un système de gestion moderne pour centres de formation professionnelle, développé avec Django et optimisé pour l'environnement marocain.

### ✨ Fonctionnalités Principales

- 🎓 **Gestion des Étudiants** : Inscription, suivi, profils détaillés
- 📚 **Gestion des Formations** : Programmes, matières, planning
- 👨🏫 **Gestion des Formateurs** : Profils, spécialités, planning
- 📊 **Tableau de Bord** : Statistiques en temps réel, graphiques
- 📝 **Notes et Évaluations** : Système de notation complet
- 📅 **Planning** : Gestion des sessions et emplois du temps
- 🏆 **Certificats** : Génération et suivi des certifications
- 💰 **Finances** : Suivi des paiements et facturation
- 📱 **Interface Responsive** : Compatible tous écrans

## 🚀 Installation Rapide (XAMPP)

### Prérequis
- XAMPP installé et démarré (Apache + MySQL)
- Python 3.7+ installé
- Git (optionnel)

### Étapes d'Installation

1. **Cloner ou télécharger le projet**
   ```bash
   git clone <repository-url>
   cd StudX
   ```

2. **Créer la base de données MySQL**
   - Ouvrir phpMyAdmin (http://localhost/phpmyadmin)
   - Créer une nouvelle base de données nommée `studx_database`
   - Utiliser l'encodage `utf8mb4_general_ci`

3. **Exécuter le script d'installation**
   ```bash
   setup.bat
   ```
   
   Ou manuellement :
   ```bash
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic --noinput
   python populate_data.py
   ```

4. **Démarrer le serveur**
   ```bash
   python manage.py runserver
   ```

5. **Accéder à l'application**
   - Interface principale : http://localhost:8000
   - Administration : http://localhost:8000/admin
   - **Login Admin** : `admin` / `admin123`

## 🎯 Utilisation

### Interface Principale
- **Tableau de Bord** : Vue d'ensemble avec statistiques
- **Étudiants** : Gestion complète des étudiants
- **Formations** : Programmes et matières
- **Planning** : Sessions et emplois du temps
- **Rapports** : Analyses et statistiques

### Interface d'Administration
- Accès complet à toutes les données
- Gestion des utilisateurs et permissions
- Configuration du système
- Import/Export de données

## 🛠️ Technologies Utilisées

- **Backend** : Django 2.2, Python 3
- **Base de Données** : MySQL
- **Frontend** : Bootstrap 5, HTML5, CSS3, JavaScript
- **Graphiques** : Chart.js
- **Animations** : AOS (Animate On Scroll)
- **Icons** : Font Awesome 6

## 📊 Données de Démonstration

Le système inclut des données de démonstration réalistes :
- 30 étudiants avec noms marocains
- 8 formations professionnelles
- 10 matières d'enseignement
- 5 salles de formation
- Notes et présences d'exemple

## 🔧 Configuration

### Base de Données
Le fichier `settings.py` est configuré pour MySQL :
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studx_database',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Personnalisation
- **Couleurs** : Modifiez les variables CSS dans `static/css/modern-dashboard.css`
- **Logo** : Remplacez dans les templates
- **Données** : Modifiez `populate_data.py` pour vos données

## 📁 Structure du Projet

```
StudX/
├── dashboard/          # Tableau de bord
├── student/           # Gestion étudiants
├── configuration/     # Formations et matières
├── schedule/         # Planning
├── user/            # Authentification
├── templates/       # Templates HTML
├── static/         # CSS, JS, images
├── media/          # Fichiers uploadés
└── StudX/          # Configuration Django
```

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

## 📝 Licence

Ce projet est open source. Consultez les licences des frameworks utilisés.

## 🆘 Support

Pour toute question ou problème :
- Créer une issue sur GitHub
- Consulter la documentation Django
- Vérifier la configuration XAMPP

## 🔄 Mises à Jour

### Version 2.0 (Actuelle)
- ✅ Interface moderne et responsive
- ✅ Thème marocain
- ✅ Données réalistes
- ✅ Administration améliorée
- ✅ Graphiques interactifs
- ✅ Optimisation mobile

### Prochaines Fonctionnalités
- 📧 Notifications par email
- 📱 Application mobile
- 🔐 Authentification avancée
- 📊 Rapports PDF
- 🌐 Multi-langues

---

**Développé avec ❤️ pour les centres de formation marocains**