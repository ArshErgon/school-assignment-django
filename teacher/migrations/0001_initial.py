# Generated by Django 2.1.7 on 2019-04-07 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddingAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_of_assignment', models.ImageField(blank=True, upload_to='assignment')),
                ('Class', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default=1, max_length=2)),
                ('adding_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default=True, max_length=254)),
                ('class_teacher_of', models.CharField(max_length=5)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='try')),
            ],
        ),
    ]
