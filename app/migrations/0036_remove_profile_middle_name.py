# Generated by Django 5.1.1 on 2024-11-25 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='middle_name',
        ),
    ]