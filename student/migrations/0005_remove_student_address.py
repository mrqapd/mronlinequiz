# Generated by Django 5.0.1 on 2024-06-04 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        ),
    ]