from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from .models import Song
from albums.models import Album
from .serializers import SongSerializer


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):     
        return Song.objects.filter(album_id=self.kwargs["pk"])
    
    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        serializer.save(album=album)

