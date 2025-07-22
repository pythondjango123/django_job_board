from django.contrib import admin
from .models import JobPost, Application
# Register your models here.



class JobAdmin(admin.ModelAdmin):
   list_display=('title', 'company', 'location', 'posted_at')
   list_filter=('company', 'location')
   search_fields=('title', 'company', 'description')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'email', 'job', 'applied_at')
    list_filter = ('job',)
    search_fields = ('applicant_name', 'email')

admin.site.register(JobPost, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
