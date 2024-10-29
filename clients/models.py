from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class PotentialClient(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

class ActiveClient(models.Model):
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE)

class Contract(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document = models.FileField(upload_to='contracts/')
    date_signed = models.DateField()
    duration = models.IntegerField()  # in months
    amount = models.DecimalField(max_digits=10, decimal_places=2)
