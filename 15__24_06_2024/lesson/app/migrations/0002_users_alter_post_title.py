# Generated by Django 4.2.13 on 2024-06-24 16:30

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[app.models.validate_name])),
                ('age', models.IntegerField(validators=[app.models.validate_age])),
                ('b_date', models.DateField(validators=[app.models.validate_b_date])),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[app.models.validate_title]),
        ),
    ]