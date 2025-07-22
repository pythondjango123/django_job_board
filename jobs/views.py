from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import JobPost, Application
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.
class JobListView(ListView):
    model=JobPost
    template_name='jobs/job_list.html'
    context_object_name='jobs'

class JobDetailView(DetailView):
    model=JobPost
    template_name='jobs/job_detail.html'
    context_object_name='job'

class JobApplicationView(LoginRequiredMixin,CreateView):
    model=Application
    fields=['applicant_name','email', 'resume']
    template_name='jobs/job_application_form.html'

    def form_valid(self, form):
        job=JobPost.objects.get(pk=self.kwargs['pk'])
        form.instance.job=job
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('apply_success')

class HomeView(TemplateView):
    template_name='jobs/home.html' 

class ApplicationSuccessView(TemplateView):
    template_name='jobs/apply_success.html'

class RegisterView(FormView):
    template_name = 'jobs/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully. You can now log in.')
        return super().form_valid(form)

class LogoutConfirmView(TemplateView):
    template_name = 'jobs/logout_confirm.html'