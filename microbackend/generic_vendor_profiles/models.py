from django.db import models
from django.conf import settings

# BASE FOR THE 8 to 10 SEGMENTS THAT ALL VENDORS AND PRODUCTS WILL DERIVE FROM 
class GlobalSegment(models.Model):
    #AdminOnly
    title = models.CharField(max_length=25, null=False, unique=True, blank=False)
    # EG alimentacao... entretenimento/cultura

# THE TYPE OF STORE
class VendorCategory(models.Model):
    # AdminEditOnly
    # EG restaurantes ... arte
    title = models.CharField(max_length=30, unique=True, blank=False, null=False)
    segment = models.ForeignKey(GlobalSegment, related_name="vendor_categories", null=False, blank=False, default=1, on_delete=models.CASCADE)

# THE GRANULATED MAIN ACTIVITY OF A STORE
class VendorSubCategory(models.Model):
    #adminEditOnly
    # EG Pizzaria... museu, galeria, estudio 
    title = models.CharField(max_length=30, unique=True, blank=False, null=False)
    category = models.ForeignKey(VendorCategory, related_name="children_categories", blank=False, null=False, on_delete=models.CASCADE)


# ALL THE VENDOR DATA THAT IS ATTACHED TO THE ACOUNTS THAT ARE LISTED TO SELL PRODUCTS
class VendorData(models.Model):
    CPF = "CPF"
    CNPJ = "CNPJ"

    TYPE_CHOICES = [(CNPJ, "CNPJ"), (CPF, "CPF")]

    vendor_category = models.ForeignKey(VendorSubCategory, on_delete=models.CASCADE, related_name="vendors", blank=False, null=False )
    vendor_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor_profile_data", null=False, blank=False)
    vendor_type = models.CharField(max_length=4, choices=TYPE_CHOICES)
