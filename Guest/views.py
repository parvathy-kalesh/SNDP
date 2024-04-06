from django.shortcuts import render,redirect
from .models import*
from Admin.models import *
from Member.models import *


# Create your views here.


def home(request):
   return render(request,"Guest/index.html") 



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
        return render(request,"Guest/MemberRegistration.html",{'memdata':memdata,'disdata':disdata})
    else:
        return render(request,"Guest/MemberRegistration.html",{'memdata':memdata,'disdata':disdata}) 

def ajax_locatiom(request):
   plaob=tbl_place.objects.get(id=request.GET.get('Pla'))
   location=tbl_location.objects.filter(place=plaob)
   return render(request,"Guest/AjaxLocation.html",{'loc':location})

def login(request):
    if request.method=="POST":


      Email=request.POST.get('txt_email')
      Password=request.POST.get('txt_pass')
      acount=tbl_adminlogin.objects.filter(email=Email,password=Password).count()
    

      ucount=tbl_financehead.objects.filter(user_name=Email,password=Password).count()
      mcount=tbl_memberadding.objects.filter(email=Email,password=Password).count()
      relativecount=tbl_relatives.objects.filter(email=Email,password=Password).count()
      if ucount > 0:
         userdata=tbl_financehead.objects.get(user_name=Email,password=Password)
         request.session['fid']=userdata.id
         return redirect('FinanceHead:Homepage')
      elif mcount > 0:
         userdata=tbl_memberadding.objects.get(email=Email,password=Password)
         request.session['mid']=userdata.id
         return redirect('Member:Homepage')
      elif acount > 0:
         return redirect('Admin:Homepage')
      elif relativecount>0:
            relativedata=tbl_relatives.objects.get(email=Email,password=Password)
            request.session["reid"]=relativedata.id
            return redirect("Member:Homepage")
      else:
         msg = "Invalid Credentials!!"
         return render(request,"Guest/Login.html",{'msg':msg})
    else:
        return render(request,"Guest/Login.html")


