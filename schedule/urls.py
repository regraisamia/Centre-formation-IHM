from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from schedule import views

app_name = 'schedule'

urlpatterns = [
	path('schedule/', views.schedule_list, name='schedule_main'),
	path('list/', views.schedule_list, name='list'),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)