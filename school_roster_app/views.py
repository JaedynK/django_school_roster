from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance
print('here')

def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    staff_data = {
       'data': my_school.staff_names
    }

    return render(request, "pages/staff.html", staff_data)


def staff_detail(request, employee_id):

    staff_detail = {
        'staff_info': my_school.find_staff_by_id(employee_id)
    }

    return render(request, "pages/staff_detail.html", staff_detail)

def list_students(request):
    student_data = {
       'data': my_school.student_names
    }

    return render(request, "pages/students.html", student_data)

def student_detail(request, student_id):
   
    student_detail = {
        'student_info': my_school.find_student_by_id(student_id),
    }

    return render(request, "pages/student_detail.html", student_detail)
