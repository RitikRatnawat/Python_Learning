# Generated by Django 4.1.7 on 2024-06-05 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_alter_student_student_id_alter_subjectmark_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmark',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='card.student'),
        ),
    ]