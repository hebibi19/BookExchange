# Generated by Django 3.2.16 on 2023-02-09 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200, unique=True)),
                ('link', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
