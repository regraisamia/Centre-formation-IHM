"""StudX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import redirect
from django.views.generic import TemplateView

import dashboard.urls, student.urls, user.urls, communication.urls, configuration.urls, schedule.urls

# Simple views for new pages
def teachers_view(request):
    from django.shortcuts import render
    return render(request, 'teachers_list.html')

def formations_view(request):
    from django.shortcuts import render
    return render(request, 'formations_list.html')

def payments_view(request):
    from django.shortcuts import render
    return render(request, 'payments_list.html')

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    path('', lambda request: redirect('dashboard:dashboard'), name='root'),
    path('schedule/', include(schedule.urls, namespace='schedule')),
    path('configuration/', include(configuration.urls, namespace='configuration')),
    path('communication/', include(communication.urls, namespace='communication')),
    path('user/', include(user.urls, namespace='user')),
    path('dashboard/', include(dashboard.urls, namespace='dashboard')),
    path('student/', include(student.urls, namespace='student')),
    # New pages
    path('teachers/', teachers_view, name='teachers'),
    path('formations/', formations_view, name='formations'),
    path('payments/', payments_view, name='payments'),
]
