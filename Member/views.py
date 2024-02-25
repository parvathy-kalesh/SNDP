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
            return render(request,"Member/ScholarshipApply.html",{'data':data,'schdata':schdata})
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
            return render(request,"Member/chittyapply.html",{'cdata':chittydata,'ptype':prooftype,'data1':memberdata})
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
        if request.method=="POST" and request.FILES:
           
            ptype=tbl_proof.objects.get(id=request.POST.get('ptype'))
            tbl_loanapply.objects.create(member_name=memberdata,loan_name=loan,
            proof_name=ptype,document=request.FILES.get('proof'))
            return render(request,"Member/LoanApply.html",{'cdata':loan,'ptype':prooftype,'data1':memberdata})
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
        mdata=tbl_chittyjoin.objects.filter(memberdata=memberdata)
        return render(request,"Member/ChittyStatusview.html",{'chittystatusview':mdata,'data1':memberdata})
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
    pid=6
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.get(id=request.session["election"])
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray.append(ecount)
    large=max(parray)
    datas=zip(pdata,parray)

    pid=5
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.get(id=request.session["election"])
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray.append(ecount)
    large1=max(parray)
    datas1=zip(pdata,parray)

    pid=4
    posItiondata=tbl_electionposition.objects.get(id=pid)
    edata=tbl_electiondeclaration.objects.get(id=request.session["election"])
    pdatacount=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata).count()
    pdata=tbl_electionapply.objects.filter(election_name=edata,election_position=posItiondata)
    parray=[]
    for i in pdata:
        ecount=tbl_voting.objects.filter(electionapply=i.id).count()
        parray.append(ecount)
    large2=max(parray)
    datas2=zip(pdata,parray)
    return render(request,"Admin/Secretary.html",{'datas':datas,'datas1':datas1,'win1':large,'win2':large1,'win3':large2})


      

