# Generated by Django 5.0.4 on 2024-04-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
