# Generated by Django 5.1.2 on 2024-11-15 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avioes', '0001_initial'),
        ('clientes', '0003_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cli_avi_codigo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='avi_codigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clientes', to='avioes.aviao'),
        ),
    ]
