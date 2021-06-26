from django.db import models

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length = 255)
    description = models.TextField()
    priority = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True , null = True)
    
    def __str__(self):
        return self.task