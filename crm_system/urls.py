from django.contrib import admin
from django.urls import path, include
from clients.views import home_view  # Измените на правильный путь


urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('', home_view, name='home'),  # Добавьте перенаправление здесь
]
