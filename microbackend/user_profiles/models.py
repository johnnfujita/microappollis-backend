from django.db import models
from microaccounts.models import Account
# from django.db.models.signals import post_save
# from django.dispatch import receiver


from microaddressbook.models import NumberLevelAddress


class ConsumerProfile(models.Model):
    # This complement Account (UserAuth class) for the consumers
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, related_name="consumer_profile", null=True, blank=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    # #Define the bucket path
    # user_picture = models.ImageField()
    # # Every User will have an address to receive deliveries (it can be overwriten at checkout time)
    # address = models.ForeignKey(NumberLevelAddress, on_delete=models.CASCADE, related_name='consumers')

# class GovernmentIssuedId(models.Model):
# #   this is used as interface for different types of possible types of documents that a user may have e.g. cpf or rg
#     account = models.OneToOneField(Account, related_name='%(class)s_related', null=False, blank=False, on_delete=models.CASCADE)

#     class Meta():
#         abstract = True


# class CPF(GovernmentIssuedId):
#     id_number = models.CharField(unique=True, max_length=11, null=False, blank=False)
#     image = models.ImageField()
# #     # DEFINIR BUCKET PATH

# class RG(GovernmentIssuedId):
#     id_number = models.CharField(unique=True, max_length=11, null=False, blank=False)
#     image = models.ImageField()
# #     # DEFINIR BUCKET PATH

# # class ProfessionalIdentification(GovernmentIssuedId):
# #     id_number = models.CharField(max_length=11, null=False, blank=False)
# #     # The issuer is important in this case cause 
# #     issuer_agency = models.CharField(max_length=20, null=False, blank=False)
# #     image = models.ImageField()
# #     # DEFINIR BUCKET PATH

# #     class Meta:
# #         constraints = [
# #             models.UniqueConstraint(fields=['id_number', 'issuer_agency'], name='id_issuer_constraint')
# #         ]

# class CNPJ(GovernmentIssuedId):
#     id_number = models.CharField(max_length=16, null=False, blank=False)
#     image = models.ImageField()