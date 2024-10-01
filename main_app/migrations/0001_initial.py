# Generated by Django 5.1.1 on 2024-10-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poke_id', models.IntegerField()),
                ('xp', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('ablilities', models.TextField()),
                ('moves', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
