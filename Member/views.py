from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from Guest.models import *
from FinanceHead.models import *
from datetime import date

# Create your views here.

def homepage(request):
    if 'mid' in request.session:
        udata=tbl_memberadding.objects.get(id=request.session['mid'])
        return render(request,"Member/Homepage.html",{'data1':udata})
    elif 'reid' in request.session:
        udata=tbl_relatives.objects.get(id=request.session['reid'])
        return render(request,"Member/Homepage.html",{'data':udata})
    else:
        return redirect("Guest:Login")

def profile(request):
    if 'mid' in request.session:
        udata=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/MyProfile.html",{'mdata':udata})
    elif 'reid' in request.session:
        udata=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/MyProfile.html",{'udata':udata})
    else:
        return redirect("Guest:Login")


def editprofile(request):
    if 'mid' in request.session:
        udata=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST":
            udata.member_name=request.POST.get('txt_name')
            udata.age=request.POST.get('txt_age')
            udata.contact=request.POST.get('contact')
            udata.email=request.POST.get('email')
            udata.address=request.POST.get('address')
            udata.save()
            return redirect("Member:MyProfile")
        else:
            return render(request,"Member/EditProfile.html",{'mdata':udata})

    elif 'reid' in request.session:
        udata=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST":
            udata.relative_name=request.POST.get('txt_name')
            udata.age=request.POST.get('txt_age')
            udata.contact=request.POST.get('contact')
            udata.email=request.POST.get('email')
            #udata.address=request.POST.get('address')
            udata.save()
            return redirect("Member:MyProfile")
        else:
            return render(request,"Member/EditProfile.html",{'udata':udata})
    else:
        return render(request,"Member/Homepage.html")

def changep(request):
    udata=tbl_memberadding.objects.get(id=request.session['mid'])
    if request.method=="POST":
        pwd=udata.password
        current_pwd=request.POST.get("txt_pass")
        if pwd == current_pwd:
            pass1 = request.POST.get("txt_new")
            pass2 = request.POST.get("txt_cpass")
            if pass1==pass2 :
                udata.password=pass1
                udata.save()
                return redirect("Member:ChangePassword")
            else:
                msg="password  does not match"
                return render(request,"Member/ChangePassword.html",{'msg':msg})
        else:
            msg="incorrect password"
            return render(request,"Member/ChangePassword.html",{'msg':msg})
    else:
      
        return render(request,"Member/ChangePassword.html")

def vchitty(request):
    disdata=tbl_scheme.objects.all()
    subcat=tbl_chitty.objects.all()
    if request.method=="POST":
        return render(request,"Member/ViewChitty.html",{'disdata':disdata,'subcat':subcat})
    else:
        return render(request,"Member/ViewChitty.html",{'disdata':disdata,'subcat':subcat})


def vloan(request):
    disdata=tbl_loan.objects.all()
    subcat=tbl_addloanname.objects.all()
    if request.method=="POST":
        return render(request,"Member/ViewLoan.html",{'disdata':disdata,'subcat':subcat})
    else:
        return render(request,"Member/ViewLoan.html",{'disdata':disdata,'subcat':subcat})


def vscholarship(request):
    disdata=tbl_scholarshiptype.objects.all()
    subcat=tbl_scholarshipname.objects.all()
    if request.method=="POST":
        return render(request,"Member/ViewScholarship.html",{'disdata':disdata,'subcat':subcat})
    else:
        return render(request,"Member/ViewScholarship.html",{'disdata':disdata,'subcat':subcat})

def ajaxchitty(request):
    schemedata=tbl_scheme.objects.get(id=request.GET.get('sch'))
    chittydata=tbl_chitty.objects.filter(scheme=schemedata)
    return render(request,"Member/ajaxchitty.html",{'subcat':chittydata})

def ajaxloan(request):
    loandata=tbl_loan.objects.get(id=request.GET.get('sch'))
    loannamedata=tbl_addloanname.objects.filter(loan_type=loandata)
    return render(request,"Member/ajaxloan.html",{'subcat':loannamedata})

def ajaxscholar(request):
    scholardata=tbl_scholarshiptype.objects.get(id=request.GET.get('sch'))
    scholarnamedata=tbl_scholarshipname.objects.filter(scholarship_type=scholardata)
    return render(request,"Member/ajaxscholar.html",{'subcat':scholarnamedata})



def relatives(request):
    relationtype=tbl_relationtype.objects.all()
    memid=tbl_memberadding.objects.get(id=request.session['mid'])
    datas=tbl_relatives.objects.filter(member_name=memid)
    if request.method=="POST" and request.FILES:
        relation=tbl_relationtype.objects.get(id=request.POST.get("relation"))
        tbl_relatives.objects.create(relative_name=request.POST.get("txt_name"),contact = request.POST.get("txt_contact"),
        email = request.POST.get("txt_email"),
        gender = request.POST.get("gender"),
        address = request.POST.get("txt_address"),
        password=request.POST.get("txt_name"),
        photo = request.FILES.get("photo"),
        age=request.POST.get('txt_age'),
        refer_id=request.POST.get('selr'),
        relation_type=relation,
        member_name=memid)

        return render(request,"Member/Relatives.html",{'relationtype':relationtype,'datas':datas})
    else:
        return render(request,"Member/Relatives.html",{'relationtype':relationtype,'datas':datas})

def Ajaxrelation(request):
    memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
    relationdata=tbl_relationtype.objects.get(id=request.GET.get('did'))
    passdata=str(relationdata.relation_type)
    print(passdata)
    if passdata=="Daughter-in-law" or passdata=="Son-in-law" or passdata=="Granddaughter" or passdata=="Grandson":
        print("Hai")
        datacount=tbl_relatives.objects.filter(member_name=memberdata).count()
        print(datacount)
        data=tbl_relatives.objects.filter(member_name=memberdata)
        return render(request,"Member/ajaxrelation.html",{'rdata':data,'content':passdata})
    else:
        return render(request,"Member/ajaxrelation.html",{'adata':memberdata,'content':passdata})





def veledec(request):
    curdate=date.today()
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        sdata=tbl_electiondeclaration.objects.all()
        
        return render(request,"Member/ViewElectiondec.html",{'datas':sdata,'data1':data,'curdate':curdate})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        sdata=tbl_electiondeclaration.objects.filter()
        return render(request,"Member/ViewElectiondec.html",{'datas':sdata,'data':data,'curdate':curdate})
    else:
        return redirect("Member:Homepage")



def Deleterelative(request,did):
    tbl_relatives.objects.get(id=did).delete()
    return redirect("Member:Relative")

def logout(request):
    if 'mid' in request.session and 'reid' in request.session:
        del request.session["mid"]
        del request.session["reid"]
        return redirect("Guest:Login")
    elif 'mid' in request.session:
        del request.session["mid"]
        return redirect("Guest:Login")
    else:
        del request.session["reid"]
        return redirect("Guest:Login")


def schapply(request,schid):

    schdata=tbl_scholarshipname.objects.get(id=schid)
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        if request.method=="POST" and request.FILES:
            tbl_scholarshipapply.objects.create(member_name=data,scholarship_name=schdata,
         
            document=request.FILES.get('filedoc'))

            msg="Scholarship Applied"
            return render(request,"Member/ScholarshipApply.html",{'data':data,'schdata':schdata,'msg':msg})
        else:
           # return render(request,"Member/scholarshipapply.html")
            return render(request,"Member/ScholarshipApply.html",{'data':data,'schdata':schdata})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        if request.method=="POST" and request.FILES:
            tbl_scholarshipapply.objects.create(relative_name=data,scholarship_name=schdata,
            document=request.FILES.get('filedoc'))
            return render(request,"Member/ScholarshipApply.html",{'data1':data,'schdata':schdata})
         
        else:
            #return render(request,"Member/scholarshipapply.html")
            return render(request,"Member/ScholarshipApply.html",{'data1':data,'schdata':schdata})
    else:
        return render(request,"Member/ScholarshipApply.html",{'data1':data,'schdata':schdata})
      

def chittyapply(request,chid):
    prooftype=tbl_proof.objects.all() 
    chittyjoindata=tbl_chittyjoin.objects.all()
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        chittydata=tbl_chitty.objects.get(id=chid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            tbl_chittyjoin.objects.create(member_name=memberdata,chittydata=chittydata,
            proof_name=ptype,document=request.FILES.get('proof'))

            msg="Chitty Applied!!"
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata,'msg':msg})
        else:
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        chittydata=tbl_chitty.objects.get(id=chid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            tbl_chittyjoin.objects.create(relative_name=rdata,chittydata=chittydata,
            proof_name=ptype,document=request.FILES.get('proof'))
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})
        else:
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})
    else:
        return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})


def loanapply(request,lnid):
        prooftype=tbl_proof.objects.all() 
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loan=tbl_addloanname.objects.get(id=lnid)
        if request.method=="POST":
           
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            tbl_loanapply.objects.create(member_name=memberdata,loan_name=loan,
            proof_name=ptype,document=request.FILES.get('proof'))
             
            msg="Loan Applied!!"
            return render(request,"Member/LoanApply.html",{'cdata':loan,'ptype':prooftype,'data1':memberdata,'msg':msg})
        else:
            return render(request,"Member/LoanApply.html",{'cdata':loan,'ptype':prooftype,'data1':memberdata})

def viewloanapply(request):
    memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
    loan=tbl_loanapply.objects.filter(member_name=memberdata)
    return render(request,"Member/ViewLoanApply.html",{'cdata':loan,'memberdata':memberdata})


def viewscholarshipapply(request):
    
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_scholarshipapply.objects.filter(member_name=mdata)
        return render(request,"Member/ViewScholarshipApply.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_scholarshipapply.objects.filter(relative_name=mdata)
        return render(request,"Member/ViewScholarshipApply.html",{'datas':data,'data':mdata})
    else:
        return render(request,"Member/ViewScholarshipApply.html",{'datas':data})

def viewchittyapply(request):
   
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_chittyjoin.objects.filter(member_name=mdata)
        return render(request,"Member/ViewChittyApply.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_chittyjoin.objects.filter(relative_name=mdata)
        return render(request,"Member/ViewChittyApply.html",{'datas':data,'data':mdata})
    else:
        return render(request,"Member/ViewchittyApply.html",{'datas':data})


def scholarshipstatus(request):
    if 'mid' in request.session:
        data=tbl_memberadding.objects.get(id=request.session["mid"])
        sdata=tbl_scholarshipapply.objects.filter(member_name=data)
        return render(request,"Member/ScholarshipStatus.html",{'datas':sdata,'data1':data})
    elif 'reid' in request.session:
        data=tbl_relatives.objects.get(id=request.session["reid"])
        sdata=tbl_scholarshipapply.objects.filter(relative_name=data)
        return render(request,"Member/ScholarshipStatus.html",{'datas':sdata,'data':data})
    else:
        return redirect("Member:Homepage")



def chittystatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        mdata=tbl_chittyjoin.objects.filter(member_name=memberdata)
        return render(request,"Member/ChittyStatus.html",{'chittystatusview':mdata,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_chittyjoin.objects.filter(relative_name=rdata)
        return render(request,"Member/ChittyStatus.html",{'chittystatusview1':data,'data':rdata})
    else:
        return redirect("Member:Homepage")

def loanstatusview(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loandata=tbl_loanapply.objects.filter(member_name=memberdata)
        
        return render(request,"Member/LoanStatus.html",{'loanstatusview':loandata,'data1':memberdata})
    else:
        return redirect("Guest:login")


def applyelec(request,did):
    return redirect("Member:ElectionApply")



def electionapply(request,lnid):
        position=tbl_electionposition.objects.all() 
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        elec=tbl_electiondeclaration.objects.get(id=lnid)
        if request.method=="POST":
            ptype=tbl_electionposition.objects.get(id=request.POST.get('ptype'))
            tbl_electionapply.objects.create(election_name=elec,member_name=memberdata,
            election_position=ptype)
            return render(request,"Member/ElectionApply.html",{'cdata':elec,'ptype':position ,'data1':memberdata})
        else:
            return render(request,"Member/ElectionApply.html",{'cdata':elec,'ptype':position,'data1':memberdata})



def viewelectionapply(request):
    memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
    elec=tbl_electionapply.objects.filter(member_name=memberdata)
    
    return render(request,"Member/ViewElectionapply.html",{'cdata':elec,'memberdata':memberdata})


def vote(request,did):
    curdate=date.today()
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        electiondata=tbl_electionapply.objects.filter(member_name=memberdata)
        return render(request,"Member/ViewElectionapply.html",{'curdate':curdate,'member':memberdata,'eletiondata':electiondata})
    else:
        return render(request,"Member/ViewElectionapply.html",{'curdate':curdate,'member':memberdata,'eletiondata':electiondata})


def viewcandidates(request,elid):
    edata=tbl_electiondeclaration.objects.get(id=elid)
    data=tbl_electionapply.objects.filter(status=1,election_name=edata)
    return render(request,"Member/ViewCandidates.html",{'data':data})



def votenow(request,vid):
    edata=tbl_electionapply.objects.get(id=vid)
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        tbl_voting.objects.create(electionapply=edata,member=memberdata)
        return redirect("Member:ViewElectiondec")
    elif 'reid' in request.session:
        reldata=tbl_relatives.objects.get(id=request.session["reid"])
        tbl_voting.objects.create(electionapply=edata,relative=reldata)
        return redirect("Member:ViewElectiondec")
    else:
        return redirect("Member:ViewElectiondec")




    
def voting(request,vid):
    edata=tbl_electiondeclaration.objects.get(id=vid)# To Retrive data Which Election is Choosed
    if 'mid' in request.session: # check if member is logined
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        voteddatacount=tbl_voting.objects.filter(member=mdata).count() 
        j=0 #initalize j=0 for indexing for arrays defined below
        parray=[0 for i in range(1,voteddatacount+1)] # Decalare array for store election Application id From voted data of logined member
        parrays=[0 for i in range(1,voteddatacount+1)] # Decalare array for store election Postion id From voted data of logined member
        voteddata=tbl_voting.objects.filter(member=mdata) # Data of Voted by member
        for i in voteddata: # for loop for store postion and application id from voted data
            parray[j]=i.electionapply.id #store application id to parray
            parrays[j]=i.electionapply.election_position.id #store position to parray
            j=j+1 #increment index of array

        votedata=tbl_electionapply.objects.filter(status=1,election_name=edata) #select data from election apply form status=1 and election we choosed
        return render(request,"Member/Voting.html",{'data':votedata,'voted':parray,'p':parrays,'mdata':mdata})
       

def results(request):
    pid=2
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.filter().last()
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray.append(ecount)
    large=max(parray)
    datas=zip(pdata,parray)

    pid=1
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.filter().last()
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray1=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray1.append(ecount)
    large1=max(parray1)
    datas1=zip(pdata,parray1)
    

    pid=3
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.filter().last()
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray2=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray2.append(ecount)
    large2=0
    if len(parray2)>0:
        large2=max(parray2)
    datas2=zip(pdata,parray2)
    
    return render(request,"Member/ViewResult.html",{'datas':datas,'datas1':datas1,'datas2':datas2,'win1':large,'win2':large1,'win3':large2})


def funding(request,vid):
    prooftype=tbl_proof.objects.all() 
    if 'mid' in request.session :
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        chittydata=tbl_chitty.objects.get(id=vid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('select_proof'))
            tbl_chittyfunding.objects.create(member_name=memberdata,chitty_name=chittydata,
            proof_name=ptype,document=request.FILES.get('doc'))
            return render(request,"Member/ChittyFunding.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata})
        else:
            return render(request,"Member/ChittyFunding.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        chittydata=tbl_chitty.objects.get(id=vid)
        if request.method=="POST":
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            tbl_chittyjoin.objects.create(relative_name=rdata,chitty_name=chittydata,
            proof_name=ptype,document=request.FILES.get('doc'))
            return render(request,"Member/ChittyFunding.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})
        else:
            return render(request,"Member/ChittyFunding.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})
    else:
        return render(request,"Member/ChittyFunding.html",{'cdata':chittydata,'ptype':prooftype,'data':rdata})


def viewchittyfunding(request):
   
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_chittyfunding.objects.filter(member_name=mdata)
        return render(request,"Member/ViewChittyFunding.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_chittyjoin.objects.filter(relative_name=mdata)
        return render(request,"Member/ViewChittyFunding.html",{'datas':data,'data':mdata})
    else:
        return render(request,"Member/ViewChittyFunding.html",{'datas':data})



def add_months_with_year_change(start_date, n_months):
    result_dates = []
    current_date = start_date

    for _ in range(n_months):
        # Add one month to the current date using relativedelta
        current_date += relativedelta(months=1)

        # Append the current date to the array
        result_dates.append(current_date)
    #print(result_dates)
    return result_dates
# Create your views here.

def add_months(start_date, n):
    month = start_date.month - 1 + n
    year = start_date.year + month // 12
    month = month % 12 + 1
    day = min(start_date.day, (start_date.replace(year=year, month=month + 1, day=1) - timedelta(days=1)).day)
    return start_date.replace(year=year, month=month, day=day)


def loanpay(request,lpid):
    if 'mid' in request.session:
        darray=[]
        cdate=date.today()
        #data=tbl_loancalender.objects.all() 
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        loandata=tbl_addloanname.objects.get(id=lpid)
        payno=tbl_loancalender.objects.get(loan_name=loandata)
        loanapp=tbl_loanapply.objects.get(loan_name=loandata,member_name=memberdata)

        ###########################################################################
        ldate=loanapp.apply_date
        
    
        ###########################################################################
        loanrapycount=tbl_repaymentloan.objects.filter(loanapply=loanapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        # darray=[]
        # j=0
        # darray.append(startdate)
        # ldate=startdate
        # for i in parray:
        #     ldate=str(ldate)
            # print("First Time:") 
            # print(type(ldate))
            # date_object = datetime.strptime(ldate, "%Y-%m-%d")
            # ldate= date_object
            # print("Second Time:") 
            # print(type(ldate))
            # month = date_object.month
            # if i%12==0:
            #     res=i//12
            #     ldate=add_months(ldate,res)
            #     edate=str(ldate)
            #     darray.append(edate)
            # else:
            #     res=i%12
            #     ldate=add_months(ldate,res)
            #     edate=str(ldate)
            #     darray.append(edate)
            # print("Third Time:") 
            # print(type(ldate))
            #if month>=12:
                #pass
                # j=j+1
                # ldate=add_months(ldate,j)
                # print(type(ldate))
            #else:
            #    pass
                # ldate=add_months(ldate,i)
                # print(type(ldate))

            
                # print(emiadte)
        datas=zip(parray,darray)
        return render(request,"Member/loanpay.html",{'paynumber':payno,'array':datas,'paycount':loanrapycount,'cdate':cdate,'data1':memberdata})
    else:
        return redirect("Guest:login")

def repaymentloan(request,lid):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        londata=tbl_addloanname.objects.get(id=lid)
        if request.method=="POST":
            loanappdata=tbl_loanapply.objects.get(member_name=memberdata,loan_name=londata)
            tbl_repaymentloan.objects.create(loanapply=loanappdata,member=memberdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")
    else:
        return redirect("Guest:login")

def chittypay(request,cpid):
    #data=tbl_loancalender.objects.all() 
    darray=[]
    cdate=date.today()
    if 'mid' in request.session:

        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        cdata=tbl_chitty.objects.get(id=cpid)
        payno=tbl_chittycalender.objects.get(chitty_name=cdata)
        chittyapp=tbl_chittyjoin.objects.get(chittydata=cdata,memberdata=mdata)
        chittypaycount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        ldate=chittyapp.apply_date
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        datas=zip(parray,darray)
        return render(request,"Member/chittypay.html",{'paynumber':payno,'array':datas,
        'paycount':chittypaycount,'data1':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        cdata=tbl_chitty.objects.get(id=cpid)
        payno=tbl_chittycalender.objects.get(chitty_name=cdata)
        chittyapp=tbl_chittyjoin.objects.get(chittydata=cdata,relative=rdata)
        chittypaycount=tbl_paymentchitty.objects.filter(chitty_apply=chittyapp).count()
        pay=int(payno.no_installment)
        parray=[i for i  in range(1,pay+1)]
        ldate=chittyapp.apply_date
        startdate=add_months(ldate,1)
        print(startdate)
        startdate=str(startdate)
        date_object = datetime.strptime(startdate, "%Y-%m-%d")
        resultarray=add_months_with_year_change(date_object,pay)
        for dates in resultarray:
            darray.append(dates.strftime("%Y-%m-%d"))
        print(darray)
        datas=zip(parray,darray)
        return render(request,"Member/chittypay.html",{'paynumber':payno,'array':datas,
        'paycount':chittypaycount,'data':rdata})
    else:
        return redirect("Member:Homepage")

def paymentchitty(request,cid):
    if request.method=="POST":
        if 'mid' in request.session:

            mdata=tbl_memberadding.objects.get(id=request.session["mid"])
            cdata=tbl_chitty.objects.get(id=cid)
            chittyapplydata=tbl_chittyjoin.objects.get(memberdata=mdata,chittydata=cdata)
            tbl_paymentchitty.objects.create(chitty_apply=chittyapplydata,memberdata=mdata)
            return redirect("Member:runpayment")
        elif 'reid' in request.session:
            rdata=tbl_relatives.objects.get(id=request.session["reid"])
            cdata=tbl_chitty.objects.get(id=cid)
            chittyapplydata=tbl_chittyjoin.objects.get(relative=rdata,chittydata=cdata)
            tbl_paymentchitty.objects.create(chitty_apply=chittyapplydata,relative=rdata)
            return redirect("Member:runpayment")
        else:
            return redirect("Member:Homepage")
    else:
        return render(request,"Member/DesignPayment.html")


def viewweeklycollection(request):

    if 'reid' in request.session:
        relativedata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_weeklycollection.objects.all().last()
        cpayment=tbl_weeklycollectionpayment.objects.filter(relative=relativedata,
        weeklycollection_id=data).count()
        warray=[i for i  in range(1,49)]
        data=tbl_weeklycollection.objects.all().last()
        return render(request,"Member/viewweeklycollection.html",{'datas':data,'array':warray,
        'weekcount':cpayment,'data':relativedata})
    elif 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_weeklycollection.objects.all().last()
        cpayment=tbl_weeklycollectionpayment.objects.filter(member=memberdata,
        weeklycollection_id=data).count()
        warray=[i for i  in range(1,49)]
        data=tbl_weeklycollection.objects.all().last()
        return render(request,"Member/viewweeklycollection.html",{'datas':data,'array':warray,
        'weekcount':cpayment,'data1':memberdata})
    else:
        return redirect("Guest:Login")
        
def viewmonthlycollection(request):
    if 'mid' in request.session:
        memberdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_monthlycollection.objects.all().last()
        cpayment=tbl_monthlycollectionpayment.objects.filter(member=memberdata,monthlycollection_id=data).count()
        marray=[i for i  in range(1,13)] 
        return render(request,"Member/viewmonthlycollection.html",{'datas':data,'array':marray,
        'monthcount':cpayment,'data1':memberdata})
    else:
        return redirect("Guest:Login")
    

# def designpayment(request):
#     return render(request,"Member/DesignPayment.html")

def paysucessful(request):
    if 'mid' in request.session:
        return render(request,"Member/paysucessful.html")
    elif 'reid' in request.session:
        return render(request,"Member/paysucessful.html")
    else:
       return redirect("Guest:Login")
    #return render(request,"Member/paysucessful.html")

def runpayment(request):
    if 'mid' in request.session:
        return render(request,"Member/runpayment.html")
    elif 'reid' in request.session:
        return render(request,"Member/runpayment.html")
    else:
        return redirect("Guest:Login")
    #return render(request,"Member/runpayment.html")



def weeklycollectionpayment(request,wid):
    if 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        wdata=tbl_weeklycollection.objects.get(id=wid)
        if request.method=="POST":
            tbl_weeklycollectionpayment.objects.create(relative=rdata,weeklycollection_id=wdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")
    elif 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
    
        wdata=tbl_weeklycollection.objects.get(id=wid)
        if request.method=="POST":
            tbl_weeklycollectionpayment.objects.create(member=mdata,weeklycollection_id=wdata)
            return redirect("Member:runpayment")
        else:
            return render(request,"Member/DesignPayment.html")    
    else:
        return redirect("Guest:Login")

def monthlycollectionpayment(request,mcid):
    medata=tbl_memberadding.objects.get(id=request.session["mid"])
    
    mdata=tbl_monthlycollection.objects.get(id=mcid)
    if request.method=="POST":
        tbl_monthlycollectionpayment.objects.create(member=medata,monthlycollection_id=mdata)
        return redirect("Member:runpayment")
    else:
        return render(request,"Member/DesignPayment.html")


def viewevents(request):
    data=tbl_events.objects.all()
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        return render(request,"Member/viewevents.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        mdata=tbl_relatives.objects.get(id=request.session["reid"])
        return render(request,"Member/viewevents.html",{'datas':data,'data':mdata})
    else:
        return redirect("Guest:login")



def complaint(request):
    if 'mid' in request.session:
        mdata=tbl_memberadding.objects.get(id=request.session["mid"])
        data=tbl_complaint.objects.filter(member=mdata)
        if request.method=="POST":
            tbl_complaint.objects.create(title=request.POST.get('txt_title'),
            content=request.POST.get('txt_content'),member=mdata)
            return render(request,"Member/complaint.html",{'datas':data,'data1':mdata})
        else:
            return render(request,"Member/complaint.html",{'datas':data,'data1':mdata})
    elif 'reid' in request.session:
        rdata=tbl_relatives.objects.get(id=request.session["reid"])
        data=tbl_complaint.objects.filter(relative=rdata)
        if request.method=="POST":
            tbl_complaint.objects.create(title=request.POST.get('txt_title'),
            content=request.POST.get('txt_content'),relative=rdata)
            return render(request,"Member/complaint.html",{'datas':data,'data':rdata})
        else:
            return render(request,"Member/complaint.html",{'datas':data,'data':rdata})
    else:
        return redirect("Member:Homepage")
