# Generated by Django 4.1.6 on 2023-02-27 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0014_post_developed_for_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='num_reviews',
        ),
    ]