# Generated by Django 2.2.5 on 2022-08-06 09:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lists', '0002_list_rooms'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete='cascade', related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
