from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=False):
        if not email:
            raise ValueError("Users must have an email address!")
        if not password:
            raise ValueError("Users must have an password!")

        user_obj = self.model(
            email = self.normalize_email(email)
        )
        
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
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

    
    def create_admin(self, email, password=None):
       
        user_obj = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user_obj


    

class Account(AbstractBaseUser):
    email                       = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    is_active                   = models.BooleanField(default=False)
    is_staff                    = models.BooleanField(default=False)
    is_admin                    = models.BooleanField(default=False)
    timestamp                   = models.DateTimeField(auto_now_add=True)
    secret_key                  = models.UUIDField(default=uuid.uuid4)

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
