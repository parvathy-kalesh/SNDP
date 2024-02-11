from django.urls import path
from Admin import views

app_name='Admin'
urlpatterns = [
    path('place/',views.pla,name="Place"),
    path('del_place/<int:did>',views.DeletePlace,name="del_place"),
    path('edit_place/<int:eid>',views.EditPlace,name="edit_place"),
    path('location/',views.loca,name="Location"),
    path('del_location/<int:sid>',views.DeleteLocation,name="del_location"),
    path('loan/',views.loan,name="Loan"),
    path('del_loan/<int:did>',views.DeleteLoan,name="del_loan"),
    path('edit_loan/<int:eid>',views.EditLoan,name="edit_loan"),
    path('proof/',views.proof,name="Proof"),
    path('del_proof/<int:did>',views.DeleteProof,name="del_proof"),
    path('edit_proof/<int:eid>',views.EditProof,name="edit_proof"),
    path('scheme/',views.scheme,name="Scheme"),
    path('del_scheme/<int:did>',views.DeleteScheme,name="del_scheme"),
    path('edit_scheme/<int:eid>',views.EditScheme,name="edit_scheme"),
    path('relation/',views.relationtype,name="Relationtype"),
    path('del_relation/<int:did>',views.DeleteRelation,name="del_relation"),
    path('edit_relation/<int:eid>',views.EditRelation,name="edit_relation"),
    path('scholarship/',views.scholarshiptype,name="Scholarshiptype"),
    path('del_scholarship/<int:did>',views.DeleteScholarship,name="del_scholarship"),
    path('edit_scholarship/<int:eid>',views.EditScholarship,name="edit_scholarship"),
    path('election/',views.electionposition,name="Electionposition"),
    path('del_election/<int:did>',views.DeleteElection,name="del_election"),
    path('edit_election/<int:eid>',views.EditElection,name="edit_election"),
    path('financehead/',views.financehead,name="FinanceHeadRegistration"),
    path('del_finance/<int:did>',views.DeleteFinance,name="del_finance"),
    path('memberregistration/',views.mreg,name="MemberRegistration"),
    path('del_member/<int:did>',views.DeleteMember,name="del_memberregister"),
    path('scholarshipe/',views.scholar,name="Scholarship"),
    path('del_sholarshipe/<int:did>',views.Deletesc,name="del_scholarshipe"),
    path('electiondec/',views.electiondec,name="ElectionDeclaration"),
    path('del_electiondec/<int:did>',views.Deleteec,name="del_electiondec"),
    path('ViewScholarApply/',views.viewscholarapply,name="ViewScholarApply"),
    path('acceptscholar/<int:did>',views.acceptscholar,name="acceptscholar"),
    path('rejectscholar/<int:did>',views.rejectscholar,name="rejectscholar"),

   
]