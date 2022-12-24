"""oespro URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from exam import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('index',views.index,name='index'),
    path('proctor',views.proctor,name='proctor'),
    path('candidate',views.candidate,name='candidate'),
    path('afterlogin_view',views.afterlogin_view,name='afterlogin_view'),
    path('contact',views.contact,name='contact'),
    path('logout',views.Logout,name='Logout'),
    path('registration_proctor',views.registration_proctor,name='registration_proctor'),
    path('login_proctor',views.login_proctor,name='login_proctor'),
    path('proctorbase',views.proctorbase,name='proctorbase'),
    path('proctorbase2',views.proctorbase2,name='proctorbase2'),
    #path('proctor_wait_approval',views.proctor_wait_approval,name='proctor_wait_approval'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('editcourse/<int:pk>',views.editcourse,name='editcourse'),
    path('viewcourse',views.viewcourse,name='viewcourse'),
    path('deletecourse/<int:pk>',views.deletecourse,name='deletecourse'),
    #path('vwcse',views.vwcse,name='vwcse'),
    path('addquestions',views.addquestions,name='addquestions'),
    path('view_course_questions',views.view_course_questions,name='view_course_questions'),
    path('viewquestions/<int:pk>',views.viewquestions,name='viewquestions'),
    path('editquestions/<int:pk>',views.editquestions,name='editquestions'),
    path('deletequestions/<int:pk>',views.deletequestions,name='deletequestions'),
    path('sendquestions',views.sendquestions,name='sendquestions'),
    path('profile_proctor',views.profile_proctor,name='profile_proctor'),
    path('editrequest_proctor',views.editrequest_proctor,name='editrequest_proctor'),
    path('registration_candidate',views.registration_candidate,name='registration_candidate'),
    path('candidate_wait_approval',views.candidate_wait_approval,name='candidate_wait_approval'),
    path('candidatebase',views.candidatebase,name='candidatebase'),
    path('candidatebase2',views.candidatebase2,name='candidatebase2'),
    path('profile_candidate',views.profile_candidate,name='profile_candidate'),
    path('editrequest_candidate',views.editrequest_candidate,name='editrequest_candidate'),
    path('view_result',views.view_result,name='view_result'),
    path('admin_login',views.admin_login,name='admin_login'),
     path('sub_admin_registration',views.sub_admin_registration,name='sub_admin_registration'),
    path('ProctorSection_login',views.ProctorSection_login,name='ProctorSection_login'),
    path('CandidateSection_login',views.CandidateSection_login,name='CandidateSection_login'),
    path('ExamSection_login',views.ExamSection_login,name='ExamSection_login'),
    path('ResultSection_login',views.ResultSection_login,name='ResultSection_login'),
    path('proctorsectionbase',views.proctorsectionbase,name='proctorsectionbase'),
    path('profilebase',views.profilebase,name='profilebase'),
    path('qbankbase',views.qbankbase,name='qbankbase'),
    path('candidatesectionbase',views.candidatesectionbase,name='candidatesectionbase'),
    path('adminbase',views.adminbase,name='adminbase'),
    path('reportbase',views.reportbase,name='reportbase'),
    path('approvedbase',views.approvedbase,name='approvedbase'),
    path('reportproctor_section',views.reportproctor_section,name='reportproctor_section'),
    path('reportcandidate_section',views.reportcandidate_section,name='reportcandidate_section'),
    path('reportexam_section',views.reportexam_section,name='reportexam_section'),
    path('reportresult_section',views.reportresult_section,name='reportresult_section'),
    path('attendexam',views.attendexam,name='attendexam'),
    path('admitcard_view',views.admitcard_view,name='admitcard_view'),
    path('edetails',views.edetails,name='edetails'),
    path('quesbank',views.quesbank,name='quesbank'),
    path('startexam',views.startexam,name='startexam'),
    path('pendingexisting_proctorlist',views.pendingexisting_proctorlist,name='pendingexisting_proctorlist'),
    path('pendingnew_proctorlist',views.pendingnew_proctorlist,name='pendingnew_proctorlist'),
    path('qualified_proctorlist/<int:pk>',views.qualified_proctorlist,name='qualified_proctorlist'),
    path('rejected_proctorlist',views.rejected_proctorlist,name='rejected_proctorlist'),
    path('orderquestions_to_proctor',views.orderquestions_to_proctor,name='orderquestions_to_proctor'),
    path('viewcourse_questions',views.viewcourse_questions,name='viewcourse_questions'),
    path('cprofilebase',views.cprofilebase,name='cprofilebase'),
    path('capprovedbase',views.capprovedbase,name='capprovedbase'),
    path('pendingexisting_candidatelist',views.pendingexisting_candidatelist,name='pendingexisting_candidatelist'),
    path('pendingnew_candidatelist',views.pendingnew_candidatelist,name='pendingnew_candidatelist'),
    path('qualified_candidatelist',views.qualified_candidatelist,name='qualified_candidatelist'),
    path('examsectionbase',views.examsectionbase,name='examsectionbase'),
    path('orderquestions_to_proctorsection',views.orderquestions_to_proctorsection,name='orderquestions_to_proctorsection'),
    path('viewfinalcourse_questions',views.viewfinalcourse_questions,name='viewfinalcourse_questions'),
    path('order_to_result',views.order_to_result,name='order_to_result'),
    path('admitcard_sent',views.admitcard_sent,name='admitcard_sent'),
    path('admitcard_list',views.admitcard_list,name='admitcard_list'),
    path('admitcard_details',views.admitcard_details,name='admitcard_details'),
    path('viewfinal_questions',views.viewfinal_questions,name='viewfinal_questions'),
    path('post_exam',views.post_exam,name='post_exam'),
    path('resultsectionbase',views.resultsectionbase,name='resultsectionbase'),
    path('viewresult',views.viewresult,name='viewresult'),
    path('publish_result',views.publish_result,name='publish_result'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
