# Generated by Django 4.1.7 on 2024-01-09 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yemekler', '0009_pkategori_program_pkategori'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pkategori',
            options={'verbose_name': 'Program Kategoriler', 'verbose_name_plural': 'Program Kategoriler'},
        ),
        migrations.DeleteModel(
            name='Yorum',
        ),
    ]