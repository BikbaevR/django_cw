# Generated by Django 4.2.13 on 2024-06-05 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='books/%d/%m/%y'),
        ),
    ]
