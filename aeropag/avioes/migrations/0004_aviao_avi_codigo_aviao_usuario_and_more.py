# Generated by Django 5.1.2 on 2024-11-28 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avioes', '0003_cobranca'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='aviao',
            name='avi_codigo',
            field=models.CharField(default='DEFAULT_VALUE', max_length=20),
        ),
        migrations.AddField(
            model_name='aviao',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avioes_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aviao',
            name='avi_toneladas',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Cobranca',
        ),
    ]