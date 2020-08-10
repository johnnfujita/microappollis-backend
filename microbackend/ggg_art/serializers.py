from rest_framework import serializers
from .models import ArtCategory, Artist, Location, Artwork, Technique, PrintedArtwork, LimitedArtwork, OriginalArtwork
import ggg_art.views
from django.contrib.auth.models import User


class UserPrintedArtworkSerializer(serializers.ModelSerializer):
    artwork_base = serializers.SlugRelatedField(queryset=Artwork.objects.all(), slug_field="title")
    class Meta:
        model = PrintedArtwork
        fields = ('artwork_base', 'id')

class UserLimitedArtworkSerializer(serializers.ModelSerializer):
    artwork_base = serializers.SlugRelatedField(queryset=Artwork.objects.all(), slug_field="title")
    class Meta:
        model = LimitedArtwork
        fields = ('artwork_base', 'id')

class UserOriginalArtworkSerializer(serializers.ModelSerializer):
    artwork_base = serializers.SlugRelatedField(queryset=Artwork.objects.all(), slug_field="title")
    class Meta:
        model = OriginalArtwork
        fields = ('artwork_base', 'id')

class UserSerializer(serializers.ModelSerializer):
    printed_artworks = UserPrintedArtworkSerializer(many=True, read_only=True)
    limited_artworks = UserLimitedArtworkSerializer(many=True, read_only=True)
    original_artwork = UserOriginalArtworkSerializer(read_only=True)
    class Meta:    
        model = User
        fields = (
            'password',
            'original_artwork',
            'username',
            'printed_artworks',
            'limited_artworks',
        )
# class UserArtworkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artwork
#         fields = ('title', 'id')

# class UserSerializer(serializers.ModelSerializer):
#     artworks = UserArtworkSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = (
#             'pk',
#             'username',
#             'artworks'
#         )
class PrintedArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PrintedArtwork
        fields = '__all__'

class LimitedArtworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = LimitedArtwork
        fields = '__all__'

class BasicArtworkSerializer(serializers.ModelSerializer):

    # Display category name
    art_category = serializers.SlugRelatedField(queryset=ArtCategory.objects.all(), slug_field='name')
    artist = serializers.SlugRelatedField(queryset=Artist.objects.all(), slug_field='name')
    original_technique = serializers.SlugRelatedField(queryset=Technique.objects.all(), slug_field='name')
   
    
    printed_count = serializers.SerializerMethodField()
    limited_count = serializers.SerializerMethodField()
    min_price_printed = serializers.SerializerMethodField()
    min_price_limited = serializers.SerializerMethodField()
    price_original = serializers.SerializerMethodField()
    class Meta:
        model = Artwork
        fields = [
            'image',
            'id',
            'title', 
            'description',
            'slug',
            'artist',  
            'art_category', 
            'release_date', 
            'min_price_printed',
            'min_price_limited',
            'price_original',
            'printed_count',
            'limited_count',  
            'original_technique', 
            'height',
            'width'
        ]
        read_only_fields = ['printed_count', 'limited_count']
    def get_printed_count(self, obj):
        printed_count = 0
        print_items = obj.printed_artworks.filter(available=True)
        if print_items:
            printed_count = print_items.count()
            return printed_count
        return printed_count
    
    def get_limited_count(self, obj):
        limited_count = 0
        limited_items = obj.limited_artworks.filter(available=True)
        if limited_items:
            limited_count = limited_items.count()
            return limited_count
        return limited_count

    def get_min_price_printed(self, obj):
        min_price_printed = -1
        print_items = obj.printed_artworks.filter(available=True)
        
        if print_items:          
            prices = [item.price for item in print_items]
            min_price_printed = min(prices)
            return min_price_printed
        return min_price_printed

    
    def get_min_price_limited(self, obj):
        min_price_limited = -1
        limited_items = obj.limited_artworks.filter(available=True)
        if limited_items:
            prices = [item.price for item in limited_items]
            min_price_limited = min(prices)
            print(min_price_limited)
            return min_price_limited
        return min_price_limited

    def get_price_original(self, obj):
        original_price = -1
        original = obj.original.filter(available=True)
        if original:
            original_price = original[0].price
            return original_price
        return original_price


class TechniqueSerializer(serializers.ModelSerializer):
    artworks = BasicArtworkSerializer(many=True, read_only=True)
    class Meta:
        model = Technique
        fields = ['id', 'name', 'description', 'artworks']

class LocationSerializer(serializers.ModelSerializer):
    artworks = BasicArtworkSerializer(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ['name', 'artworks']


class ArtistSerializer(serializers.ModelSerializer):
    artworks = BasicArtworkSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['name', 'origin', 'artworks']



class ArtCategorySerializer(serializers.ModelSerializer):
    artworks = BasicArtworkSerializer(many=True, read_only=True)
    class Meta:
        model = ArtCategory
        fields = ['name', 'artworks']


# class ArtworkCompleteSerializer(serializers.ModelSerializer):

#     # Display category name
#     art_category = serializers.SlugRelatedField(queryset=ArtCategory.objects.all(), slug_field='name')
#     artist = ArtistSerializer()
#     displayed_at = LocationSerializer()
#     technique = TechniqueSerializer()
#     class Meta:
#         model = Artwork
#         fields = [
#             'title',
#             'displayed_at', 
#             'artist',
#             'description',
#             'slug',  
#             'art_category', 
#             'release_date', 
#             'available_original', 
#             'limited_available', 
#             'printed_available',
#             'price',
#             'price_limited',
#             'price_printed',
#             'technique'
#         ] 

