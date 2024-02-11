from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import *
from Member.models import *

# Create your views here.

def pla(request):
    disdata=tbl_place.objects.all()
    if request.method=="POST":
        tbl_place.objects.create(place_name=request.POST.get("txt_place"))
        return render(request,"Admin/place.html",{'place':disdata})
    else:
        return render(request,"Admin/Place.html",{'place':disdata})

def DeletePlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")

def EditPlace(request,eid):
    dis=tbl_place.objects.get(id=eid)
    disdata=tbl_place.objects.all()
    if request.method=="POST":
        dis.place_name=request.POST.get("txt_place")
        dis.save()
        return redirect("Admin:Place")
    else:
        return render(request,"Admin/Place.html",{'edis':dis,'place':disdata})


def loca(request):
    disdata=tbl_place.objects.all()
    subdata=tbl_location.objects.all()
    if request.method=="POST":
        cat = tbl_place.objects.get(id=request.POST.get("select_pla"))
        
        tbl_location.objects.create(
            location_name=request.POST.get("txt_name1"),
            place=cat
            )
        
        return render(request,"Admin/Location.html",{'disdata':disdata,'subcat':subdata})
    else:
        return render(request,"Admin/Location.html",{'disdata':disdata,'subcat':subdata})

def DeleteLocation(request,sid):
    tbl_location.objects.get(id=sid).delete()
    return redirect("Admin:Location")

def loan(request):
    disdata=tbl_loan.objects.all()
    if request.method=="POST":
        tbl_loan.objects.create(loan_name=request.POST.get("txt_loan"))
        return render(request,"Admin/Loan.html",{'loan':disdata})
    else:
        return render(request,"Admin/Loan.html",{'loan':disdata})

def DeleteLoan(request,did):
    tbl_loan.objects.get(id=did).delete()
    return redirect("Admin:Loan")

def EditLoan(request,eid):
    dis=tbl_loan.objects.get(id=eid)
    disdata=tbl_loan.objects.all()
    if request.method=="POST":
        dis.loan_name=request.POST.get("txt_loan")
        dis.save()
        return redirect("Admin:Loan")
    else:
        return render(request,"Admin/Loan.html",{'edis':dis,'loan':disdata})

def proof(request):
    disdata=tbl_proof.objects.all()
    if request.method=="POST":
        tbl_proof.objects.create(proof_name=request.POST.get("txt_proof"))
        return render(request,"Admin/Proof.html",{'proof':disdata})
    else:
        return render(request,"Admin/Proof.html",{'proof':disdata})

def DeleteProof(request,did):
    tbl_proof.objects.get(id=did).delete()
    return redirect("Admin:Proof")

def EditProof(request,eid):
    dis=tbl_proof.objects.get(id=eid)
    disdata=tbl_proof.objects.all()
    if request.method=="POST":
        dis.proof_name=request.POST.get("txt_proof")
        dis.save()
        return redirect("Admin:Proof")
    else:
        return render(request,"Admin/Proof.html",{'edis':dis,'proof':disdata})

def scheme(request):
    disdata=tbl_scheme.objects.all()
    if request.method=="POST":
        tbl_scheme.objects.create(scheme_name=request.POST.get("txt_scheme"))
        return render(request,"Admin/Scheme.html",{'scheme':disdata})
    else:
        return render(request,"Admin/Scheme.html",{'scheme':disdata})

def DeleteScheme(request,did):
    tbl_scheme.objects.get(id=did).delete()
    return redirect("Admin:Scheme")

def EditScheme(request,eid):
    dis=tbl_scheme.objects.get(id=eid)
    disdata=tbl_scheme.objects.all()
    if request.method=="POST":
        dis.scheme_name=request.POST.get("txt_scheme")
        dis.save()
        return redirect("Admin:Scheme")
    else:
        return render(request,"Admin/Scheme.html",{'edis':dis,'scheme':disdata})

def relationtype(request):
    disdata=tbl_relationtype.objects.all()
    if request.method=="POST":
        tbl_relationtype.objects.create(relation_type=request.POST.get("txt_relation"))
        return render(request,"Admin/Relationtype.html",{'relationtype':disdata})
    else:
        return render(request,"Admin/Relationtype.html",{'relationtype':disdata})

def DeleteRelation(request,did):
    tbl_relationtype.objects.get(id=did).delete()
    return redirect("Admin:Relationtype")

def EditRelation(request,eid):
    dis=tbl_relationtype.objects.get(id=eid)
    disdata=tbl_relationtype.objects.all()
    if request.method=="POST":
        dis.relation_type=request.POST.get("txt_relation")
        dis.save()
        return redirect("Admin:Relationtype")
    else:
        return render(request,"Admin/Relationtype.html",{'edis':dis,'relationtype':disdata})

def scholarshiptype(request):
    disdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        tbl_scholarshiptype.objects.create(scholarship_type=request.POST.get("txt_scholar"))
        return render(request,"Admin/Scholarshiptype.html",{'scholarshiptype':disdata})
    else:
        return render(request,"Admin/Scholarshiptype.html",{'scholarshiptype':disdata})

def DeleteScholarship(request,did):
    tbl_scholarshiptype.objects.get(id=did).delete()
    return redirect("Admin:Scholarshiptype")

def EditScholarship(request,eid):
    dis=tbl_scholarshiptype.objects.get(id=eid)
    disdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        dis.scholarship_type=request.POST.get("txt_scholar")
        dis.save()
        return redirect("Admin:Scholarshiptype")
    else:
        return render(request,"Admin/Scholarshiptype.html",{'edis':dis,'scholarshiptype':disdata})

def electionposition(request):
    disdata=tbl_electionposition.objects.all()
    if request.method=="POST":
        tbl_electionposition.objects.create(election_position=request.POST.get("txt_election"))
        return render(request,"Admin/Electionposition.html",{'electionposition':disdata})
    else:
        return render(request,"Admin/Electionposition.html",{'electionposition':disdata})

def DeleteElection(request,did):
    tbl_electionposition.objects.get(id=did).delete()
    return redirect("Admin:Electionposition")

def EditElection(request,eid):
    dis=tbl_electionposition.objects.get(id=eid)
    disdata=tbl_electionposition.objects.all()
    if request.method=="POST":
        dis.election_position=request.POST.get("txt_election")
        dis.save()
        return redirect("Admin:Electionposition")
    else:
        return render(request,"Admin/Electionposition.html",{'edis':dis,'electionposition':disdata})

def financehead(request):
    disdata=tbl_financehead.objects.all()
    if request.method=="POST":
        tbl_financehead.objects.create(financehead_name=request.POST.get("txt_name"),user_name=request.POST.get("txt_user"),password=request.POST.get("txt_password"),fdate=request.POST.get("txt_date1"),sdate=request.POST.get("txt_date2"))
        return render(request,"Admin/FinanceHeadRegistration.html",{'financehead':disdata})
    else:
        return render(request,"Admin/FinanceHeadRegistration.html",{'financehead':disdata})

def DeleteFinance(request,did):
    tbl_financehead.objects.get(id=did).delete()
    return redirect("Admin:FinanceHeadRegistration")


def mreg(request):
    disdata=tbl_place.objects.all()
    memdata=tbl_memberadding.objects.all()
    if request.method=="POST" and request.FILES:
        locationid=tbl_location.objects.get(id=request.POST.get("select_loca"))
        tbl_memberadding.objects.create(member_name=request.POST.get("txt_name"),contact = request.POST.get("txt_con"),
        email = request.POST.get("txt_email"),
        gender = request.POST.get("btn_gen"),
        address = request.POST.get("txt_add"),
        location = locationid,
        photo = request.FILES.get("txt_pic"),
        password = request.POST.get("txt_pass"),age=request.POST.get('txt_age'))
        return render(request,"Admin/MemberRegistration.html",{'memdata':memdata})
    else:
        return render(request,"Admin/MemberRegistration.html",{'memdata':memdata}) 

def ajax_locatiom(request):
   plaob=tbl_place.objects.get(id=request.GET.get('Pla'))
   location=tbl_location.objects.filter(place=plaob)
   return render(request,"Guest/AjaxLocation.html",{'loc':location})

def DeleteMember(request,did):
    tbl_memberadding.objects.get(id=did).delete()
    return redirect("Admin:MemberRegistration")

def scholar(request):
    disdata=tbl_scholarshipname.objects.all()
    catdata=tbl_proof.objects.all()
    misdata=tbl_scholarshiptype.objects.all()
    if request.method=="POST":
        cat = tbl_proof.objects.get(id=request.POST.get("select_pro"))
        mat = tbl_scholarshiptype.objects.get(id=request.POST.get("select_sch"))
        tbl_scholarshipname.objects.create(scholarship_name=request.POST.get("txt_name1"),scholarship_details=request.POST.get("txt_name2"),
        proof_name=cat,
        scholarship_type=mat)
        return render(request,"Admin/Scholarship.html",{'disdata':disdata,'misdata':misdata,'catdata':catdata})
    else:

        return render(request,"Admin/Scholarship.html",{'disdata':disdata,'misdata':misdata,'catdata':catdata})


def Deletesc(request,did):
    tbl_scholarshipname.objects.get(id=did).delete()
    return redirect("Admin:Scholarship")
 

def electiondec(request):
    disdata=tbl_electiondeclaration.objects.all()
    if request.method=="POST":
        tbl_electiondeclaration.objects.create(title=request.POST.get("txt_title"),details=request.POST.get("txt_details"),
        nodate=request.POST.get("txt_nomdate"),vedate=request.POST.get("txt_vedate"),
        eldate=request.POST.get("txt_eldate"),redate=request.POST.get("txt_redate"),
        podate=request.POST.get("txt_podate"))
        return render(request,"Admin/ElectionDeclaration.html",{'disdata':disdata})
        
    else:
        return render(request,"Admin/ElectionDeclaration.html",{'disdata':disdata})

def Deleteec(request,did):
    tbl_electiondeclaration.objects.get(id=did).delete()
    return redirect("Admin:ElectionDeclaration")


def viewscholarapply(request):
    memdata=tbl_scholarshipapply.objects.all()
    return render(request,"Admin/ViewScholarApply.html",{'memdata':memdata})

def acceptscholar(request,did):
    data=tbl_scholarshipapply.objects.get(id=did)
    data.status=1
    data.save()
    return redirect("Admin:ViewScholarApply")


def rejectscholar(request,did):
    data=tbl_scholarshipapply.objects.get(id=did)
    data.status=2
    data.save()
    return redirect("Admin:ViewScholarApply")


def viewelectionapply(request):
    memdata=tbl_electionapply.objects.all()
    return render(request,"Admin/ViewElectionapply.html",{'memdata':memdata})


def acceptelection(request,did):
    data=tbl_electionapply.objects.get(id=did)
    data.status=1
    data.save()
    return redirect("Admin:ViewElectionapply")


def rejectelection(request,did):
    data=tbl_electionapply.objects.get(id=did)
    data.status=2
    data.save()
    return redirect("Admin:ViewElectionapply")


