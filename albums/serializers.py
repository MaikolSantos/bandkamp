from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Album
        fields = ["id", "name", "year", "user_id"]
