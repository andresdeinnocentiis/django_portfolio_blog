# Generated by Django 4.1.6 on 2023-02-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0004_rename_technoloy_validation_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/study_images'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/tech_images'),
        ),
    ]
