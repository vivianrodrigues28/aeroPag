# Generated by Django 5.1.3 on 2024-12-12 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cobrancas', '0002_cobranca_campo_temporario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cobranca',
            name='campo_temporario',
        ),
    ]
