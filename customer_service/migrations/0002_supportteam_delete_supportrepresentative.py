# Generated by Django 5.1.5 on 2025-01-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='SupportRepresentative',
        ),
    ]
