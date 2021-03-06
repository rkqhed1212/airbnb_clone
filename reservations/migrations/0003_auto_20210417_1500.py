# Generated by Django 2.2.5 on 2021-04-17 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20210414_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='amentities',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='reservations.Amentity'),
        ),
    ]
