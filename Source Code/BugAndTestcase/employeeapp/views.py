from django.shortcuts import render, redirect
from adminsapp.models import Employee, Project, News
from adminsapp.forms import EmployeeForm, ProjectForm
from employeeapp.models import Testcase, Bug, Requirements
from employeeapp.forms import TestcaseForm, BugForm, RequirementsForm
from django.db.models import Count
from managementapp.models import Task
from django.http import JsonResponse

# Create your views here.
def employee(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "employee_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "employee_login.html", {"msg": msg})
    return render(request, "employee_login.html", {})

def employee_home(request):
    return render(request, "employee_home.html", {})


def employee_change_pwd(request):
    email = request.session["email"]
    if islogin(request):
        # role = request.session["role"]
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                employee = Employee.objects.get(email=email, password=password)

                employee.password = new_password
                employee.save()
                msg = "Successfully Password Update"
                return render(request, "index.html", {"msg": msg})
            except:
                msg = "Invalid Data"
                return render(request, "employee_chpwd.html", {"msg": msg,"email":email})
        return render(request, "employee_chpwd.html", {"email":email})
    else:
        return render(request, "index.html", {"email":email})


def employee_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "employee_login.html", {})


def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def employee_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "employee_edit_profile.html", {"employ": employ, "role":role})


def employee_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "employee_home.html", {"msg": "Successfully Update", "role": role})
        except Exception as e:
            print(e)
            return render(request, "employee_home.html", {"msg": "your details not updated", "role":role})
    return render(request, "employee_edit_profile.html", {"employee":data, "role":role})


def add_testcase(request):
    if request.method == "POST":
        testcase = TestcaseForm(request.POST)
        print("hi1")
        try:
            if testcase.is_valid():
                print("hi2")
                testcase.save()
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_testcase.html", {"msg": "success"})
    tester_emails = request.session["email"]
    details_project = Project.objects.all()
    requirements = Requirements.objects.all()
    return render(request, "add_testcase.html", {"tester_emails": tester_emails, "details_project": details_project,"requirements":requirements})


def view_testcase(request):
    email = request.session["email"]
    if request.method == "GET":
        testcases = Testcase.objects.filter(tester_email=email)
        role=request.session["role"]
        return render(request, "view_testcase.html", {"testcases": testcases,"role": role})


def delete_testcase(request, id):
    testcase = Testcase.objects.get(id=id)
    testcase.delete()
    return redirect("/view_testcase")

def edit_testcase(request, id):
    testcases = Testcase.objects.get(id=id)
    tester_emails = request.session["email"]
    details_project = Project.objects.all()
    requirements = Requirements.objects.all()
    return render(request, "edit_testcase.html",
                  {"testcases": testcases, "tester_emails": tester_emails, "details_project": details_project,"requirements":requirements})


def update_testcase(request):
    if request.method == "POST":
        userid = request.POST["id"]
        testcase = Testcase.objects.get(id=userid)
        testcase = TestcaseForm(request.POST, instance=testcase)
        print("hi1")
        try:
            if testcase.is_valid():
                print("hi2")
                testcase.save()
                print("h3")
        except Exception as e:
            print(e)
            return redirect("/view_testcase", {"msg": "success"})
        return render(request, "edit_testcase.html", {})

def add_bug(request):
    if request.method == "POST":
        print("hi")
        bugs = BugForm(request.POST,request.FILES)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return render(request, "add_bug.html", {"msg": "success"})
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.filter(status='Fail')
    developersids = Employee.objects.filter(role='devloper')
    return render(request, "add_bug.html",
                          {"tested_by": tested_by, "testcaseids": testcaseids,"developersids":developersids})

def view_bug(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        role=request.session["role"]
        return render(request,"view_bug.html",{"bugs":bugs,"role":role})

def delete_bug(request, id):
    bugs = Bug.objects.get(id=id)
    bugs.delete()
    return redirect("/view_bug")

def edit_bug(request, id):
    bugs = Bug.objects.get(id=id)
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.filter(status='Fail')
    developersids = Employee.objects.filter(role='devloper')
    return render(request, "edit_bug.html",
                  {"tested_by": tested_by, "testcaseids": testcaseids,"bugs":bugs,"developersids":developersids})


def update_bug(request):
    if request.method == "POST":
        userid = request.POST["id"]
        bugs = Bug.objects.get(id=userid)
        print("hi")
        bugs = BugForm(request.POST,request.FILES,instance=bugs)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return redirect("/view_bug", {"msg": "success"})
    return render(request, "edit_bug.html", {})

def developer_view_bugs(request):
    email = request.session["email"]
    if request.method=="GET":
        role=request.session["role"]
        print(role)
        bugs=Bug.objects.filter(developer_email=email)
        return render(request,"developer_view_bugs.html",{"bugs":bugs,"role":role})

def developer_view_testcases(request):
    if request.method == "GET":
        role=request.session["role"]
        testcases = Testcase.objects.all()
        return render(request, "developer_view_testcases.html", {"testcases": testcases,"role":role})

def developer_update_status(request,id):
    bugs = Bug.objects.get(id=id)
    email= request.session["email"]
    return render(request,"developer_status_update.html",{"bugs":bugs,"email":email,"id":id})

def developer_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session["email"]
            status=request.POST['status']
            id=request.POST['id']
            print("hi1")
            print("hi2")
            bug=Bug.objects.get(id=id)
            print("hi3")
            bug.status=status
            bug.tested_by_email=tested_by_email
            print("hi4")
            bug.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "developer_view_bugs.html", {})
    return render(request, "developer_status_update.html", {})

def tester_update_status(request,id):
    bugs = Bug.objects.get(id=id)
    email= request.session["email"]
    return render(request,"tester_update_status.html",{"bugs":bugs,"email":email,"id":id})

def tester_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session["email"]
            status=request.POST['status']
            id=request.POST['id']
            print("hi1")
            print("hi2")
            bug=Bug.objects.get(id=id)
            print("hi3")
            bug.status=status
            bug.tested_by_email=tested_by_email
            print("hi4")
            bug.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "view_bug.html", {})
    return render(request, "tester_update_status.html", {})

def analyst_view_bugs(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        return render(request,"analyst_view_bugs.html",{"bugs":bugs})

def analyst_view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        return render(request, "analyst_view_testcases.html", {"testcases": testcases})

def developer(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "developer_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "developer.html", {"msg": msg})
    return render(request, "developer.html", {})

def developer_home(request):
    return render(request, "developer_home.html", {})

def developer_change_pwd(request):
    email = request.session["email"]
    if islogin(request):
        # role = request.session["role"]
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                employee = Employee.objects.get(email=email, password=password)

                employee.password = new_password
                employee.save()
                msg = "Successfully Password Update"
                return render(request, "index.html", {"msg": msg})
            except:
                msg = "Invalid Data"
                return render(request, "developer_change_pwd.html", {"msg": msg,"email":email})
        return render(request, "developer_change_pwd.html", {"email":email})
    else:
        return render(request, "index.html", {"email":email})


def developer_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "developer.html", {})

def developer_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "developer_edit_profile.html", {"employ": employ, "role":role})


def developer_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "developer.html", {"msg": "Successfully Update ", "role": role})
        except Exception as e:
            print(e)
            return render(request, "developer_edit_profile.html", {"msg": "Your Details Not Updated", "role":role})
    return render(request, "developer_edit_profile.html", {"employee":data, "role":role})


def analyst_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "analyst_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "analyst_login.html", {"msg": msg})
    return render(request, "analyst_login.html", {})

def analyst_home(request):
    return render(request, "analyst_home.html", {})

def analyst_change_pwd(request):
    email = request.session["email"]
    if islogin(request):
        # role = request.session["role"]
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                employee = Employee.objects.get(email=email, password=password)

                employee.password = new_password
                employee.save()
                msg = "Successfully Password Update"
                return render(request, "index.html", {"msg": msg})
            except:
                msg = "Invalid Data"
                return render(request, "analyst_change_pwd.html", {"msg": msg,"email":email})
        return render(request, "analyst_change_pwd.html", {"email":email})
    else:
        return render(request, "index.html", {"email":email})


def analyst_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "analyst_login.html", {})

def analyst_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "analyst_edit_profile.html", {"employ": employ, "role":role})


def analyst_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "analyst_login.html", {"msg": "Successfully Update ", "role": role})
        except Exception as e:
            print(e)
            return render(request, "analyst_edit_profile.html", {"msg": "Your Details Not Updated", "role":role})
    return render(request, "analyst_edit_profile.html", {"employee":data, "role":role})

def developer_view_projects(request):
    projects = Project.objects.all()
    return render(request, "developer_view_projects.html", {"projects": projects})



def employee_view_projects(request):
    projects = Project.objects.all()
    return render(request, "employee_view_projects.html", {"projects": projects})


def analyst_view_projects(request):
    projects = Project.objects.all()
    return render(request, "analyst_view_projects.html", {"projects": projects})


def add_requirements(request):
    email = request.session['email']
    projects = Project.objects.all()
    if request.method == "POST":
        requirements = RequirementsForm(request.POST)
        if requirements.is_valid():
            requirements.save()
        return render(request, "add_requirements.html", {"msg": "Success","projects":projects,"email":email})
    return render(request, "add_requirements.html", {"projects":projects,"email":email})

def analyst_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "analyst_view_requirements.html", {"requirements": requirements})

def developer_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "developer_view_requirements.html", {"requirements": requirements})


def employee_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "employee_view_requirements.html", {"requirements": requirements})

def testcase_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "testcase_bug_piechart.html", context)



def developer_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "developer_view_notifications.html", {"notifications": notifications})




def analyst_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "analyst_view_notifications.html", {"notifications": notifications})


def employee_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "employee_view_notifications.html", {"notifications": notifications})

# def employee_bug_piechart(request):
#     """
#     Generates data and renders the template with testcase and bug counts.
#     """
#
#     try:
#         requirements_count = Requirements.objects.count()
#         testcase_count = Testcase.objects.count()
#         bug_count = Bug.objects.count()
#
#         return render(request, "employee_bug_piechart.html", {"testcase_count": testcase_count, "bug_count": bug_count,"requirements_count":requirements_count})
#
#     except Exception as e:
#         print(e)
#         return render(request, "employee_bug_piechart.html", {"msg": "Error retrieving data."})

def analyst_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "analyst_bug_piechart.html", context)



def employee_update_testcases_status(request,id):
    testcases = Testcase.objects.get(id=id)
    email= request.session["email"]
    return render(request,"employee_update_testcases_status.html",{"testcases":testcases,"email":email,"id":id})

def employee_update_testcases_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session["email"]
            status=request.POST['status']
            comments=request.POST['comments']
            id=request.POST['id']
            print("hi1")
            print("hi2")
            testcases=Testcase.objects.get(id=id)
            print("hi3")
            testcases.status=status
            testcases.comments=comments
            testcases.tested_by_email=tested_by_email
            print("hi4")
            testcases.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "view_testcase.html", {})
    return render(request, "employee_update_testcases_status.html", {})

def employee_bug_piechart(request, id):
    # Get the project object based on ID
    projects = Project.objects.get(pk=id)

    # Count Requirements for the project
    requirements_count = Requirements.objects.filter(projects=projects).count()

    # Filter Testcases with status count
    project_testcases = Testcase.objects.filter(project_name=projects.title)  # Assign the queryset to a variable
    testcases_count = project_testcases.count()

    testcases_by_status = project_testcases.values('status').annotate(count=Count('id'))

    # Initialize test case counts
    testcases_pass_count = 0
    testcases_fail_count = 0
    testcases_new_count = 0

    # Extract counts from queryset
    for testcase in testcases_by_status:
        if testcase['status'] == 'Pass':
            testcases_pass_count = testcase['count']
        elif testcase['status'] == 'Fail':
            testcases_fail_count = testcase['count']
        elif testcase['status'] == 'new':
            testcases_new_count = testcase['count']

    # Filter Bugs using the assigned variable
    bugs = Bug.objects.filter(testcase_id__in=project_testcases.values_list('id', flat=True))
    bugs_count = bugs.count()

    context = {
        'projects': projects,
        'requirements_count': requirements_count,
        'testcases_count':testcases_count,
        'testcases_pass_count': testcases_pass_count,
        'testcases_fail_count': testcases_fail_count,
        'testcases_new_count': testcases_new_count,
        'bugs_count': bugs_count,
    }

    return render(request, "employee_bug_piechart.html", context)



def developer_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "developer_view_task.html", {"tasks": tasks})

def employee_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "employee_view_task.html", {"tasks": tasks})

def analyst_view_task(request):
    email= request.session["email"]
    if request.method == "GET":
        tasks = Task.objects.filter(employee_email=email)
        return render(request, "analyst_view_task.html", {"tasks": tasks})

def project_view_requirements(request):
    title = request.GET["project_title"]
    print("project ",title)
    projects = Project.objects.filter(title=title)
    requirements = Requirements.objects.filter(projects_id=projects[0].id)
    req_list = []
    for req in requirements:
        req_list.append(req.title)
    print(req_list)
    return JsonResponse(req_list,safe=False)


