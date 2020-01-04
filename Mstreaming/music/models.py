from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    album_title = models.CharField(max_length=100, default='')
    owner = models.ForeignKey('auth.User', related_name='songs', on_delete=models.CASCADE, null=True, blank=True)
    artist = models.ForeignKey(User, related_name='album', on_delete=models.CASCADE, default='', blank=True, null=True)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=False, null=False)
    song_title = models.CharField(max_length=250, default='')
    feat_artist = models.ForeignKey(User, on_delete=models.CASCADE, default='', blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='feat_songs', on_delete=models.CASCADE, null=True, blank=True)


class FeatSong(models.Model):
    feat_songs = models.ManyToManyField(Song)

# (User, related_name='song', default='', blank=True)

