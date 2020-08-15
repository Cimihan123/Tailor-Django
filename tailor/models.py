from django.db import models
from django import forms
from django.urls import reverse
from django.contrib.auth.models import User

GENDER_CHOICES =( 
    ("male", "male"), 
    ("female", "female"), 
 
) 


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30, null=True,blank=True)
    address = models.CharField(max_length=50, null=True,blank=True)
    age = models.IntegerField( null=True,blank=True)
    number = models.IntegerField( null=True,blank=True)
    type = models.CharField(max_length=50, null=True,blank=True)
    checkbox = models.BooleanField(null=True,default=False)
   
    order_date = models.DateField(blank=True,null=True)
    issue_date = models.DateField(blank=True,null=True)
    gender = models.CharField(choices = GENDER_CHOICES , max_length= 15)
   

    def __str__(self):
        return str(self.name)




class Male(models.Model):
    
    contact1 = models.OneToOneField(Contact,  on_delete=models.CASCADE,null=True)
    chest = models.CharField(max_length=30 , blank=True)
    neck = models.CharField(max_length=30 , blank=True)
    full_shoulder_width = models.CharField(max_length=30 , blank=True)
    right_sleeve = models.CharField(max_length=30 , blank=True)
    left_sleeve = models.CharField(max_length=30 , blank=True)
    bicep = models.CharField(max_length=30 , blank=True)
    shoulder_width = models.CharField(max_length=30 , blank=True)
    seat = models.CharField(max_length=30 , blank=True)
    arm_length = models.CharField(max_length=30 , blank=True)
    thigh = models.CharField(max_length=30 , blank=True)
    waist = models.CharField(max_length=30 , blank=True)
    wrist = models.CharField(max_length=30 , blank=True)
    hip = models.CharField(max_length=30 , blank=True)
    full_back_length = models.CharField(max_length=30 , blank=True)
    front_chest_width = models.CharField(max_length=30 , blank=True)
    def __str__(self):
       return str(self.contact1)

 


class Female(models.Model):
  
    contact2 = models.OneToOneField(Contact,  on_delete=models.CASCADE, null=True)
    fchest = models.CharField(max_length=30 , blank=True)
    fneck = models.CharField(max_length=30 , blank=True)
    fwaist = models.CharField(max_length=30 , blank=True)
    seat = models.CharField(max_length=30 , blank=True)
    shoulder_width = models.CharField(max_length=30 , blank=True)
    arm_length = models.CharField(max_length=30 , blank=True)
    wrist = models.CharField(max_length=30 , blank=True)
    hip = models.CharField(max_length=30 , blank=True)
    biceps = models.CharField(max_length=30 , blank=True)
    back_length = models.CharField(max_length=30 , blank=True)
    wrist = models.CharField(max_length=30 , blank=True)
    sleeve_length = models.CharField(max_length=30 , blank=True)
    arm_hole = models.CharField(max_length=30 , blank=True)
    bust = models.CharField(max_length=30 , blank=True)
    upper_bust = models.CharField(max_length=30 , blank=True)
    skirt_length = models.CharField(max_length=30 , blank=True)
    shoulder_to_shoulder = models.CharField(max_length=30 , blank=True)
    full_back_length = models.CharField(max_length=30 , blank=True)
    def __str__(self):
            return str(self.contact2)



class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=30 , blank=True)
    email = models.CharField(max_length=30 , blank=True)



class Product(models.Model):
    name = models.CharField(max_length=30 , blank=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    #image


    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=30 , blank=True)

    def __str__(self):
        return str(self.id)

    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True,blank=True)
    city = models.CharField(max_length=30 , blank=True)
    state = models.CharField(max_length=30 , blank=True)
    zipcode = models.CharField(max_length=30 , blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.address)



