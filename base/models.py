from django.db import models

import uuid

from ckeditor_uploader.fields import RichTextUploadingField


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='project', default='images/project.jpg')
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    

class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name