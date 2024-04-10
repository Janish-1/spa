
from django.contrib import admin
from django.urls import path,include
from home.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('', spa_search, name='spa_search'),
    path('spa_details/<int:spa_id>/',spa_details, name='spa_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
