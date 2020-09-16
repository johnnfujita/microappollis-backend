from django.db import models

# Create your models here.

# Create your models here.
class ZipCodeLevelAddress(models.Model):
    # There will be only one enter for zipcode
    zip_code = models.CharField(max_length=8, unique=True, blank=False, null=False)
    country = models.CharField(max_length=3, blank=True, default="BR")
    state = models.CharField(max_length=2, blank=True, default="CE")
    city = models.CharField(max_length=85, blank=True, default="Fortaleza")
    street_name = models.CharField(max_length=150, blank=False, null=False)
    

class NumberLevelAddress(models.Model):
    # this will ensure that only complete address will be used, by all the users who live or work at the same place
    base_address = models.ForeignKey(ZipCodeLevelAddress, on_delete=models.CASCADE, related_name="complete_child_addresses", null=False, blank=False )    
    street_number = models.CharField(max_length=5, null=False, blank=False)
    complement = models.CharField(max_length=12, blank=True, default="")
    find_helper = models.CharField(max_length=200, blank=True, default="")