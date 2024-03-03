from django.urls import path
from FinanceHead import views

app_name='FinanceHead'
urlpatterns = [
     path('homepage/',views.homepage,name="Homepage"),
     path('myprofile/',views.myprofile,name="MyProfile"),
     path('changepwd/',views.changep,name="ChangePassword"),
     path('chitty/',views.chitty,name="Chitty"),
     path('loan/',views.loan,name="Loan"),
     path('del_chitty/<int:did>',views.DeleteChitty,name="del_chitty"),
     path('del_loan/<int:did>',views.DeleteLoan,name="del_loan"),
    
     path('ViewChittyApply/',views.viewchittyapply,name="ViewChittyApply"),
     path('ViewLoanApply/',views.viewloanapply,name="ViewLoanApply"),
     path('acceptchiity/<int:did>',views.acceptchitty,name="acceptchitty"),
     path('rejectchiity/<int:did>',views.rejectchitty,name="rejectchitty"),
     path('acceptloan/<int:did>',views.acceptloan,name="acceptloan"),
     path('rejectloan/<int:did>',views.rejectloan,name="rejectloan"),
     path('ViewChittyFunding/',views.viewchittyfunding,name="ViewChittyFunding"),
     
  path('loancalender/<int:lid>', views.loancalender,name="loancalender"),
   path('loangviewloanrepayrant/<int:lid>', views.viewloanrepay,name="viewloanrepay"),
    path('chittycalender/<int:cid>', views.chittycalender,name="chittycalender"),
    path('deleteloancalender/<int:lid>',views.deleteloancalender,name="deleteloancalender"),
    path('deletechittycalender/<int:cid>',views.deletechittycalender,name="deletechittycalender"),


    path('viewchittypayment/<int:cid>', views.viewchittypay,name="viewchittypay"),
    path('weeklycollection/', views.weeklycollection,name="weeklycollection"),
     path('monthlycollection/', views.monthlycollection,name="monthlycollection"),
    path('deletemonthlycollection/<int:mid>',views.deletemonthlycollection,name="deletemonthlycollection"),
    path('deleteweeklycollection/<int:wid>',views.deleteweeklycollection,name="deleteweeklycollection"),
      path('viewweeklycollectionpayment/', views.viewweeklycollectionpayment,name="viewweeklycollectionpayment"),
    path('viewmonthlycollectionpayment/', views.viewmonthlycollectionpayment,name="viewmonthlycollectionpayment"),

    
]