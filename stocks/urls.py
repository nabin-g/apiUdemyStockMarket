from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('stocksapp.urls')),
    path('admin/', admin.site.urls),

]
