# Generated by Django 5.1.1 on 2024-11-25 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_remove_profile_middle_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History',
        ),
    ]