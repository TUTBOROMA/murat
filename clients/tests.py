# clients/tests.py
from django.test import TestCase
from .models import Service

class ServiceModelTest(TestCase):
    def setUp(self):
        Service.objects.create(name="Тестовая услуга", description="Описание", price=100.00)

    def test_service_creation(self):
        service = Service.objects.get(name="Тестовая услуга")
        self.assertEqual(service.description, "Описание")
        self.assertEqual(service.price, 100.00)
