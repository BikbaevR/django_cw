# Generated by Django 4.2.15 on 2024-08-28 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
    ]