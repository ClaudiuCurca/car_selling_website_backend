from rest_framework import generics
from .serializers import ListingSerializer
from listings.models import Listing


class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer
