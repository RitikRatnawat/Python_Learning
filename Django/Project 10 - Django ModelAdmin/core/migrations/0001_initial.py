# Generated by Django 4.1.7 on 2024-08-29 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('student_email', models.EmailField(max_length=20)),
                ('student_password', models.CharField(max_length=70)),
            ],
        ),
    ]
