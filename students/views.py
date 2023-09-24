from django.shortcuts import render, get_object_or_404, redirect

# from django.shortcuts import render,redirect

from .forms import StudentForm
from .models import Student



# Create your views here.
def home(request):
    return render(request, 'home.html')
  
def Contact(request):
    return render(request, 'ContactUs.html')


def addStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = StudentForm()
    return render(request, 'student-add.html', {'form': form})

def list_students(request):
        students = Student.objects.all()
        return render(request, 'list_students.html', {'students': students})

        # crud operations
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list-students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('list-students')
    return render(request, 'confirm_delete.html', {'student': student})