"""
URL configuration for altamir project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from altamirrr import views
from altamirrr.views import delete_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index,name='Index'),
    path('Gallery/', views.Gallery,name='Gallery'),
    path('Anual/', views.Anual,name='Anual'),
    path('Maintance/', views.Maintance,name='Maintance'),
    path('Acinstall/', views.Acinstall,name='Acinstall'),
    path('Piduct/', views.Piduct,name='Piduct'),
    path('feedback/delete/<int:feedback_id>/', delete_feedback, name='delete_feedback'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
