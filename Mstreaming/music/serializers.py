from rest_framework import serializers
from .models import Album, Song
from django.contrib.auth.models import User


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='album-detail', format='html')

    class Meta:
        model = Album
        fields = ['id', 'album_title', 'url', 'owner']


class SongSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    class Meta:
        model = Song
        fields = ['album', 'song_title', 'feat_artist', 'artist']


class FeatSongSerializer(serializers.RelatedField):
    song = serializers.HyperlinkedRelatedField(many=True, view_name='song-detail', read_only=True)

    def to_representation(self, value):
        return '%s' % value.song_title


class UserSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(many=True, view_name='song-detail', read_only=True)
    feat_songs = FeatSongSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'songs', 'feat_songs']


"""
class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    album_title = serializers.CharField(max_length=50, default='')
    album_logo = serializers.CharField(required=False, allow_blank=True, max_length=1000, default='')

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.album_title = validated_data.get('album_title', instance.album_title)
        instance.feat_artist = validated_data.get('feat_artist', instance.feat_artist)
        instance.album_logo = validated_data.get('album_logo', instance.album_logo)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Album.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'owner']


class SongSerializer(serializers.Serializer):
    album = serializers.CharField(max_length=50)
    song_title = serializers.CharField(max_length=50)
    feat_artist = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.album = validated_data.get('album', instance.album)
        instance.song_title = validated_data.get('song_title', instance.song_title)
        # instance.feat_artist = validated_data.get('feat_artist', instance.feat_artist)
        instance.save()
        return instance

    class Meta:
        model = Song
        fields = ['album', 'song_title', 'feat_artist']
"""
