# Generated by Django 3.2.18 on 2023-09-26 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_animal_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='USER',
        ),
    ]
