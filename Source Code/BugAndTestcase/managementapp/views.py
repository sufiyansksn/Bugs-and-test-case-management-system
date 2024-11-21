from django.shortcuts import render, redirect
from managementapp.models import Contact
from managementapp.forms import ContactForm
from adminsapp.models import Employee, Project, News
from adminsapp.forms import EmployeeForm, ProjectForm
from managementapp.models import Task
from managementapp.forms import TaskForm
from employeeapp.models import Bug, Testcase, Requirements
from employeeapp.forms import BugForm, TestcaseForm
from django.db.models import Count


# Create your views here.

def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        return render(request, "contact.html", {"msg": "Success"})
    return render(request, "contact.html", {})


# def management(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         p_word = request.POST['password']
#         request.session['email'] = email
#         role = request.session["role"]
#         if Employee.objects.filter(email=email, password=p_word, role="manager"):
#             return render(request, "management_home.html", {"msg": "Great! login Successfully"})
#         else:
#             return render(request, "management_login.html", {"msg": "Sorry! you are not a manager"})
#     return render(request, "management_login.html", {})
def management(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "management_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid Credentials"
            print(e)
            return render(request, "management_login.html", {"msg": msg})
    return render(request, "management_login.html", {})

def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def manager_change_pwd(request):
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
                return render(request, "manager_change_pwd.html", {"msg": msg,"email":email})
        return render(request, "manager_change_pwd.html", {"email":email})
    else:
        return render(request, "index.html", {"email":email})


def manager_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "manager_edit_profile.html", {"employ": employ, "role":role})


def manager_update_profile(request):
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
                return render(request, "manager_home.html", {"msg": "Successfully Update ", "role": role})
        except Exception as e:
            print(e)
            return render(request, "manager_edit_profile.html", {"msg": "Your Details Not Updated", "role":role})
    return render(request, "manager_edit_profile.html", {"employee":data, "role":role})


def management_home(request):
    return render(request, "management_home.html", {})


def management_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "management_login.html", {})

def manager_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "management_login.html", {})

def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def add_task(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        print("hi1")
        try:
            if task.is_valid():
                print("hi2")
                task.save()
                return render(request, "add_task.html", {"msg": "Success"})
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_task.html", {})
    mngr_email = request.session["email"]
    details_emply = Employee.objects.all().exclude(role="manager")
    details_project = Project.objects.all()
    return render(request, "add_task.html",
                  {"mngr_email": mngr_email, "details_emply": details_emply, "details_project": details_project})


def view_task(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, "view_task.html", {"tasks": tasks})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/view_task")


def edit_task(request, id):
    tasks = Task.objects.get(id=id)
    mngr_email = request.session["email"]
    details_emply = Employee.objects.all().exclude(role="manager")
    details_project = Project.objects.all()
    return render(request, "edit_task.html", {"mngr_email": mngr_email, "details_emply": details_emply, "tasks": tasks,
                                              "details_project": details_project})


def update_task(request):
    if request.method == "POST":
        userid = request.POST["id"]
        task = Task.objects.get(id=userid)
        task = TaskForm(request.POST, instance=task)
        print("hi1")
        try:
            if task.is_valid():
                print("hi2")
                task.save()
                print("h3")
        except Exception as e:
            print(e)
            return redirect("/view_task", {"msg": "success"})
    return render(request, "edit_task.html", {})


def manager_view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        return render(request, "manager_view_testcases.html", {"testcases": testcases})


def manager_view_bugs(request):
    if request.method == "GET":
        bugs = Bug.objects.all()
        return render(request, "manager_view_bugs.html", {"bugs": bugs})


def task_update_status(request, id):
    tasks = Task.objects.get(id=id)
    # email= request.session["email"]
    return render(request, "task_update_status.html", {"tasks": tasks, "id": id})


def task_status_insert(request):
    if request.method == "POST":
        try:
            # tested_by_email = request.session["email"]
            status = request.POST['status']
            id = request.POST['id']
            print("hi1")
            print("hi2")
            task = Task.objects.get(id=id)
            print("hi3")
            task.status = status
            # task.tested_by_email=tested_by_email
            print("hi4")
            task.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "view_task.html", {})
    return render(request, "task_update_status.html", {})

def manager_view_projects(request):
    projects = Project.objects.all()
    return render(request, "manager_view_projects.html", {"projects": projects})

def manager_view_requirements(request,id):
    projects = Project.objects.get(id=id)
    requirements = Requirements.objects.filter(projects_id=projects)
    return render(request, "manager_view_requirements.html", {"requirements": requirements})

def manager_view_notifications(request):
    notifications = News.objects.all()
    return render(request, "manager_view_notifications.html", {"notifications": notifications})


def manager_bug_piechart(request, id):
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

    return render(request, "manager_bug_piechart.html", context)
