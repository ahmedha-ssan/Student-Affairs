from django.shortcuts import render, redirect
from . import views
from .models import Student_Data
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    return render(request, 'home.html')


def add(request):
    return render(request, 'add.html')


def index(request):
    return render(request, 'index.html')


def edit(request, context):
    return render(request, 'edit.html', {'students': context})


def login(request):
    return render(request, 'login.html')


def view(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        id = request.POST.get('id')
        student = Student_Data.objects.get(SI=id)

        student.status = status
        student.save()

        data = Student_Data.objects.all()

        context = {
            "data": data,
        }

        return render(request, 'view page.html', context)
    elif request.method == 'GET':
        data = Student_Data.objects.all()

        context = {
            "data": data,
        }

        return render(request, 'view page.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        si = request.POST.get('ID')
        gpa = request.POST.get('GPA')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        status = request.POST.get('status')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dateOfBirth = request.POST.get('date of brith')
        Department = request.POST.get('department')

        newStudent = Student_Data(name=name, gender=gender, level=level, SI=si, GPA=gpa, status=status,
                                  Email=email, mobile=mobile, DateOfBirth=dateOfBirth, department=Department)

        newStudent.save()
        return redirect('add')


def search_edit(request):
    return render(request, 'search_edit.html')


def search_data(request):
    ID = request.POST.get('id')
    checker = Student_Data.objects.filter(SI=ID).exists()
    if checker:
        student = Student_Data.objects.get(SI=ID)
        context = {
            'mystudent': student,
        }
        return render(request, 'edit.html', context)
    else:
        return search_edit(request)


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        si = request.POST.get('ID')
        gpa = request.POST.get('GPA')
        gender = request.POST.get('gender')
        level = request.POST.get('level')
        status = request.POST.get('status')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        # dateOfBirth = request.POST.get('DateOfBirth')

        studen_obj = Student_Data.objects.get(SI=id)

        studen_obj.name = name
        studen_obj.SI = si
        studen_obj.GPA = gpa
        studen_obj.gender = gender
        studen_obj.level = level
        studen_obj.status = status
        studen_obj.mobile = mobile
        # studen_obj.DateOfBirth = dateOfBirth
        studen_obj.email = email
        studen_obj.save()
    return redirect('search_edit')


def delete(request, id):
    # if request.method == 'GET':
    student_obj = Student_Data.objects.get(SI=id)
    student_obj.delete()
    return redirect('search_edit')


def search(request):
    if request.method == 'GET':
        return render(request, 'search_active.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        checker = Student_Data.objects.filter(
            name=name, status='active').exists()
        context = {
            'isEmpty': True,
        }
        if checker:
            students = Student_Data.objects.filter(name=name)
            context = {
                'students': students,
                'isEmpty': False,
            }
            return render(request, 'search_active.html', context)

        else:
            return redirect('search')


def department(request):
    if request.method == 'GET':
        return render(request, 'department_registeration.html', {'res': ''})
    elif request.method == 'POST':
        name = request.POST.get('name')
        id = request.POST.get('id')
        department = request.POST.get('department')

        student = Student_Data.objects.get(SI=id)
        student.department = department
        student.save()

        return redirect('search')
