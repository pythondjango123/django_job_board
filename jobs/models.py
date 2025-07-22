from django.db import models

# Create your models here.
class JobPost(models.Model):
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    description=models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Application(models.Model):
    job=models.ForeignKey(JobPost, on_delete=models.CASCADE, related_name='applications')
    applicant_name=models.CharField(max_length=100)
    email=models.EmailField()
    resume=models.FileField(upload_to='resumes/')
    applied_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"