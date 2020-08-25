from django.db import models
from product_generic_catalog.models import FoodNetStorage
from ggg_art.models import PrintedArtwork, OriginalArtwork, LimitedArtwork
from django.conf import settings 

# DOCUMENTS TO BE GENERATED FOR EVERY ORDER WITHIN MOU
# REMEMBER THAT IN THE END THIS IS TO MICROAPPOLLIS (THE PAYMENT)
class OrderDocument(models.Model):
    doc_image = models.ImageField(upload_to="")
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="buying_doc_orders", null=True, blank=True, on_delete=models.CASCADE)
    payment_option = models.CharField(max_length=6, null=False, blank=False)
    # cielo_transaction_number
    # the front will take care to segment the order items by the seller and create a single order document for each seller that may have products mixed in the cart
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="selling_doc_orders", null=True, blank=True, on_delete=models.CASCADE)
    doc_serial = models.CharField(max_length=25, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# class GenericTasks(models.Models):
# create options of status finished, running, cancelled, waiting, paused
#     name = models.CharField(max_length=6, null=False, blank=False)
#     started = models.DateTimeField()
#     next_task = models.ForeignKey('self', null=True, blank=True)
#     status = models.CharField(max_lenght='5', null=False, blank=False)
#     finished_time = models.DateTimeField(null=True, blank=True)

# THE ITEMS LISTED IN A ORDER
class Payment(models.Model):
    order = models.ForeignKey(OrderDocument, on_delete=models.CASCADE, null=False, blank=False)
    value = models.DecimalField(max_digits=14, decimal_places=2, null=False, blank=False)
    payed = models.BooleanField(default=False)
    payed_at = models.DateTimeField(null=True, blank=True)
    due = models.DateTimeField(null=False, blank=False)
    
# compute the mou fee and all the fees
    # these are for now, microappollis = .07, which accounts for the retained .xx of cielo, there's ggg(intemediary) fee for art, finally location fee () 
    # has to check if theses fees are must be charged, and align them to the payments schedule or withdraw at data 0 the rest is the value owned
    # to the seller, the net value of the sell this value is kept as a debt of mou as soon as the payment is confirmed
class PaymentCredits(models.Model):
    pass


class OrderItem(models.Model):
    unit = models.CharField(max_length=2, blank=True, default='unidade')
    order = models.ForeignKey(OrderDocument, related_name='%(class)s_related', null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        abstract = True

    
class FoodProductDisplayedRelatedToItem(OrderItem):
    product = models.ForeignKey(FoodNetStorage,
                                related_name='food_order_items',
                                on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)

 
class PrintedArtworkRelatedToItem(OrderItem):
    # this product has a location field, this location has a fee percentage, 
    # also it has an owner which has a percentage to the product, 
    # this is the value that will be owned to the owner and to the location the 0.07 will hit the intermediary
    # sequence to charge full price => full-price * 0.07 (mou+cielo) => full-price * (for artintermediary-fee -0.07) => full-price-(for art locatiotion-fee)
    # right after this calcule based on the product, the value may be collected from cielo, or may be withold
    #at this point everyone has a credit to microappollis that has equivalent value of credit from cielo
    # if cielo deliver the money, than microappollis has a debt to everyone, an has a reserve to cover this value
    # on a given date... if a owner wants to withdraw the value early we will charge a fee,
    # if the owner set to retrieve the money always, it will receive the money
    # if it wants to keep the money within microappollis it will charge for the next buy * 0.01
    # microappollis real-credits
    product = models.OneToOneField(PrintedArtwork,
                                on_delete=models.CASCADE)

class LimitedArtworkRelatedToItem(OrderItem):
    product = models.OneToOneField(PrintedArtwork,
                                on_delete=models.CASCADE)


class OriginalArtworkRelatedToItem(OrderItem):
    product = models.OneToOneField(OriginalArtwork,
                                on_delete=models.CASCADE)
   