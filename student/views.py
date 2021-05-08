from django.shortcuts import render
from django.http import HttpResponse
from student.models import Studentdetails, Coursedetails, CommentData, Studentenrollment
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    if 'username' in request.session:
        uname = request.session['username']
    request.session['title'] = "Final Project"
    f = "freshman"
    so = "sophomore"
    j = "junior"
    se = "senior"
    cursorobj = connection.cursor()
    cursorobj.execute("select count(*) from fproject_mysql.student_studentdetails")
    studentnum = cursorobj.fetchone()
    cursorobj.execute("select count(*) from fproject_mysql.student_studentdetails where studentyear = %s", [f]) 
    freshmannum = cursorobj.fetchone()
    cursorobj.execute("select count(*) from fproject_mysql.student_studentdetails where studentyear = %s", [so])
    sophomorenum = cursorobj.fetchone()
    cursorobj.execute("select count(*) from fproject_mysql.student_studentdetails where studentyear = %s", [j])
    juniornum = cursorobj.fetchone()
    cursorobj.execute("select count(*) from fproject_mysql.student_studentdetails where studentyear = %s", [se])
    seniornum = cursorobj.fetchone()
    cursorobj.execute("select count(*) from fproject_mysql.student_coursedetails")
    coursenum = cursorobj.fetchone()
    cursorobj.execute("select round(avg(studentgpa), 2) from fproject_mysql.student_studentdetails")
    gpaavg = cursorobj.fetchone()
    context = {'name':'Gil Kiesler', 'studnum': studentnum[0], 'freshmen': freshmannum[0], 'sophomore': sophomorenum[0], 'junior': juniornum[0],
    'senior': seniornum[0], 'cournum': coursenum[0], 'avggpa': gpaavg[0]}
    return render(request, 'student/home.html', context)
    
@login_required
def studentdetails(request):
#    studentdetails = Studentdetails.objects.filter(firstname = 'gil') #variables by filter
    studentdata = Studentdetails.objects.all() #all variables
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data': minidata}
    
    return render(request, 'student/studentdetails.html', context)
    
@login_required    
def coursedetails(request):
    coursedata = Coursedetails.objects.all() #all variables
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data': minidata}
    return render(request, 'student/coursedetails.html', context)   
    
def commentpage(request):
    request.session['username'] = request.user.username # session variable
    return render(request, 'student/comment.html')
    
    
def savedata(request):
    if('email' and 'comment' in request.GET):
        emailid = request.GET.get('email')
        commentdata = request.GET.get('comment')
        dataobj = CommentData(emailid = emailid, commentdata = commentdata)
        dataobj.save()
    return HttpResponse("Success")
    
def studentenrollment(request):
    studentdata = Studentdetails.objects.all()
    coursedata = Coursedetails.objects.all()
    if 'studentname' in request.session:
        enrollmentdata = Studentenrollment.objects.filter(sname = request.session['studentname'])
    else:
        enrollmentdata = Studentenrollment.objects.all()
    context = {'student':studentdata,'course':coursedata, 'enrollment': enrollmentdata }
    return render(request, 'student/enrollment.html', context )
    
def saveenrollment(request):
    if('namestudent' in request.GET and 'titlecourse' not in request.GET):
        request.session['studentname'] = request.GET.get('namestudent')
    if('namestudent' and 'titlecourse' in request.GET):
        sname = request.GET.get('namestudent')
        course = request.GET.get('titlecourse')
        cnt = Studentenrollment.objects.filter(sname = sname).count()
        cnt2 = Studentenrollment.objects.filter(sname = sname, course = course).count()
        if(cnt >= 3):
            return HttpResponse("Failure")
        elif(cnt2 != 0):
            return HttpResponse("Failure")
        else:
            dataobj = Studentenrollment(sname = sname, course = course)
            dataobj.save()
            return HttpResponse("Success")
    
def dictfetchall(cursor):
    "return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return[
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


