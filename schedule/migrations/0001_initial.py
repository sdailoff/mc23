# Generated by Django 4.2.2 on 2023-07-16 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('usuario1', models.ForeignKey(blank=True, default=99, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules_usuario1', to='usuarios.usuario')),
                ('usuario2', models.ForeignKey(blank=True, default=99, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules_usuario2', to='usuarios.usuario')),
                ('usuario3', models.ForeignKey(blank=True, default=99, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules_usuario3', to='usuarios.usuario')),
                ('usuario4', models.ForeignKey(blank=True, default=99, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules_usuario4', to='usuarios.usuario')),
            ],
        ),
    ]
