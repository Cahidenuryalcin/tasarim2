# Generated by Django 4.1.7 on 2023-06-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
