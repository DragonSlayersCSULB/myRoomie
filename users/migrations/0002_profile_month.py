# Generated by Django 3.0.2 on 2020-05-13 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='month',
            field=models.CharField(choices=[('h', 'Home'), ('s', 'School'), ('g', 'Gym')], default='1', max_length=9),
        ),
    ]
