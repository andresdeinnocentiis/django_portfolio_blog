# Generated by Django 4.1.6 on 2023-02-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Extra', '0002_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
