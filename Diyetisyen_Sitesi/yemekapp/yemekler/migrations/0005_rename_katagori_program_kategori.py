# Generated by Django 4.1.7 on 2024-01-05 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yemekler', '0004_program_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='Katagori',
            new_name='Kategori',
        ),
    ]