from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('los/', views.ListOfStudent.as_view(), name='listofstudent'),
    path('los/<int:pk>', views.DetailsOfStudent.as_view(), name='detailsofstudent'),
    path('ca', views.CreateStudentProfile.as_view(), name='CreateStudentProfile'),
    path('<int:pk>/ua', views.UpdateStudentProfile.as_view(), name='UpdateStudentProfile'),
    path('<int:pk>/da', views.DeleteStudentProfile.as_view(), name='DeleteStudentProfile'),

]
