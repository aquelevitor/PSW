# Generated by Django 4.2 on 2023-04-15 00:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('carga_horaria', models.IntegerField()),
                ('logo', models.FileField(upload_to='logos')),
                ('cor_principal', models.CharField(max_length=7)),
                ('cor_secundaria', models.CharField(max_length=7)),
                ('cor_fundo', models.CharField(max_length=7)),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
