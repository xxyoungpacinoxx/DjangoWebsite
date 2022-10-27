from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'student/home.html'


class ListOfStudent(ListView):
    model = models.Student
    template_name = 'student/listofstudent.html'


class DetailsOfStudent(DetailView):
    model = models.Student
    template_name = 'student/Detailsofstudent.html'


class CreateStudentProfile(CreateView):
    model = models.Student
    template_name = 'student/CreateStudentProfile.html'
    fields = ['name', 'family', 'age', 'university', 'status']


class UpdateStudentProfile(UpdateView):
    model = models.Student
    template_name = 'student/UpdateStudentProfile.html'
    fields = ['name', 'family', 'age', 'university', 'status']


class DeleteStudentProfile(DeleteView):
    model = models.Student
    template_name = 'student/DeleteStudentProfile.html'
    success_url = reverse_lazy('listofstudent')
