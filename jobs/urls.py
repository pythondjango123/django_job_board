from django.urls import path
from .views import HomeView, JobListView, JobDetailView, JobApplicationView, ApplicationSuccessView,RegisterView, HomeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import LogoutConfirmView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('jobs/<int:pk>/apply/', JobApplicationView.as_view(), name='apply_job'),
    path('application-success/', ApplicationSuccessView.as_view(), name='apply_success'),
    path('login/', auth_views.LoginView.as_view(template_name='jobs/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-confirm/', LogoutConfirmView.as_view(), name='logout_confirm'),
]
