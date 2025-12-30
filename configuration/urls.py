from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from configuration import views as config_views

app_name = 'configuration'

urlpatterns = [
	path('classes_list', config_views.classes_list, name='classes_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)