# Generated by Django 2.2.5 on 2021-04-14 09:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0002_auto_20210414_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='conversation', to=settings.AUTH_USER_MODEL),
        ),
    ]
