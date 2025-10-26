import helpers
from django.db import models
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()

# Models
class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email Required"

class PublishedStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    DRAFT = "draft", "Draft"
    COMING_SOON = "soon", "Coming Soon"

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=120)
    
    description = models.TextField(null=True, blank=True)
    
    access = models.CharField(max_length=5, 
                              choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    
    status = models.CharField(max_length=10, 
                              choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)
    
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image", null=True)
    