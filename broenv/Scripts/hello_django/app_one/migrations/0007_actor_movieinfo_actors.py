# Generated by Django 5.0.1 on 2024-01-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0006_movieinfo_directed_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='actors',
            field=models.ManyToManyField(related_name='acted_movies', to='app_one.actor'),
        ),
    ]
