from rest_framework import filters
from rest_framework import generics
from .serializers import ListingSerializer
from listings.models import Listing
from django_filters.rest_framework import DjangoFilterBackend


class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer


class ListingCreate(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingDelete(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingUpdate(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class ListingListSearch(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [filters.OrderingFilter,
                       DjangoFilterBackend, ]
    ordering_fields = ['date_posted', 'price']

    filterset_fields = {
        'make': ['in'],
        'car_model': ['iexact'],
        'body_type': ['iexact'],
        'engine': ['iexact'],
        'price': ['gte', 'lte'],
        'fabrication_year': ['gte', 'lte'],
        'location': ['iexact']
    }
