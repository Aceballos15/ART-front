# Generated by Django 4.1.5 on 2023-02-03 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='adress',
            new_name='Adress',
        ),
    ]
