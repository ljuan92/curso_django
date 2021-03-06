# Generated by Django 3.2.9 on 2021-12-09 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPaperApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalist',
            old_name='lastName',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='journalist',
            old_name='themes',
            new_name='thems',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='name',
            new_name='create_date',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaperApp.news')),
            ],
        ),
    ]
