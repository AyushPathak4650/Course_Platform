from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email Required"

class PublishedStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    access = models.CharField(max_length=14, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)
    
    @property
    def is_published(self):
        return self.status == PublishedStatus.PUBLISHED