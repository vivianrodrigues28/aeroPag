# Generated by Django 5.1.2 on 2024-10-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviao',
            fields=[
                ('avi_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('avi_prefixo_do_aviao', models.CharField(max_length=50)),
                ('avi_toneladas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('avi_grupo', models.IntegerField()),
            ],
        ),
    ]