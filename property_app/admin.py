from django.contrib import admin
from property_app.models import (LoginRole,LoginUser,
                                 State,District,Taluk,
                                 Panchayat,PropertyType,
                                 PublicProperty,Attribute,
                                 PropertyDetails
                                 )

# Register your models here.
admin.site.register(LoginRole)
admin.site.register(LoginUser)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Taluk)
admin.site.register(Panchayat)
admin.site.register(PropertyType)
admin.site.register(PublicProperty)
admin.site.register(Attribute)
admin.site.register(PropertyDetails)