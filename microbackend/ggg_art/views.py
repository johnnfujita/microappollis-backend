from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import ArtCategory, Artist, Artwork, Location, Technique, PrintedArtwork, LimitedArtwork
from .serializers import ArtCategorySerializer, ArtistSerializer, LocationSerializer, PrintedArtworkSerializer, LimitedArtworkSerializer, BasicArtworkSerializer, TechniqueSerializer,UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from rest_framework import filters

#from .customfilters import ArtworkFilter
from rest_framework import permissions
from . import custompermissions


from rest_framework.throttling import ScopedRateThrottle


# Create your views here.


class ArtCategoryList(generics.ListCreateAPIView):
    queryset = ArtCategory.objects.all()
    serializer_class = ArtCategorySerializer
    name = 'art-category-list'

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class ArtCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtCategory.objects.all()
    serializer_class = ArtCategorySerializer
    name = 'art-category-detail'


class TechniqueList(generics.ListCreateAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer
    name = 'technique-list'

class TechniqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Technique.objects.all()
    serializer_class = TechniqueSerializer
    name = 'technique-detail'



class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = BasicArtworkSerializer
    name = 'artwork-list'
    #filter_class = ArtworkFilter
    search_fields = ['^title','^artist__name']
    ordering_fields = (
        'artist',
        'price',
        'title',
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
       
    )

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


    
    

class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'artworks'
    throttle_classes = (ScopedRateThrottle, )
    queryset = Artwork.objects.all()
    serializer_class = BasicArtworkSerializer
    name = 'artwork-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
      
    )


class PrintedArtworkList(generics.ListCreateAPIView):
    queryset = PrintedArtwork.objects.all()
    serializer_class = PrintedArtworkSerializer
    name = 'printed-artwork-list'
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    
    

class PrintedArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = PrintedArtwork.objects.all()
    serializer_class = PrintedArtworkSerializer
    name = 'printed-artwork-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly
    )


class LimitedArtworkList(generics.ListCreateAPIView):
    queryset = LimitedArtwork.objects.all()
    serializer_class = LimitedArtworkSerializer
    name = 'limited-artwork-list'
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    
    

class LimitedArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = LimitedArtwork.objects.all()
    serializer_class = LimitedArtworkSerializer
    name = 'limited-artwork-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermissions.IsCurrentUserOwnerOrReadOnly
    )


class ArtistList(generics.ListCreateAPIView):
    throttle_scope = 'artworks'
    throttle_classes = (ScopedRateThrottle, )
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-list'
    filter_backends = [filters.SearchFilter]
    filter_field = (
        'name',
        'origin',
    )
    search_fields = ( '^name',)
    ordering_fields = ('name',)

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    name = 'artist-detail'

class LocationList(generics.ListCreateAPIView):
    trottle_scope = 'locations'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'location-list'

    filter_field = (
        'name',
    )
    search_fields = (
        '^name'
    )
    ordering_fields = (
        'name',
    )
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    trottle_scope = 'locations'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    name = 'location-detail'
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'art_categories': reverse('ggg_art:art-category-list', request=request),
            'artworks': reverse('ggg_art:artwork-list', request=request),
            'artists': reverse('ggg_art:artist-list', request=request),
            'locations': reverse('ggg_art:location-list', request=request),
            'techniques': reverse('ggg_art:technique-list', request=request)
        })



class RegisterTest(generics.GenericAPIView):
    serializer_class = UserSerializer
    name = 'register'
    def post(self, request, *args, **kwargs):
        
        return Response({
            'token': {
                "access": "aodjfoadjfoadjf34235fa",
                "refresh": "dfjoiajdfiaipfapfoaopfpoa"
            }
        })
    def get(self, request, *args, **kwargs):
        return Response({
            'token': {
                "access": "aodjfoadjfoadjf34235fa",
                "refresh": "dfjoiajdfiaipfapfoaopfpoa"
            }
        })