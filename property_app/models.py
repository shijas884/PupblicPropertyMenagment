from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class LoginUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN','ADMIN'
        WRITER = 'WRITER','WRITER'
        VIEWER = 'VIEWER','VIEWER'
    
    role_type = models.CharField(max_length=100,choices=Role.choices,null=True,blank=True)



    def __str__(self):
        return  self.username
    

class State(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(LoginUser, on_delete=models.SET_NULL,null=True,blank=True ,related_name='state_created')



    def __str__(self):
        return  self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(LoginUser,on_delete=models.SET_NULL,null=True,blank=True,related_name='district_created')
    state = models.ForeignKey(State, on_delete=models.SET_NULL,null=True,blank=True)
    

    def __str__(self):
        return  self.name


class Taluk(models.Model):
    name = models.CharField(max_length=100)
    discrete = models.ForeignKey(District, on_delete=models.SET_NULL,blank=True, null=True )


    def __str__(self):
        return  self.name


class Panchayat(models.Model):
    name = models.CharField(max_length=100)
    taluk = models.ForeignKey(Taluk, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return  self.name


class PropertyType(models.Model):
    name =  models.CharField(max_length=100)
    created_by = models.ForeignKey(LoginUser, on_delete=models.SET_NULL, blank=True,null=True, related_name='propertype_created')

    
    def __str__(self):
        return  self.name


class PublicProperty(models.Model):
    name = models.CharField(max_length=225)
    property = models.ForeignKey(PropertyType, on_delete=models.SET_NULL,blank=True, null=True, related_name='publicproperty_related')
    panchayat = models.ForeignKey(Panchayat, on_delete=models.SET_NULL,blank=True, null=True,)



    def __str__(self):
        return  self.name


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=225)
    propertytype = models.ForeignKey(PropertyType, on_delete=models.SET_NULL,blank=True, null=True, related_name='attribute_related')
    created_by = models.ForeignKey(LoginUser, on_delete=models.SET_NULL,blank=True, null=True, related_name='attribute_created')

    
    def __str__(self):
        return  self.attribute_name


class PropertyDetails(models.Model):
    public_property = models.ForeignKey(PublicProperty, on_delete=models.SET_NULL,blank=True, null=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL,blank=True, null=True)
    attribute_value = models.CharField(max_length=225)
    created_by = models.ForeignKey(LoginUser, on_delete=models.SET_NULL,blank=True, null=True,  related_name='details_created')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  (f'datails of {self.public_property.name}')



