# Generated by Django 3.0.10 on 2021-03-10 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostulationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'estado de postulación',
                'verbose_name_plural': 'estado de postulaciones',
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_posts', to=settings.AUTH_USER_MODEL, verbose_name='creada por'),
        ),
        migrations.CreateModel(
            name='Postulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creada')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_postulations', to=settings.AUTH_USER_MODEL, verbose_name='candidato')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='publicacion')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='posts.PostulationStatus', verbose_name='estado')),
            ],
            options={
                'verbose_name': 'postulaciones',
                'verbose_name_plural': 'postulaciones',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='postulations',
            field=models.ManyToManyField(through='posts.Postulation', to=settings.AUTH_USER_MODEL, verbose_name='postulaciones'),
        ),
    ]