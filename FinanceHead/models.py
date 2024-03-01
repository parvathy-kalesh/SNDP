from django.db import models
from Admin.models import tbl_financehead,tbl_scheme,tbl_loan


# Create your models here.

class tbl_chitty(models.Model):
    chitty_name=models.CharField(max_length=50)
    chitty_details=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    scheme=models.ForeignKey(tbl_scheme,on_delete=models.CASCADE)

class tbl_addloanname(models.Model):
    loan_name=models.CharField(max_length=50)
    loan_details=models.CharField(max_length=50)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)
    loan_type=models.ForeignKey(tbl_loan,on_delete=models.CASCADE)


class tbl_monthlycollection(models.Model):
    amount=models.IntegerField()
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)


class tbl_weeklycollection(models.Model):
    amount=models.IntegerField()
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)

class tbl_chittycalender(models.Model):
    amount=models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField()
    no_installment=models.IntegerField()
    chitty_name=models.ForeignKey(tbl_chitty,on_delete=models.CASCADE)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)


class tbl_loancalender(models.Model):
    amount=models.IntegerField()
    startdate=models.DateField()
    enddate=models.DateField()
    no_installment=models.IntegerField()
    loan_name=models.ForeignKey(tbl_addloanname,on_delete=models.CASCADE)
    head=models.ForeignKey(tbl_financehead,on_delete=models.CASCADE)