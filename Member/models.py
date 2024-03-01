from django.db import models
from Admin.models import *
from Guest.models import *
from FinanceHead.models import *


# Create your models here.

class tbl_relatives(models.Model):
    relative_name=models.CharField(max_length=50)
    age=models.IntegerField()
    password=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=50)
    photo=models.FileField(upload_to="MemberDocs/")
    address=models.TextField()
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    relation_type=models.ForeignKey(tbl_relationtype,on_delete=models.CASCADE)
    refer_id=models.IntegerField()

class tbl_scholarshipapply(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to="MemberDocs/")
    scholarship_name=models.ForeignKey(tbl_scholarshipname,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)


class tbl_chittyjoin(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to="MemberDocs/")
    chittydata=models.ForeignKey(tbl_chitty,on_delete=models.CASCADE)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)
    apply_date=models.DateField(auto_now_add=True)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative_name=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)

class tbl_loanapply(models.Model):
    status=models.IntegerField(default=0)
    document=models.FileField(upload_to="MemberDocs/")
    loan_name=models.ForeignKey(tbl_addloanname,on_delete=models.CASCADE)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)
    apply_date=models.DateField(auto_now_add=True)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    
class tbl_electionapply(models.Model):
    status=models.IntegerField(default=0)
    election_name=models.ForeignKey(tbl_electiondeclaration,on_delete=models.CASCADE)
    election_position=models.ForeignKey(tbl_electionposition,on_delete=models.CASCADE)
    member_name=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)

class tbl_voting(models.Model):
    electionapply=models.ForeignKey(tbl_electionapply,on_delete=models.CASCADE)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)


class tbl_monthlycollectionpayment(models.Model):
    monthlycollection_id=models.ForeignKey(tbl_monthlycollection,on_delete=models.CASCADE)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    payment_date=models.DateField(auto_now_add=True)

class tbl_weeklycollectionpayment(models.Model):
    weeklycollection_id=models.ForeignKey(tbl_weeklycollection,on_delete=models.CASCADE)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)
    payment_date=models.DateField(auto_now_add=True)

class tbl_complaint(models.Model):
    title=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    content=models.CharField(max_length=50)
    reply=models.CharField(max_length=50)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)


class tbl_feedback(models.Model):
    content=models.CharField(max_length=50)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.SET_NULL,null=True)
    relative=models.ForeignKey(tbl_relatives,on_delete=models.SET_NULL,null=True)

class tbl_repaymentloan(models.Model):
    loanapply=models.ForeignKey(tbl_loanapply,on_delete=models.CASCADE)
    member=models.ForeignKey(tbl_memberadding,on_delete=models.CASCADE)
    repayment_date=models.DateField(auto_now_add=True)
    