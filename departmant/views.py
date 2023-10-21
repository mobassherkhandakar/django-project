from django.shortcuts import render

# Create your views here.


def department_fun(req):
    return render(req, 'department/department.html')
