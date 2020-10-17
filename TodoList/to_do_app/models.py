# TodoList > to_do_app > models.py
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=255)
    deleteYn = models.BooleanField(default=False)
    