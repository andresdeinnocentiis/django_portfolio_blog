# Generated by Django 4.1.6 on 2023-02-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_anonymoususer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_images'),
        ),
    ]
