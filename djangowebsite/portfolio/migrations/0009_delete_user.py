# Generated by Django 4.1.7 on 2023-03-26 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
