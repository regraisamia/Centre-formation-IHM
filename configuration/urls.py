from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from configuration import views as config_views

app_name = 'configuration'

urlpatterns = [
	path('classes/', config_views.classes_list, name='classes_list'),
	path('formations/', config_views.formations_list, name='formations_list'),
	path('add-formation/', config_views.add_formation, name='add_formation'),
	path('add-classe/', config_views.add_classe, name='add_classe'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)