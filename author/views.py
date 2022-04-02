from rest_framework import viewsets
from .serializer import AuthorSerializer
from .models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer