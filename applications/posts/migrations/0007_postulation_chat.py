# Generated by Django 3.0.10 on 2021-03-12 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_remove_chat_postulation'),
        ('posts', '0006_remove_postulation_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulation',
            name='chat',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chats.Chat', verbose_name='chat'),
        ),
    ]
