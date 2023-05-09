from django.db import models


# Create your models here.
class LookUpType(models.Model):
    value_code = models.CharField(max_length=50,blank=True,null=True)
    dle_flg = models.BooleanField(default=False)

class LookUpValue(models.Model):
    type_code_id = models.ForeignKey(LookUpType,on_delete=models.DO_NOTHING,blank=True,null=True)
    value_code = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    dle_flg = models.BooleanField(default=False)
    att1 = models.CharField(max_length=50,blank=True,null=True)
    att2 = models.CharField(max_length=50,blank=True,null=True)
    att3 = models.JSONField(blank=True,null=True)

class Users(models.Model):
    username = models.CharField(max_length=50,blank=True,null=True)
    password = models.CharField(max_length=50,blank=True,null=True)
    frist_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    role_id = models.ForeignKey(LookUpValue,on_delete=models.DO_NOTHING,blank=True,null=True)
    id_card = models.CharField(max_length=128,blank=True,null=True)
    email = models.EmailField(max_length = 254)
    dle_flg = models.BooleanField(default=False)
