# Generated by Django 2.2.5 on 2021-04-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210413_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('english', 'English'), ('korean', 'KOREAN')], max_length=6, null=True),
        ),
    ]
