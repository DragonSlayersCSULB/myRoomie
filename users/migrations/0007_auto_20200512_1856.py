# Generated by Django 3.0.2 on 2020-05-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200512_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('Home', 'h'), ('School', 's'), ('Gym', 'g')], default='Home', max_length=9),
        ),
    ]
