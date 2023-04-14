"""
URL configuration for monthly_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from eda.views import index_view, page1_view, page2_view, page3_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view),
    path("index/", index_view),
    path("type/", page1_view),
    path("vendor/", page2_view),
    path("foundry/", page3_view),
]
