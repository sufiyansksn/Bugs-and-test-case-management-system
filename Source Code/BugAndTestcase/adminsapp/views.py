from django.shortcuts import render, redirect
from adminsapp.models import Admins
from adminsapp.models import Employee
from adminsapp.forms import EmployeeForm
from adminsapp.models import Project
from adminsapp.forms import ProjectForm
from employeeapp.models import Bug, Testcase, Requirements
from employeeapp.forms import BugForm, TestcaseForm
from adminsapp.models import News
from adminsapp.forms import NewsForm
from django.db.models import Count


# Create your views here.

def admins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        request.session["username"] = username
        try:
            admin = Admins.objects.get(username=username, password=password)

            msg = "Data Found"
            print("msg")
            return render(request, "admins_home.html", {"admin": admin, "msg": msg})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "admins.html", {"msg": msg})
    return render(request, "admins.html", {})


def admins_home(request):
    return render(request, "admins_home.html", {})


def admins_change_pwd(request):
    username = request.session["username"]
    if islogin(request):
        if request.method == "POST":
            username = request.session["username"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                admins = Admins.objects.get(username=username, password=password)
                admins.password = new_password
                admins.save()
                msg = "Successfully Password Update"
                return redirect("/admins_logout",{"msg":msg})
            except:
                return render(request, "admins_chpwd.html", {"msg": "Invalid Data", "username":username})
        return render(request, "admins_chpwd.html", {"username":username})
    else:
        return render(request, "admins.html", {"username":username})


def admins_logout(request):
    request.session["username"] = ""
    del request.session["username"]
    return render(request, "admins.html", {})


def islogin(request):
    if request.session.__contains__("username"):
        return True
    else:
        return False


def add_employee(request):
    if request.method == "POST":
        print("hi")
        employee = EmployeeForm(request.POST)
        print("hi1")
        try:
            if employee.is_valid():
                print("hi2")
                employee.save()
                return render(request, "add_employee.html", {"msg": "Success"})
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_employee.html", {})
    return render(request, "add_employee.html", {})


def view_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
    return render(request, "view_employee.html", {"employee": employee})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/view_employee")


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit_employee.html", {"employee": employee})


def update_employee(request):
    if request.method == "POST":
        print("h")
        userid = request.POST["id"]
        print("hi")
        employee = Employee.objects.get(id=userid)
        print("HI")
        employee = EmployeeForm(request.POST, instance=employee)
        print("hii")
        if employee.is_valid():
            print("hiii")
            employee.save()
            print("hiiiii")
        return redirect("/view_employee")
    return redirect("/view_employee")


def add_project(request):
    managers = Employee.objects.filter(role="manager")
    return render(request, "add_project.html", {"managers": managers})


def add_new_project(request):
    if request.method == "POST":
        project = ProjectForm(request.POST)
        try:
            if project.is_valid():
                print("hi2")
                project.save()
                print("h3")
                return render(request, "admins_home.html", {})
        except Exception as e:
            print(e)
            return render(request, "add_project.html", {})
    return render(request, "add_project.html", {})


def view_project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
    return render(request, "view_project.html", {"projects": projects})


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/view_project")


def edit_project(request, id):
    project = Project.objects.get(id=id)
    managers = Employee.objects.filter(role="manager")
    return render(request, "edit_project.html", {"project": project, "managers": managers})


def update_project(request):
    if request.method == "POST":
        print("h")
        userid = request.POST["id"]
        print("hi")
        project = Project.objects.get(id=userid)
        print("HI")
        project = EmployeeForm(request.POST, instance=project)
        print("hii")
        if project.is_valid():
            print("hiii")
            project.save()
            print("hiiiii")
        return redirect("/view_project")
    return redirect("/view_project")


def view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
    return render(request, "view_testcases.html", {"testcases": testcases})


def view_bugs(request):
    if request.method == "GET":
        bugs = Bug.objects.all()
    return render(request, "view_bugs.html", {"bugs": bugs})


def add_news(request):
    if request.method == "POST":
        news = NewsForm(request.POST)
        if news.is_valid():
            news.save()
        return render(request, "add_news.html", {"msg": "Success"})
    return render(request, "add_news.html", {})


def view_news(request):
    if request.method == "GET":
        news = News.objects.all()
    return render(request, "view_news.html", {"news": news})

def delete_news(request,id):
    news=News.objects.get(id=id)
    news.delete()
    return redirect("/view_news")

def edit_news(request, id):
    news = News.objects.get(id=id)
    return render(request, "edit_news.html", {"news": news})


def update_news(request):
    if request.method == "POST":
        userid = request.POST["id"]
        news = News.objects.get(id=userid)
        news = NewsForm(request.POST, instance=news)
        if news.is_valid():
            news.save()
        return redirect("/view_news")
    return redirect("/view_news")


def admin_bug_piechart(request, id):
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

    return render(request, "admin_bug_piechart.html", context)

