# Generated by Django 4.2.13 on 2024-07-15 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='title',
            new_name='name',
        ),
    ]
