"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import jobs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('jobs/1', jobs.views.detail1, name='detail1'),
    path('jobs/2', jobs.views.detail2, name='detail2'),
    path('jobs/3', jobs.views.detail3, name='detail3'),
    path('jobs/4', jobs.views.detail4, name='detail4'),
    path('jobs/5', jobs.views.detail5, name='detail5'),
    path('jobs/6', jobs.views.detail6, name='detail6'),
    path('jobs/7', jobs.views.detail7, name='detail7'),
    path('jobs/8', jobs.views.detail8, name='detail8'),
    path('jobs/9', jobs.views.detail9, name='detail9'),
    path('jobs/10', jobs.views.detail10, name='detail10'),
    path('jobs/11', jobs.views.detail11, name='detail11'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


