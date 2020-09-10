from django.db import models
from microaccounts.models import Account
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.
# class ZipCodeLevelAddress(models.Model):
#     # There will be only one enter for zipcode
#     zip_code = models.CharField(max_length=8, unique=True, blank=False, null=False)
#     country = models.CharField(max_length=3, blank=True, default="BR")
#     state = models.CharField(max_length=2, blank=True, default="CE")
#     city = models.CharField(max_length=85, blank=True, default="Fortaleza")
#     street_name = models.CharField(max_length=150, blank=False, null=False)
    

# class NumberLevelAddress(models.Model):
#     # this will ensure that only complete address will be used, by all the users who live or work at the same place
#     base_address = models.ForeignKey(ZipCodeLevelAddress, on_delete=models.CASCADE, related_name="complete_child_addresses", null=False, blank=False )    
#     street_number = models.CharField(max_length=5, null=False, blank=False)
#     complement = models.CharField(max_length=12, blank=True, default="")
#     find_helper = models.CharField(max_length=200, blank=True, default="")
    

class ConsumerProfile(models.Model):
    # This complement Account (UserAuth class) for the consumers
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, related_name="consumer_profile", null=True, blank=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    # #Define the bucket path
    # user_picture = models.ImageField()
    # # Every User will have an address to receive deliveries (it can be overwriten at checkout time)
    # address = models.ForeignKey(NumberLevelAddress, on_delete=models.CASCADE, related_name='consumers')

# class GovernmentIssuedId(models.Model):
#     # this is used as interface for different types of possible types of documents that a user may have e.g. cpf or rg
#     account = models.OneToOneField(Account, related_name='%(class)s_related', null=False, blank=False, on_delete=models.CASCADE)

#     class Meta():
#         abstract = True


# class CPF(GovernmentIssuedId):
#     id_number = models.CharField(unique=True, max_length=11, null=False, blank=False)
#     image = models.ImageField()
#     # DEFINIR BUCKET PATH

# class RG(GovernmentIssuedId):
#     id_number = models.CharField(unique=True, max_length=11, null=False, blank=False)
#     image = models.ImageField()
#     # DEFINIR BUCKET PATH

# class ProfessionalIdentification(GovernmentIssuedId):
#     id_number = models.CharField(max_length=11, null=False, blank=False)
#     # The issuer is important in this case cause 
#     issuer_agency = models.CharField(max_length=20, null=False, blank=False)
#     image = models.ImageField()
#     # DEFINIR BUCKET PATH

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['id_number', 'issuer_agency'], name='id_issuer_constraint')
#         ]

# class CNPJ(GovernmentIssuedId):
#     id_number = models.CharField(max_length=16, null=False, blank=False)
#     image = models.ImageField()