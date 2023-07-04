# Generated by Django 4.2.3 on 2023-07-04 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('year', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]