# Generated by Django 2.2.6 on 2020-01-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200104_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='feat_songs',
        ),
        migrations.CreateModel(
            name='FeatSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feat_songs', models.ManyToManyField(to='music.Song')),
            ],
        ),
    ]
