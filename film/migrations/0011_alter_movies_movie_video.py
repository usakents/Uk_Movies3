# Generated by Django 3.2.7 on 2021-10-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0010_auto_20211017_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_video',
            field=models.FileField(upload_to='m_videos'),
        ),
    ]
