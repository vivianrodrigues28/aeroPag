# Generated by Django 5.1.2 on 2024-11-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avi_prefixo_do_aviao', models.CharField(max_length=50)),
                ('avi_grupo', models.CharField(choices=[('1', 'Grupo 1'), ('2', 'Grupo 2')], max_length=1)),
                ('avi_toneladas', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
