from rest_framework import viewsets
from portfolio_app.models import Contact
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ItemSerializer
