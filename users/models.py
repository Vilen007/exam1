from django.db import models

# Create your models here.
class User_Table(models.Model):
    uname = models.CharField(max_length=50,default ="")
    fname = models.CharField(max_length=50,default ="")
    lname = models.CharField(max_length=50,default ="")
    password = models.CharField(max_length=50,default ="")
    phone = models.CharField(max_length=20,default ="")
    address = models.CharField(max_length=200,default ="")
    created = models.DateField()

    def __str__(self):
        return self.uname

class User_Role(models.Model):
    rname = models.CharField(max_length=50,default ="")
    rdetail = models.CharField(max_length=200,default ="")

    def __str__(self):
        return self.rname

class Users_Rights(models.Model):
    role_id = models.IntegerField(default=0)
    uname = models.CharField(max_length=50,default ="")
    right_name = models.CharField(max_length=300,default ="")
    right_detail = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.right_name

class  User_assign_role(models.Model):
    ftname = models.CharField(max_length=50,default ="")
    ltname = models.CharField(max_length=50,default ="")
    uname = models.CharField(max_length=50, default="")
    role_name = models.CharField(max_length=50,default ="")

    def __str__(self):
        return self.ftname
