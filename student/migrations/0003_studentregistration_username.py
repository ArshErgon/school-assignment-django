# Generated by Django 2.1.7 on 2019-04-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_studentregistration_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='username',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]