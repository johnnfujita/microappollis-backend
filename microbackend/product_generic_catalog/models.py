from django.db import models
from generic_vendor_profiles.models import GlobalSegment, VendorData


class ProductGenericClass(models.Model):
    #AdminOnly
        # example ArtProduct Beverage, Meat, Accessory, Jewel, Car, Candy, Dessert
    title = models.CharField(max_length=30, null=False, blank=False)
    segment = models.ForeignKey(GlobalSegment, related_name="generic_product_classes", on_delete=models.CASCADE, blank=False, null=False)

# class GenericProduct(models.Charfield):
#     # eexample car, painting neckless medical appoitment_hour, personal_trainer_hour, Beer, Wine, Wrist Watch, T-Shirt, Long-Pants,Coca-cola

#     name = models.CharField(max_length=100, null=False, blank=False)
#     generic_category = models.ForeignKey(ProductGenericClass, related_name='generic_products', on_delete=models.CASCADE null=False,  blank=False)


class ProductInstance(models.Model):
    parent_product = models.ForeignKey(ProductGenericClass,related_name="child_products", on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(unique=True, max_length=200, blank=False, default="")
    measure_unit = models.CharField(max_length=3, blank=False, null=False)
    created_by_vendor = models.ForeignKey(VendorData,on_delete=models.CASCADE,  blank=False, null=False, related_name="products_created",)
    is_branded = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # WE CAN ADD COLLECTION INFO BRAND MANUFACTOR
    # COLOR SIZE HERE 

class FoodNetStorage(models.Model):
    product = models.ForeignKey(ProductInstance, null=False, blank=False, on_delete=models.CASCADE)
    # this refers to the quantity that results from the computed value of in product (either by a formal order document, or an informal entry, same to the outbound movements)
    net_quantity = models.DecimalField(max_digits=16, decimal_places=2, blank=True, default=1)
    unit_cost = models.DecimalField(max_digits=16, decimal_places=2, blank=False, null=False)
    manufactor = models.CharField(max_length=100, blank=False, default="")
    unit_price = models.DecimalField(decimal_places=3, max_digits=14, null=False, blank=False)
    # this set to not keep track of the net quantity as a constraint for availability of the product
    # this is usefull for companies that do not wish to keep count of storage and simply want to sell, still if the unit_cost is made available, the liquid net can be calculed
    # the selling quantities and derived income are kept to date cause of the orders still holds all the selling operations.
    is_infinite = models.BooleanField(default=False, blank=True)


class FoodProductDisplaySection(models.Model):
    vendor = models.ForeignKey(VendorData,on_delete=models.CASCADE,  null=False, blank=False, related_name="sections")
    name = models.CharField(max_length=40, null=False, blank=False)
    parent_section = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name="sub_sections")
    # CLOTHES SECTIONS EXAMPLES SPORT,MEN,WOMEN,  SHORTS, JEANS, FOOTWEAR, WALLETS

class FoodProductAvailable(models.Model):
    #This displayed_at links to section that is especific to a Vendor
    displayed_at = models.ForeignKey(FoodProductDisplaySection, on_delete=models.CASCADE, null=False, related_name="products", blank=False)
    thumb = models.ImageField(upload_to="products", null=True, blank=True)
    details = models.CharField(max_length=250, blank=True, default="")
    #this links to a food that is checked to be available from the net storage 
    StoredFood = models.ForeignKey(FoodNetStorage, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    is_displayed = models.BooleanField(default=True, blank=True)

# CLOTHES EXAMPLE OF FIELDS COLOR, SIZE




# class GenericFoodProduct(models.Model):
#     # example Fillet Au Poivre, Chios, Cheetos, Milka Bar
#     label = models.CharField(max_length=100, null=False, blank=False, un )
#     measure_unit = models.CharField(max_length=10, null=False, blank=False)

# # class GenericClothingProduct(models.Model):
# #     # Watch Rolex,
# #     label = models.CharField(max_length=100, null=False, blank=False)
#     measure_unit = models.CharField(max_length=10, null=False, blank=False)


# class CreativeJuridicAndManagementProduct(models.Model):
#     # Legal Accessement, SongWriting, SongEditing, ManagementConsulting
#     label = models.CharField(max_length=100, null=False, blank=False)
#     measure_unit = models.CharField(max_length=10, null=False, blank=False)
#     # hour minute, unit, 

# class TransportProduct(models.Model):
#     # CarRepair, MotorcycleRepair, Car component x, hour of service
#     label = models.CharField()
#     label = models.CharField(max_length=100, null=False, blank=False)
#EntertainmentCultureProduct(models.Model):

#HousingAndConstructionProduct(models.Model):

#class EducationLearningProduct(models.Model):

#class SportHealthAndWellnessProduct(models.Model):

# class EletroEletronicProduct(models.Model)