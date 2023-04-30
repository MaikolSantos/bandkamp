from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    album_id = serializers.IntegerField(read_only=True, source="album.id")

    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]
