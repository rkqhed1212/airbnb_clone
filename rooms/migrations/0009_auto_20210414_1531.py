# Generated by Django 2.2.5 on 2021-04-14 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0008_auto_20210414_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bath',
            new_name='baths',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='descriptiion',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rooms.RoomType'),
        ),
    ]