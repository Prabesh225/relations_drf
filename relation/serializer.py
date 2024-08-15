from rest_framework import serializers
from .models import Singer, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'singer', 'duration')


class SingerSerializer(serializers.ModelSerializer):
    # Reference the related songs using the correct related_name 'song'
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(
    #     many=True, 
    #     read_only=True, 
    #     view_name='songs-detail'
    # )
    # song = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='duration',)
    song= SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ('id', 'name', 'gender', 'song',)

