"""foodoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from foodapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('signup/', signup),
    path('signin/', signin),
    path('signout/',signout),
    path('foodcourts/', foodcourt),
    path('stores/<str:fc_id>/', stores),
    path('stores/<str:fc_id>/<str:number>/menu/', store_menu),
    path('order_summary/', order_summary),
    path('invoice/', invoice),
    path('add_to_cart/', add_to_cart),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
