# Generated by Django 5.2 on 2025-05-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtechapp', '0002_eventregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tableexample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=50)),
                ('event_name', models.CharField(max_length=100)),
                ('event_category', models.CharField(max_length=100)),
                ('event_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
