from django.urls import path
from .views import (
    shop_view,
    service_detail,
    service_edit,
    service_list,
    service_create,
    register,
    campaign_statistics,
)

urlpatterns = [
    path('services/', service_list, name='service_list'),
    path('services/new/', service_create, name='service_create'),
    path('services/<int:pk>/', service_detail, name='service_detail'),
    path('services/<int:pk>/edit/', service_edit, name='service_edit'),
    path('register/', register, name='register'),
    path('statistics/', campaign_statistics, name='campaign_statistics'),
    path('shop/', shop_view, name='shop_view'),  # Этот маршрут обрабатывает /clients/shop/
]
