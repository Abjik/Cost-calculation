# Generated by Django 3.2.23 on 2023-12-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='expenses',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
