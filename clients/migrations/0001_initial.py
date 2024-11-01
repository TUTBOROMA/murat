# Generated by Django 5.1.2 on 2024-10-29 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('promotion_channel', models.CharField(max_length=255)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='contracts/')),
                ('date_signed', models.DateField()),
                ('duration', models.IntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PotentialClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.campaign')),
            ],
        ),
        migrations.CreateModel(
            name='ActiveClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.contract')),
                ('potential_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.potentialclient')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.service'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.service'),
        ),
    ]
