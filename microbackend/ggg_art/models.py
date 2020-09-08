from django.db import models
from django.conf import settings 
from .utilities import artist_directory_path, location_directory_path
from product_generic_catalog.models import ProductGenericClass

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
    name = models.CharField(max_length=100, blank=False, null=False)
    origin = models.CharField(max_length=100, blank=True, default='')
    history = models.CharField(max_length=400, blank=True, default="" )
    #tags
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
    # vendor = models.ForeignKey(VendorDataLink, null=F
    # 
    #address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=False, null=True )
    created = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(blank=True, null=True, upload_to=location_directory_path)
    #manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='stores_controlled_by', on_delete=models.CASCADE)
    #profit_share = models.DecimalField(decimal_places=2, max_digits=4, blank=True, default=0.0) 
    def __str__(self):
        return self.name


class Artwork(models.Model):
    #parent_product = models.ForeignKey(ProductGenericClass, on_delete=models.CASCADE, related_name="artworks", null=False, blank=False)
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
    # tags 
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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='printed_artworks', on_delete=models.CASCADE)
    available = models.BooleanField(default=False, blank=False)
    #accessible only to admin
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        ordering = ('artwork_base','price', 'owner')
    def __str__(self):
        return self.artwork_base


class LimitedArtwork(models.Model):
    artwork_base = models.ForeignKey(Artwork, related_name="limited_artworks", on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=12, blank=False, decimal_places=2)
    displayed_at = models.ForeignKey(Location, related_name="limited_artworks", on_delete=models.CASCADE, blank=False, default=1)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='limited_artworks', on_delete=models.CASCADE, blank=True, null=True)
    available = models.BooleanField(default=False, blank=False)
    #accessible only to admin
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('artwork_base','price', 'owner')
    def __str__(self):
        return self.artwork_base

class OriginalArtwork(models.Model):
    artwork_base = models.ForeignKey(Artwork, unique=True,  related_name='original', on_delete=models.CASCADE, blank=False, null=False)
    price = models.DecimalField(default=0.00, max_digits=12, blank=False, decimal_places=2)
    displayed_at = models.ForeignKey(Location, related_name="original", on_delete=models.CASCADE, blank=False, default=1)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='original_artworks', on_delete=models.CASCADE)
    available = models.BooleanField(default=False, blank=False)
    #accessible only to admin
    #company_owner = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('artwork_base','price', 'owner')
    def __str__(self):
        return self.artwork_base


class OrderArtwork(models.Model):
    item                    = models.ForeignKey(OriginalArtwork, on_delete=models.CASCADE)
    buyer                   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at              = models.DateTimeField(auto_now_add=True)


class CieloOrderResponse(models.Model):
    proof_of_sale          = models.CharField(max_length=6, null=False, blank=False)
    tid                    = models.CharField(max_length=20, null=False, blank=False)
    authorization_code     = models.CharField(max_length=6, null=False, blank=False)
    payment_id             = models.CharField(max_length=36, null=False, blank=False)
    status                 = models.CharField(max_length=4, null=False, blank=False)
    return_code            = models.CharField(max_length=32, null=False, blank=False)
    return_message          = models.CharField(max_length=512, null=False, blank=False)
    order_related           = models.OneToOneField(OrderArtwork, on_delete=models.CASCADE)

#{
#    "MerchantOrderId":"2014111703",
#    "Payment":{
#      "Type":"CreditCard", ok
#      "Amount":15700,
#      "Installments":1,
#      "SoftDescriptor":"123456789ABCD",
#      "CreditCard":{
#          "CardNumber":"4551870000000183", ok
#          "Holder":"Teste Holder", ok
#          "ExpirationDate":"12/2021", ok
#          "SecurityCode":"123",ok
#          "Brand":"Visa"ok
#      }
#    }
# }