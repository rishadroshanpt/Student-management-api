# Generated by Django 5.1.4 on 2025-01-10 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.IntegerField()),
                ('name', models.TextField()),
                ('course', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
