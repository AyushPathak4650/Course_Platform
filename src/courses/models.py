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
    
    access = models.CharField(
        max_length=5, 
        choices=AccessRequirement.choices, 
        default=AccessRequirement.EMAIL_REQUIRED
    )
    
    status = models.CharField(
        max_length=10, 
        choices=PublishedStatus.choices, 
        default=PublishedStatus.DRAFT
    )
    
    # image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    image = CloudinaryField("image", null=True)
    

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(null = True, blank= True)
    can_preview = models.BooleanField(default=False, help_text="If user does not have access to the course, can they view this?")
    status = models.CharField(
        max_length=10, 
        choices=PublishedStatus.choices, 
        default=PublishedStatus.PUBLISHED
    )