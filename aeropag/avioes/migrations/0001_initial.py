# Generated by Django 5.1.3 on 2024-11-09 18:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviao',
            fields=[
                ('avi_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('avi_prefixo_do_aviao', models.CharField(max_length=50)),
                ('avi_toneladas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avi_grupo', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
