from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, 
                    email,
                    # name, 
                    # cpf,
                    # address_street,
                    # address_number,
                    # complement,
                    # card_holder_name,
                    # card_number,
                    # card_expiration,
                    # card_type,
                    # card_security_code,
                    # card_brand,
                    is_staff=False, 
                    is_admin=False, 
                    is_active=False,
                    is_superuser=False,
                    password=None,
                    ):
        if not email:
            raise ValueError("Users must have an email address!")
        if not password:
            raise ValueError("Users must have an password!")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        # user_obj.name = name
        # user_obj.cpf = cpf
        # user_obj.address_street = address_street
        # user_obj.address_number = address_number        
        # user_obj.complement = complement
        # user_obj.card_holder_name = card_holder_name
        # user_obj.card_number = card_number
        # user_obj.card_expiration = card_expiration
        # user_obj.card_type = card_type
        # user_obj.card_security_code = card_security_code
        # user_obj.card_bramd = card_brand
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)

        return user_obj

    def create_staff(self, email, password=None):
       
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True,
        )
        return user_obj

    
    def create_superuser(self, email, password=None):
       
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user_obj


    

class Account(AbstractBaseUser, PermissionsMixin):
    email                       = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    is_active                   = models.BooleanField(default=False)
    is_staff                    = models.BooleanField(default=False)
    is_admin                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    timestamp                   = models.DateTimeField(auto_now_add=True)
    secret_key                  = models.UUIDField(default=uuid.uuid4)
    
    # #profile data
    # name                        = models.CharField(max_length=100, null=False, blank=False)
    # cpf                         = models.CharField(max_length=11, null=False, blank=False)
    # address_street                     = models.CharField(max_length=50, null=False, blank=False)
    # address_number              = models.CharField(max_length=5, blank=False, null=False)
    # complement                  = models.CharField(max_length=15, blank=True, default="")

    # Payment
    # card_holder_name            = models.CharField(max_length=100, null=False, blank=False)
    # card_number                 = models.CharField(max_length=16, null=False, blank=False)
    # card_expiration                  = models.CharField(max_length=7, null=False, blank=False)
    # card_type                   = models.CharField(max_length=100, null=False, blank=False)
    # card_security_code               = models.CharField(max_length=3, null=False, blank=False)
    # card_brand                       = models.CharField(max_length=12, null=False, blank=False)



#     #{
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
#{  
#    "MerchantOrderId":"2014121201",
#    "Customer":{  
#       "Name":"Paulo Henrique"     
#    },
#    "Payment":{  
#      "Type":"DebitCard", ok
#      "Amount":15700,
#      "Provider":"Simulado", what
#      "ReturnUrl":"http://www.google.com.br",
#      "DebitCard":{  
#          "CardNumber":"4532117080573703", ok
#          "Holder":"Teste Holder", ok
#          "ExpirationDate":"12/2019", ok
#          "SecurityCode":"023", ok
#          "Brand":"Visa" ok
#      }
#    }
# }
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
    
   



# class IPAddress(models.Model):
#     host_accounts = models.ManyToManyField(Account, related_name="known_ips", null=False, blank=False)
#     ip_number = models.GenericIPAddressField(unique=True, null=False, blank=False)

# class PhoneNumber(models.Model):
#     user                        = models.OneToOneField(Account,on_delete=models.CASCADE,  null=False, blank=False)
#     mobile_country_code         = models.CharField(max_length=3, blank=True, default="+55")
#     mobile_regional_code        = models.CharField(max_length=3, blank=True, default="85")
#     mobile_phone                = models.CharField(max_length=9, null=False, blank=False)
