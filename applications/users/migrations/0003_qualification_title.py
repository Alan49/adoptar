# Generated by Django 3.0.10 on 2021-03-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210308_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='title',
            field=models.CharField(default='titulo', max_length=50, verbose_name='titulo'),
            preserve_default=False,
        ),
    ]
