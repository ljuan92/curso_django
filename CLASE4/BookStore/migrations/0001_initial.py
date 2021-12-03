# Generated by Django 3.2.9 on 2021-11-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('synopsis', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('editorial', models.CharField(max_length=60)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]