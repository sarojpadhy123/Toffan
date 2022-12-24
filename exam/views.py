# Create your views here.
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def proctor(request):
    error=""
    if request.method == 'POST':
        ue = request.POST['mailid']
        pd = request.POST['password']
        user = authenticate(username=ue, password=pd)
        try:
            if user:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"

    return render(request,'proctor.html',locals())

def candidate(request):
    error=""
    if request.method == 'POST':
        ue = request.POST['mailidn']
        pd = request.POST['pass']
        user = authenticate(username=ue, password=pd)
        try:
            if user:
                login(request, user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"

    return render(request,'candidate.html',locals())

def afterlogin_view(request):
    '''if CandidateRegistration(request.user):
        accntapproval=CandidateRegistration.objects.all().filter(user_id=request.user.id,status=True)
        if accntapproval:
            return redirect('candidatebase')
        else:
            return render(request,'candidate/candidate_wait_approval.html')
    else:
        return redirect('candidatesectionbase')
    '''
    if ProctorRegistration(request.user):
        accountapproval=ProctorRegistration.objects.all().filter(user_id=request.user.id)
        if accountapproval:
            return redirect('proctorbase')
        else:
            return render(request,'proctor/proctor_wait_approval.html')
    else:
        return redirect('pendingexisting_proctorlist')

def contact(request):
    return render(request,'contact.html')

def registration_proctor(request):
    error = ""
    if request.method == "POST":
        se = request.POST['surname']
        fe = request.POST['fullname']
        fs = request.POST['fname']
        ms = request.POST['mname']
        db = request.POST['dob']
        gd = request.POST['gender']
        em = request.POST['emailid']
        cno = request.POST['contactno']
        idf = request.POST['idproof']
        idn = request.POST['idno']
        dgr = request.POST['edegree']
        oth1 = request.POST['other1']
        pdgr = request.POST['pdegree']
        oth2 = request.POST['other2']
        mn = request.POST['mqlfn']
        oth3 = request.POST['other3']
        sm = request.POST['stream']
        oth4 = request.POST['other4']
        hs = request.POST['honours']
        oth5 = request.POST['other5']
        poy = request.POST['poy']
        cn = request.POST['cname']
        un = request.POST['uname']
        sad = request.POST['sad']
        dsg = request.POST['dsg']
        uec = request.POST['uec']
        upc = request.POST['upc']
        al1 = request.POST['al1']
        al2 = request.POST['al2']
        dt = request.POST['district']
        st = request.POST['state']
        cy = request.POST['country']
        pe = request.POST['pincode']
        pwd = request.POST['cnpwd']

        if len(request.FILES)!=0:
            upsp = request.FILES['upsp']

        try:
            user=User.objects.create_user(first_name=fe,username=em,password=pwd)
            ProctorRegistration.objects.create(user=user, Full_Name=fe,Surname=se,Contact_No=cno,Email_Id=em,Fathers_Name=fs,Mothers_Name=ms,Date_of_Birth=db,
            Gender=gd,ID_PROOF=idf,ID_NO=idn,Degree=dgr,If_Other1_Please_Specify=oth1,Proctorship_Degree=pdgr,If_Other2_Please_Specify=oth2,
            Max_Qualification=mn,If_Other3_Please_Specify=oth3,Stream=sm,If_Other4_Please_Specify=oth4,Honours=hs,If_Other5_Please_Specify=oth5, Passed_Out_Year=poy,
            College_Name=cn,University_Name=un,Designation=dsg,Subject_Questions_Added=sad,Upload_Educational_Certificate=uec,Upload_Proctor_Certificate=upc,
            Upload_Passport_Size_Photo=upsp,Address_Line1=al1,Address_Line2=al2,District=dt,State=st,Country=cy,Pincode=pe)
            user.save()
            error = "no"
        except:
            error = "yes"

    return render(request,'proctor/registration_proctor.html',locals())

def Logout(request):
    logout(request)
    return redirect('/')
'''
def proctor_wait_approval(request):
    return render(request, 'proctor/proctor_wait_approval.html')
'''
def login_proctor(request):
    return render(request, 'proctor/login_proctor.html')

def proctorbase(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    return render(request, 'proctor/proctorbase.html')

def proctorbase2(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    return render(request, 'proctor/proctorbase2.html')

def addcourse(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    if request.method == "POST":
        cne = request.POST['csename']
        tq = request.POST['ttlques']
        tm = request.POST['ttlmks']
        Add_Course.objects.create(Course_Name=cne,Total_Question=tq,Total_Marks=tm)
    return render(request, 'proctor/add_course.html')

def editcourse(request,pk):
    if not request.user.is_authenticated:
        return redirect('proctor')
    error = False
    data = Add_Course.objects.get(id=pk)
    if request.method=='POST':
        ce = request.POST['csename']
        tqs = request.POST['ttlques']
        tms = request.POST['ttlmks']
        data.Course_Name = ce
        data.Total_Question = tqs
        data.Total_Marks = tms
        data.save()
        error=True
        return redirect('viewcourse')

    d = {'data':data,'error':error}
    return render(request, 'proctor/edit_course.html',d)

def viewcourse(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    courses = Add_Course.objects.all()
    d={'courses':courses}
    return render(request, 'proctor/view_course.html',d)

def deletecourse(request,pk):
    if not request.user.is_authenticated:
        return redirect('proctor')
    courses=Add_Course.objects.get(id=pk)
    courses.delete()
    return redirect('viewcourse')
'''
def vwcse(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    courses = Add_Course.objects.values('Course_Name')
    d={'courses':courses}
    return render(request, 'proctor/vwcse.html',d)
'''
def addquestions(request):
    if not request.user.is_authenticated:
        return redirect('proctor')

    courses = Add_Course.objects.values('Course_Name')
    if request.method == "POST":
        cs = request.POST.get('course')
        qn = request.POST['qname']
        s = request.POST['smark']
        op1 = request.POST['option1']
        op2 = request.POST['option2']
        op3 = request.POST['option3']
        op4 = request.POST['option4']
        ans = request.POST['ans']
        courses.Course_Name = cs

        Add_Question.objects.create(Question_Name=qn,Select_Mark=s,Option1=op1,Option2=op2,Option3=op3,Option4=op4,Correct_Answer=ans)

    return render(request, 'proctor/addquestions.html',{'courses':courses})

def view_course_questions(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    courses = Add_Course.objects.all()
    return render(request,'proctor/view_course_questions.html',{'courses':courses})

def viewquestions(request,pk):
    if not request.user.is_authenticated:
        return redirect('proctor')
    questions=Add_Question.objects.all().filter(Course_id=pk)
    return render(request, 'proctor/viewquestions.html',{'questions':questions})

def editquestions(request,pk):
    if not request.user.is_authenticated:
        return redirect('proctor')
    data = Add_Question.objects.get(id=pk)
    error = False
    if request.method=='POST':
        q = request.POST['qname']
        m = request.POST['smark']
        o1 = request.POST['option1']
        o2 = request.POST['option2']
        o3 = request.POST['option3']
        o4 = request.POST['option4']
        ans = request.POST['ans']
        data.Question_Name = q
        data.Select_Mark = m
        data.Option1 = o1
        data.Option2 = o2
        data.Option3 = o3
        data.Option4 = o4
        data.Correct_Answer = ans
        data.save()
        error=True
        return redirect('/viewquestions')

    d = {'data':data,'error':error}
    return render(request, 'proctor/editquestions.html',d)

def deletequestions(request,pk):
    if not request.user.is_authenticated:
        return redirect('proctor')
    questions=Add_Question.objects.get(id=pk)
    questions.delete()
    return redirect('viewquestions')

def sendquestions(request):
    return render(request, 'proctor/sendquestions.html')

def profile_proctor(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    user = User.objects.get(id=request.user.id)
    data = ProctorRegistration.objects.get(user = user)

    d = {'data':data,'user':user}
    return render(request, 'proctor/profile_proctor.html',d)

def editrequest_proctor(request):
    if not request.user.is_authenticated:
        return redirect('proctor')
    user = User.objects.get(id=request.user.id)
    data = ProctorRegistration.objects.get(user = user)
    error = False
    if request.method == "POST":
        se = request.POST.get('surname')
        fe = request.POST.get('fullname')
        fs = request.POST.get('fname')
        ms = request.POST.get('mname')
        db = request.POST.get('dob')
        gd = request.POST.get('gender')
        em = request.POST.get('emailid')
        cno = request.POST.get('cno')
        idf = request.POST.get('idproof')
        idn = request.POST.get('idno')
        dgr = request.POST.get('edegree')
        oth1 = request.POST.get('other1')
        pdgr = request.POST.get('pdegree')
        oth2 = request.POST.get('other2')
        mn = request.POST.get('mqlfn')
        oth3 = request.POST.get('other3')
        sm = request.POST.get('stream')
        oth4 = request.POST.get('other4')
        hs = request.POST.get('honours')
        oth5 = request.POST.get('other5')
        poy = request.POST.get('poy')
        cn = request.POST.get('cname')
        un = request.POST.get('uname')
        sad=request.POST.get('sad')
        dsg=request.POST.get('dsgn')
        uec = request.POST.get('uec')
        upc = request.POST.get('upc')

        if len(request.FILES)!=0:
            ups = request.FILES['ups']

        user.first_name = fe
        data.Surname = se
        data.Fathers_Name = fs
        data.Mothers_Name = ms
        data.Date_of_Birth = db
        data.ID_PROOF = idf
        data.ID_NO = idn
        data.Gender = gd
        data.Contact_No = cno
        user.username = em
        data.Degree = dgr
        data.If_Other1_Please_Specify = oth1
        data.Proctorship_Degree = pdgr
        data.If_Other2_Please_Specify = oth2
        data.Max_Qualification = mn
        data.If_Other3_Please_Specify = oth3
        data.Stream = sm
        data.If_Other4_Please_Specify = oth4
        data.Honours = hs
        data.If_Other5_Please_Specify = oth5
        data.Passed_Out_Year = poy
        data.College_Name = cn
        data.University_Name = un
        data.Designation = dsg
        data.Subject_Questions_Added = sad
        data.Upload_Educational_Certificate = uec
        data.Upload_Proctor_Certificate = upc
        data.Upload_Passport_Size_Photo = ups
        user.save()
        data.save()
        error=True
        return HttpResponseRedirect('profile_proctor')

    d = {'data':data,'user':user,'error':error}
    return render(request, 'proctor/editrequest_proctor.html',d)

def registration_candidate(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['fullname']
        fs = request.POST['fname']
        ms = request.POST['mname']
        db = request.POST['dob']
        gd = request.POST['gender']
        em = request.POST['emailid']
        cno = request.POST['contactno']
        idf = request.POST['idproof']
        idn = request.POST['idno']
        dgr = request.POST['edegree']
        oth1 = request.POST['other1']
        cqlfn = request.POST['cqlfn']
        oth2 = request.POST['other2']
        sm = request.POST['stream']
        oth3 = request.POST['other3']
        hs = request.POST['honours']
        oth4 = request.POST['other4']
        scn = request.POST['sclcname']
        bd = request.POST['board']
        un = request.POST['uname']
        al1 = request.POST['al1']
        al2 = request.POST['al2']
        dt = request.POST['district']
        st = request.POST['state']
        cy = request.POST['country']
        pe = request.POST['pincode']
        pwd = request.POST['cnpwd']

        if len(request.FILES)!=0:
            upsp = request.FILES['upsp']

        try:
            user = User.objects.create_user(first_name=fn,username=em,password=pwd)
            CandidateRegistration.objects.create(user=user, Full_Name=fn,Contact_No=cno,Email_Id=em,Fathers_Name=fs,Mothers_Name=ms,Date_of_Birth=db,
            Gender=gd,ID_PROOF=idf,ID_NO=idn,Educational_Degree=dgr,If_Other1_Please_Specify=oth1,Current_Qualification=cqlfn,If_Other2_Please_Specify=oth2,
            Stream=sm,If_Other3_Please_Specify=oth3,Honours=hs,If_Other4_Please_Specify=oth4,School_Name_or_College_Name=scn,Board = bd,
            University_Name=un,Upload_Passport_Size_Photo=upsp,Address_Line1=al1,Address_Line2=al2,District=dt,State=st,Country=cy,Pincode=pe)
            error="no"
        except:
            error="yes"

    return render(request,'candidate/registration_candidate.html',locals())

def candidatebase(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/candidatebase.html')

def candidatebase2(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/candidatebase2.html')

def candidate_wait_approval(request):
    return render(request, 'candidate/candidate_wait_approval.html')

def profile_candidate(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    user = User.objects.get(id=request.user.id)
    data = CandidateRegistration.objects.get(user = user)

    d = {'data':data,'user':user}
    return render(request, 'candidate/profile_candidate.html',d)

def editrequest_candidate(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    user = User.objects.get(id=request.user.id)
    data = CandidateRegistration.objects.get(user = user)
    error = False
    if request.method=='POST':
        fe = request.POST.get('fullname')
        fs = request.POST.get('fname')
        ms = request.POST.get('mname')
        db = request.POST.get('dob')
        gd = request.POST.get('gender')
        em = request.POST.get('emailid')
        cno = request.POST.get('cno')
        idf = request.POST.get('idproof')
        idn = request.POST.get('idno')
        edgr = request.POST.get('edegree')
        oth1 = request.POST.get('other1')
        cqlfn = request.POST.get('cqlfn')
        oth2 = request.POST.get('other2')
        sm = request.POST.get('stream')
        oth3 = request.POST.get('other3')
        hs = request.POST.get('honours')
        oth4 = request.POST.get('other4')
        scn = request.POST.get('sclcname')
        un = request.POST.get('uname')

        if len(request.FILES)!=0:
            upsp = request.FILES['upsp']

        user.first_name = fe
        data.Fathers_Name = fs
        data.Mothers_Name = ms
        data.Date_of_Birth = db
        data.ID_PROOF = idf
        data.ID_NO = idn
        data.Gender = gd
        data.Contact_No = cno
        user.username = em
        data.Upload_Passport_Size_Photo = upsp
        data.Educational_Degree = edgr
        data.If_Other1_Please_Specify = oth1
        data.Current_Qualification = cqlfn
        data.If_Other2_Please_Specify = oth2
        data.Stream = sm
        data.If_Other3_Please_Specify = oth3
        data.Honours = hs
        data.If_Other4_Please_Specify = oth4
        data.School_Name_or_College_Name = scn
        data.University_Name = un
        user.save()
        data.save()
        error=True
        return HttpResponseRedirect('profile_candidate')

    d = {'data':data,'user':user,'error':error}
    return render(request, 'candidate/editrequest_candidate.html',d)

def attendexam(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/attend_exam.html')

def admitcard_view(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/admitcard_view.html')

def startexam(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/startexam.html')

def view_result(request):
    if not request.user.is_authenticated:
        return redirect('candidate')
    return render(request, 'candidate/viewresult.html')

def admin_login(request):
    error=" "
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin/admin_login.html',locals())

def ProctorSection_login(request):
    error=" "
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'admin/ProctorSection_login.html',locals())

def CandidateSection_login(request):
    error=" "
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin/CandidateSection_login.html',locals())

def ExamSection_login(request):
    error=" "
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin/ExamSection_login.html',locals())

def ResultSection_login(request):
    error=" "
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin/ResultSection_login.html',locals())

def adminbase(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/adminbase.html')

def sub_admin_registration(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method=='POST':
        s = request.POST['sadmin']
        m = request.POST['mno']
        eid = request.POST['emailid']
        a = request.POST['address']
        ds = request.POST['deptsec']
        ld = request.POST['loginid']
        p = request.POST['pwd']

        user = User.objects.create_user(username = ld, first_name = s, password=p)
        Sub_Admin_Registration.objects.create(user=user, Sub_Admin_Name = s, Mobile_Number = m, Email_Id = eid, Address = a,
        Section = ds, Login_Id = ld)

    return render(request, 'admin/sub-admin_registration.html')

def reportbase(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/reportbase.html')

def reportproctor_section(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/reportproctor_section.html')

def reportcandidate_section(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/reportcandidate_section.html')

def reportexam_section(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/reportexam_section.html')

def reportresult_section(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin/reportresult_section.html')

def profilebase(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/profilebase.html')

def pendingexisting_proctorlist(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    proctors = ProctorRegistration.objects.values('Full_Name','Upload_Passport_Size_Photo','Contact_No','Designation','Max_Qualification','Stream','ID_PROOF','ID_NO')
    return render(request, 'admin/pendingexisting_proctorlist.html',{'proctors':proctors})

def pendingnew_proctorlist(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/pendingnew_proctorlist.html')

def approvedbase(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/approvedbase.html')

def proctorsectionbase(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/proctorsectionbase.html')

def qbankbase(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/qbankbase.html')

def qualified_proctorlist(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    proctors = ProctorRegistration.objects.values('Full_Name','Upload_Passport_Size_Photo','Contact_No','Designation','Max_Qualification','Stream','ID_NO','ID_PROOF')
    return render(request, 'admin/qualified_proctorlist.html',{'proctors':proctors})

def rejected_proctorlist(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/rejected_proctorlist.html')

def orderquestions_to_proctor(request):
    if not request.user.is_authenticated:
        return redirect('ProctorSection_login')
    return render(request, 'admin/orderquestions_to_proctor.html')

def candidatesectionbase(request):
    if not request.user.is_authenticated:
        return redirect('CandidateSection_login')
    return render(request, 'admin/candidatesectionbase.html')

def cprofilebase(request):
    if not request.user.is_authenticated:
        return redirect('CandidateSection_login')
    return render(request, 'admin/cprofilebase.html')

def capprovedbase(request):
    if not request.user.is_authenticated:
        return redirect('CandidateSection_login')
    return render(request, 'admin/capprovedbase.html')

def pendingexisting_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('CandidateSection_login')
    return render(request, 'admin/pendingexisting_candidatelist.html')

def pendingnew_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('CandidateSection_login')
    return render(request, 'admin/pendingnew_candidatelist.html')

def viewcourse_questions(request):
    return render(request, 'admin/viewcourse_questions.html')

def qualified_candidatelist(request):
    return render(request, 'admin/qualified_candidatelist.html')

def examsectionbase(request):
    return render(request, 'admin/examsectionbase.html')

def post_exam(request):
    return render(request, 'admin/post_exam.html')

def edetails(request):
    return render(request, 'admin/edetails.html')

def quesbank(request):
    return render(request, 'admin/quesbank.html')

def orderquestions_to_proctorsection(request):
    return render(request, 'admin/orderquestions_to_proctorsection.html')

def viewfinalcourse_questions(request):
    return render(request, 'admin/viewfinalcourse_questions.html')

def admitcard_sent(request):
    return render(request, 'admin/admitcard_sent.html')

def admitcard_list(request):
    return render(request, 'admin/admitcard_list.html')

def admitcard_details(request):
    return render(request, 'admin/admitcard_details.html')

def viewfinal_questions(request):
    return render(request, 'admin/viewfinal_questions.html')

def order_to_result(request):
    return render(request, 'admin/order_to_result.html')

def resultsectionbase(request):
    return render(request, 'admin/resultsectionbase.html')

def viewresult(request):
    return render(request, 'admin/viewresult.html')

def publish_result(request):
    return render(request, 'admin/publish_result.html')
