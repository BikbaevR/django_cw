# Generated by Django 4.2.13 on 2024-07-08 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_is_publiched'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_publiched',
            new_name='is_published',
        ),
    ]
