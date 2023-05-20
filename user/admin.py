from django.contrib import admin
from .models import LookUpType ,LookUpValue ,Users

# Register your models here.
admin.site.register(LookUpType)
admin.site.register(LookUpValue)
admin.site.register(Users)