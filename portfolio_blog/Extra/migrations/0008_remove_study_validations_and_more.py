# Generated by Django 4.1.6 on 2023-02-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0007_alter_study_certificate_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='validations',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='validations',
        ),
        migrations.AddField(
            model_name='validation',
            name='anonymous_identifier',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
