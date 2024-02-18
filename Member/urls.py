from django.urls import path
from Member import views

app_name='Member'
urlpatterns = [
     path('homepage/',views.homepage,name="Homepage"),
     path('myprofile/',views.profile, name="MyProfile"),
     path('editprofile/',views.editprofile,name="EditProfile"),
     path('changepassword/',views.changep,name="ChangePassword"),
     path('viewchitty/',views.vchitty,name="ViewChitty"),
     path('viewloan/',views.vloan,name="ViewLoan"),
     path('viewscholar/',views.vscholarship,name="ViewScholarship"),
     path('ajaxchitty/',views.ajaxchitty,name="ajaxchitty"),
     path('ajaxloan/',views.ajaxloan,name="ajaxloan"),
     path('ajaxscholar/',views.ajaxscholar,name="ajaxscholar"),
     path('relatives/',views.relatives,name="Relative"),
     path('veledec/',views.veledec,name="ViewElectiondec"),
     path('Ajaxrelation/', views.Ajaxrelation,name="Ajaxrelation"),
     path('deleterelative/<int:did>',views.Deleterelative,name="deleterelative"),
     path('logout/',views.logout,name="logout"),
     path('ScholarshipApply/<int:schid>',views.schapply,name="ScholarshipApply"),
     path('ChittyApply/<int:chid>',views.chittyapply,name="ChittyApply"),
     path('LoanApply/<int:lnid>',views.loanapply,name="LoanApply"),
     path('ViewLoanApply/',views.viewloanapply,name="ViewLoanApply"),
     path('ViewScholarShipApply/',views.viewscholarshipapply,name="ViewScholarShipApply"),
     path('ViewChittyApply/',views.viewchittyapply,name="ViewChittyApply"),
     path('scholarshipstatus/', views.scholarshipstatus,name="scholarshipstatus"),
     path('chittystatusview/', views.chittystatusview,name="chittystatusview"),
     path('loanstatusview/', views.loanstatusview,name="loanstatusview"),
     path('applyelec/<int:did>',views.applyelec,name="applyelec"),
     path('ElectionApply/<int:lnid>',views.electionapply,name="ElectionApply"),
     path('ViewElectionapply/',views.viewelectionapply,name="ViewElectionapply"),
     path('ViewCandidates/<int:elid>',views.viewcandidates,name="ViewCandidates"),
     path('Vote/<int:vid>',views.votenow,name="Vote"),
     path('Voting/<int:vid>',views.voting,name="Voting"),
     path('results/',views.results,name="results"),

    
]