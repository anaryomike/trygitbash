# Generated by Django 2.1.7 on 2019-03-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20190317_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='pending', max_length=8),
        ),
    ]
