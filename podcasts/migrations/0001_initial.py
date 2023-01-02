# Generated by Django 4.1.4 on 2022-12-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField()),
                ('image', models.URLField()),
                ('podcast_name', models.CharField(max_length=100)),
                ('guid', models.CharField(max_length=50)),
            ],
        ),
    ]