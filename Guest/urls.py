from django.urls import path
from Guest import views

app_name='Guest'
urlpatterns = [
    path('memberregistration/',views.mreg,name="MemberRegistration"),
    path('ajaxlocation/',views.ajax_locatiom,name="AjaxLocation"),
    path('login/',views.login,name="Login"),
  
   
]