from django.db import models

# Create your models here.
class tbl_adminlogin(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)

class tbl_location(models.Model):
    location_name=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_loan(models.Model):
    loan_name=models.CharField(max_length=50)

class tbl_proof(models.Model):
    proof_name=models.CharField(max_length=50)

class tbl_scheme(models.Model):
    scheme_name=models.CharField(max_length=50)

class tbl_relationtype(models.Model):
    relation_type=models.CharField(max_length=50)

class tbl_scholarshiptype(models.Model):
    scholarship_type=models.CharField(max_length=50)

class tbl_electionposition(models.Model):
    election_position=models.CharField(max_length=50)

class tbl_financehead(models.Model):
    financehead_name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    fdate=models.DateField()
    sdate=models.DateField()


class tbl_scholarshipname(models.Model):
    scholarship_name=models.CharField(max_length=50)
    scholarship_details=models.CharField(max_length=50)
    proof_name=models.ForeignKey(tbl_proof,on_delete=models.CASCADE)
    scholarship_type=models.ForeignKey(tbl_scholarshiptype,on_delete=models.CASCADE)


class tbl_electiondeclaration(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=50)
    nodate=models.DateField()
    vedate=models.DateField()
    eldate=models.DateField()
    redate=models.DateField()
    podate=models.DateField(auto_now_add=True)


class tbl_events(models.Model):
    name=models.CharField(max_length=50)
    details=models.CharField(max_length=100)
    date=models.DateField()

    

