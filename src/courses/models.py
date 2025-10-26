from django.db import models

# Create your models here.

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email", "Email Required"

class PublishedStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    DRAFT = "draft", "Draft"
    COMING_SOON = "soon", "Coming Soon"


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    
    access = models.CharField(max_length=10, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    
    status = models.CharField(max_length=10, choices=PublishedStatus.choices, default=PublishedStatus.DRAFT)
    
    #image
    