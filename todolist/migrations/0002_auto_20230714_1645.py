# Generated by Django 3.2.6 on 2023-07-14 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='duedate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('primary', 'nomal'), ('secondary', 'low')], default='low', max_length=50),
        ),
    ]