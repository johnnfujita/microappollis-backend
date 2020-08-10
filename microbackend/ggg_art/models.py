from django.db import models

from .utilities import artist_directory_path

class ArtCategory(models.Model):
    name = models.CharField(max_length=255,blank=False, null=False, unique=True)

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

# class Address(models.Model):
#     street_name = models.CharField(max_length=255, null=False, blank=False)
#     street_number = models.CharField(max_length=8, null=False, blank=False)
#     complement = models.CharField(max_length=30, blank=True, null=True)
#     zip_code = models.IntegerField(unique=True, max_length=8, null=False, blank=False)


class Artist(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    origin = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    

class Technique(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False, unique=True)
    description = models.CharField(max_length=500, blank=True, default="")
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    #address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=False, null=True )
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Artwork(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to=artist_directory_path)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False, default='')
    slug = models.SlugField(max_length=300, blank=False, null=False, unique=True)
    description = models.CharField(max_length=300, blank=True, default='')
    art_category = models.ForeignKey(ArtCategory, related_name='artworks', on_delete=models.CASCADE , null=False, blank=False)
    artist = models.ForeignKey(Artist, related_name='artworks', on_delete=models.CASCADE , null=False, blank=False)
    release_date = models.DateTimeField()
    original_technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='artworks', null=False, blank=False)
    height = models.DecimalField(max_digits= 8, decimal_places=3, blank=False, null=False)
    width = models.DecimalField(max_digits=8, decimal_places=3, null=False, blank=False)
    class Meta:
        ordering = ('artist', 'title')
       

    def __str__(self):
        return f'{self.artist} - {self.title}'

        # TODO: have to create the order class model, that takes items and count, pricing also, payments that as long one is open the order is not finished, also has a delivery linked to know if the order is due, and have a cielo order id, an owner,
        # the owner to the artwork_instance need a comission field to properly discount when sold

class PrintedArtwork(models.Model):
    artwork_base = models.ForeignKey(Artwork, related_name="printed_artworks", on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=12, blank=False, decimal_places=2)
    displayed_at = models.ForeignKey(Location, related_name="printed_artworks", on_delete=models.CASCADE, blank=False, default=1)
    is_printed = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='printed_artworks', on_delete=models.CASCADE)
    available = models.BooleanField(default=False, blank=False)
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

class LimitedArtwork(models.Model):
    artwork_base = models.ForeignKey(Artwork, related_name="limited_artworks", on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=12, blank=False, decimal_places=2)
    displayed_at = models.ForeignKey(Location, related_name="limited_artworks", on_delete=models.CASCADE, blank=False, default=1)
    owner = models.ForeignKey('auth.User', related_name='limited_artworks', on_delete=models.CASCADE, blank=True, null=True)
    available = models.BooleanField(default=False, blank=False)
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

class OriginalArtwork(models.Model):
    artwork_base = models.ForeignKey(Artwork, unique=True,  related_name='original', on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=12, blank=False, decimal_places=2)
    displayed_at = models.ForeignKey(Location, related_name="original", on_delete=models.CASCADE, blank=False, default=1)
    owner = models.ForeignKey('auth.User', related_name='original_artworks', on_delete=models.CASCADE)
    available = models.BooleanField(default=False, blank=False)
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)