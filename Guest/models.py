from django.db import models
from Admin.models import tbl_location

# Create your models here.

class tbl_memberadding(models.Model):
    member_name=models.CharField(max_length=50)
    age=models.IntegerField()
    password=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    gender=models.CharField(max_length=50)
    location=models.ForeignKey(tbl_location,on_delete=models.CASCADE)
    photo=models.FileField(upload_to="MemberDocs/")