# Generated by Django 3.0.2 on 2020-05-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200512_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('Home', 'Home'), ('School', 'School'), ('Gym', 'Gym')], default='1', max_length=9),
        ),
    ]