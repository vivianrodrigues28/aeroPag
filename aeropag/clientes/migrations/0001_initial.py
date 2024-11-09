# Generated by Django 5.1.3 on 2024-11-09 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avioes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cli_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('cli_nome', models.CharField(max_length=255)),
                ('cli_email', models.EmailField(max_length=255)),
                ('cli_telefone', models.CharField(max_length=50)),
                ('cli_avi_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='avioes.aviao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
