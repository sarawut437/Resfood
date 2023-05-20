from django.db import models

# Create your models here.
class Store(models.Model):
    name_store = models.CharField(max_length=50,blank=True,null=True)
    stampin_reg = models.DateTimeField(auto_created=True,blank=True,null=True)
    expire_store = models.DateTimeField(auto_created=True,blank=True,null=True)
    level_store = models.IntegerField(blank=True,null=True) 
    dle_flg = models.BooleanField(default=False)
    user_id_main = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name 

class Zone(models.Model):
    name_zone = models.CharField(max_length=50,blank=True,null=True)
    id_store = models.ForeignKey(Store,on_delete=models.DO_NOTHING,blank=True,null=True)
    dle_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tables(models.Model):
    name_table = models.CharField(max_length=50,blank=True,null=True)
    id_zone = models.ForeignKey(Zone,on_delete=models.DO_NOTHING,blank=True,null=True)
    id_store = models.ForeignKey(Store,on_delete=models.DO_NOTHING,blank=True,null=True)
    dle_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name_menu = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    price =  models.IntegerField(blank=True,null=True)
    img = models.CharField(max_length=50,blank=True,null=True)
    type_menu_id =  models.IntegerField(blank=True,null=True)
    status_id = models.BooleanField(default=False)
    id_store = models.ForeignKey(Store,on_delete=models.DO_NOTHING,blank=True,null=True)
    dle_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class StaffStore(models.Model):
    user_id = models.IntegerField(blank=True,null=True)
    id_store = models.ForeignKey(Store,on_delete=models.DO_NOTHING,blank=True,null=True)
    dle_flg = models.BooleanField(default=False)
    role_staff_id = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

