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

def viewchittyfunding(request):
    mdata=tbl_memberadding.objects.all()
    rdata=tbl_relatives.objects.all()
    mappdata=tbl_chittyfunding.objects.filter(member_name__in=mdata)
    rappdata=tbl_chittyfunding.objects.filter(relative_name__in=rdata)
    return render(request,"FinanceHead/ViewChittyFunding.html",{'data':mappdata,'data1':rappdata})

def loancalender(request,lid):
    if 'fhid' in request.session:
        data=tbl_loancalender.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            loanname=tbl_addloanname.objects.get(id=lid)
            tbl_loancalender.objects.create(amount=request.POST.get('txt_rs'),
            no_installment=request.POST.get('txt_in'),
            startdate=request.POST.get('sdate'),
            enddate=request.POST.get('edate'),head=headdata,loan_name=loanname)
            return redirect("FinanceHead:addloan")
        else:

            return render(request,"FinanceHead/loancalender.html",{'data':data})
    else:
        return redirect("Guest:Login")   


def viewloanrepay(request,lid):
    if 'fhid' in request.session:
        loanapp=tbl_loanapply.objects.get(id=lid)
        datacount=tbl_repaymentloan.objects.filter(loanapply=loanapp).count()
        loannames=loanapp.loan_name.id
        loancalender=tbl_loancalender.objects.get(loan_name=loannames)
        installments=int(loancalender.no_installment)
        array=[i for i in range(1,installments+1)]
        return render(request,"FinanceHead/ViewRepayment.html",{'data':datacount,'paynumber':loancalender,'array':array})
    else:
        return redirect("Guest:Login")

def chittycalender(request,cid):
    if 'fhid' in request.session:
        data=tbl_chittycalender.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
            chittyname=tbl_chitty.objects.get(id=cid)
            tbl_chittycalender.objects.create(amount=request.POST.get('txt_rs'),
            no_installment=request.POST.get('txt_in'),
            startdate=request.POST.get('sdate'),
            enddate=request.POST.get('edate'),head=headdata,chitty_name=chittyname)
            return redirect("FinanceHead:chitty")
        else:
            return render(request,"FinanceHead/chittycalender.html",{'data':data})
    else:
        return redirect("Guest:Login")

def deleteloancalender(request,lid):
    tbl_loancalender.objects.get(id=lid).delete()
    return redirect("FinanceHead:loancalender")

def deletechittycalender(request,cid):
    tbl_chittycalender.objects.get(id=cid).delete()
    return redirect("FinanceHead:chittycalender")


def viewchittypay(request,cid):
    if 'fhid' in request.session:
        chittyapp=tbl_chittyjoin.objects.get(id=cid)
        datacount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        chittyname=chittyapp.chittydata.id
        chittycalender=tbl_chittycalender.objects.get(chitty_name=chittyname)
        installments=int(chittycalender.no_installment)
        array=[i for i in range(1,installments+1)]
        return render(request,"FinanceHead/viewchittypayment.html",{'data':datacount,'paynumber':chittycalender,'array':array})
    else:
        return redirect("Guest:Login")

def weeklycollection(request):
    if 'fhid' in request.session:
        data=tbl_weeklycollection.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
       
            tbl_weeklycollection.objects.create(amount=request.POST.get('txt_amount'),
            head=headdata)
            return redirect("FinanceHead:weeklycollection")
        else:
            return render(request,"FinanceHead/weeklycollection.html",{'data':data})
    else:
        return redirect("Guest:Login")


def monthlycollection(request):
    if 'fhid' in request.session:
        data=tbl_monthlycollection.objects.all()
        if request.method=="POST":
            headdata=tbl_financehead.objects.get(id=request.session["fhid"])
       
            tbl_monthlycollection.objects.create(amount=request.POST.get('txt_amount'),
            head=headdata)
            return redirect("FinanceHead:monthlycollection")
        else:
            return render(request,"FinanceHead/monthlycollection.html",{'data':data})
    else:
        return redirect("Guest:Login")

def deletemonthlycollection(request,mid):
    tbl_monthlycollection.objects.get(id=mid).delete()
    return redirect("FinanceHead:monthlycollection")

def deleteweeklycollection(request,wid):
    tbl_weeklycollection.objects.get(id=wid).delete()
    return redirect("FinanceHead:weeklycollection")


def viewweeklycollectionpayment(request):
    if 'fhid' in request.session:
        rdata=tbl_relatives.objects.all()
        data=tbl_weeklycollectionpayment.objects.all()
    #datacount=tbl_weeklycollectionpayment.objects.filter(relative_name=rdata).count
    #dcount=tbl_weeklycollectionpayment.objects.filter(weeklycollection_id=datacount)
    
        return render(request,"FinanceHead/viewweeklycollectionpayment.html",{'data':data})
    else:
        return redirect("Guest:Login")

def viewmonthlycollectionpayment(request):
    if 'fhid' in request.session:
    #rdata=tbl_relatives.objects.all()
        data=tbl_monthlycollectionpayment.objects.all()
    #datacount=tbl_weeklycollectionpayment.objects.filter(relative_name=rdata).count
    #dcount=tbl_weeklycollectionpayment.objects.filter(weeklycollection_id=datacount)
    
        return render(request,"FinanceHead/viewmonthlycollectionpayment.html",{'data':data})
    else:
        return redirect("Guest:Login")
