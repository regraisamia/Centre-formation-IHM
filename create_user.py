import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudX.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@cfp.ma',
        password='admin123'
    )
    print("Superuser created:")
    print("Username: admin")
    print("Password: admin123")
else:
    print("Superuser already exists:")
    print("Username: admin")
    print("Password: admin123")