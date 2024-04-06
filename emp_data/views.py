from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import student
# Create your views here.

# adding data
def emp_add_data(request):
    if request.method=='POST':
        data=request.POST
        e=student.objects.create(name=data['student_name'], classes=data['student_class'], age=data['student_age'], roll_number=data['student_roll_number'], phone_number=data['student_phone_number'])
        e.save()
        return redirect('/emp/show_data')
    else:
        return render(request, "emp.html")

# showing data
def show_data(req):
    data=student.objects.all()
    return render(req, "show_data.html", {'data': data})

# delete data
def delete_data(request, pk):
    student.objects.get(id=pk).delete();
    return redirect("/emp/show_data")

# update data
def update_data_form(request, ud):
    data=student.objects.get(id=ud);
    return  render(request, "emp_update.html", {'data': data});

# data updated
def updated_data_save(request, data_update):
    if request.method=='POST':
        data=student.objects.get(id=data_update)
        data.name=request.POST.get('student_name')
        data.classes=request.POST.get('student_class')
        data.age=request.POST.get('student_age')
        data.roll_number=request.POST.get('student_roll_number')
        data.phone_number=request.POST.get('student_phone_number')
        data.save()
        return redirect('/emp/show_data')
    else:
        return render(request, "emp_update.html")
