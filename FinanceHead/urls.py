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
     


    
]