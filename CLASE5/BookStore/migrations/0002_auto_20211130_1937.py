# Generated by Django 3.2.9 on 2021-11-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='lastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='synopsis',
            new_name='sysnopsis',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
