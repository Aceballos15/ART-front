# Generated by Django 4.1.5 on 2023-02-01 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Artisan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.artisan'),
            preserve_default=False,
        ),
    ]
