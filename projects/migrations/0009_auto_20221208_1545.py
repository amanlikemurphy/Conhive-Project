# Generated by Django 2.1.15 on 2022-12-08 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_youtube_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
