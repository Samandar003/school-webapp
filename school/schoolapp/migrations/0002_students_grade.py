# Generated by Django 4.0 on 2021-12-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='grade',
            field=models.IntegerField(default=1),
        ),
    ]