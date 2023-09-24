from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('add-student', views.addStudent, name="add-student"),
    path('Contact', views.Contact, name="ContactUs"),
    path('list-students', views.list_students, name='list-students'),
     path('edit-student/<int:student_id>/', views.edit_student, name='edit-student'),
    path('delete-student/<int:student_id>/', views.delete_student, name='delete-student'),

]