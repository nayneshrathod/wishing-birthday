# Generated by Django 3.0.8 on 2020-08-15 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toname', models.CharField(max_length=120)),
                ('fromname', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
