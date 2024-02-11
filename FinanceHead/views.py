from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Member.models import *

# Create your views here.



def homepage(request):
    udata=tbl_financehead.objects.get(id=request.session['fid'])
    return render(request,"FinanceHead/Homepage.html",{'udata':udata})

def myprofile(request):
    udata=tbl_financehead.objects.get(id=request.session['fid'])
    return render(request,"FinanceHead/MyProfile.html",{'udata':udata})

def changep(request):
    udata=tbl_financehead.objects.get(id=request.session['fid'])
    if request.method=="POST":
        pwd=udata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                udata.password=pass1
                udata.save()
                return redirect("FinanceHead:ChangePassword")
            else:
                msg="password  does not match"
                return render(request,"FinanceHead/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render(request,"FinanceHead/ChangePassword.html",{'msg':msg})
    else:
        return render(request,"FinanceHead/ChangePassword.html")


def chitty(request):
    fheadid=tbl_financehead.objects.get(id=request.session['fid'])
    disdata=tbl_scheme.objects.all()
    subdata=tbl_chitty.objects.filter(head=fheadid)
    if request.method=="POST":
        cat = tbl_scheme.objects.get(id=request.POST.get("select_sch"))
       
        
        tbl_chitty.objects.create(
            chitty_name=request.POST.get("txt_name1"),
            chitty_details=request.POST.get("txt_name2"),
            scheme=cat,
            head=fheadid,
            )
        
        return render(request,"FinanceHead/Chitty.html",{'disdata':disdata,'subcat':subdata})
    else:
        return render(request,"FinanceHead/Chitty.html",{'disdata':disdata,'subcat':subdata})

def loan(request):
    fheadid=tbl_financehead.objects.get(id=request.session['fid'])
    disdata=tbl_loan.objects.all()
    subdata=tbl_addloanname.objects.filter(head=fheadid)
    if request.method=="POST":
        cat = tbl_loan.objects.get(id=request.POST.get("select_sch"))
       
        
        tbl_addloanname.objects.create(
            loan_name=request.POST.get("txt_name1"),
            loan_details=request.POST.get("txt_name2"),
            loan_type=cat,
            head=fheadid,
            )
        
        return render(request,"FinanceHead/Loan.html",{'disdata':disdata,'subcat':subdata})
    else:
        return render(request,"FinanceHead/Loan.html",{'disdata':disdata,'subcat':subdata})

def DeleteChitty(request,did):
    tbl_chitty.objects.get(id=did).delete()
    return redirect("FinanceHead:Chitty")

def DeleteLoan(request,did):
    tbl_addloanname.objects.get(id=did).delete()
    return redirect("FinanceHead:Loan")



def viewchittyapply(request):
    memdata=tbl_chittyjoin.objects.all()
    return render(request,"FinanceHead/ViewChittyApply.html",{'memdata':memdata})

def viewloanapply(request):
    memdata=tbl_loanapply.objects.all()
    return render(request,"FinanceHead/ViewLoanApply.html",{'memdata':memdata})

def acceptchitty(request,did):
    data=tbl_chittyjoin.objects.get(id=did)
    data.status=1
    data.save()
    return redirect("FinanceHead:ViewChittyApply")


def rejectchitty(request,did):
    data=tbl_chittyjoin.objects.get(id=did)
    data.status=2
    data.save()
    return redirect("FinanceHead:ViewChittyApply")


def acceptloan(request,did):
    data=tbl_loanapply.objects.get(id=did)
    data.status=1
    data.save()
    return redirect("FinanceHead:ViewLoanApply")


def rejectloan(request,did):
    data=tbl_loanapply.objects.get(id=did)
    data.status=2
    data.save()
    return redirect("FinanceHead:ViewLoanApply")