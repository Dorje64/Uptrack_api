from django.db import models
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField( auto_now_add = True )
    updated_at = models.DateTimeField( auto_now = True )
    class Meta:
        abstract = True

class Project(BaseModel):
    name = models.CharField(max_length = 200)
    repo_dir = models.CharField(max_length = 200)
    remote_url = models.TextField()

class Author(model.Model):
    usernam =  models.CharField(max_length = 200)
    password = models.TextField()

class Update(BaseModel):
    text = models.TextField();
    project = models.ForeignKey( Project, on_delete = models.CASCADE )
    author = models.ForeignKey( Author, on_delete = models.CASCADE )
