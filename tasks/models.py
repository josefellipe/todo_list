from django.db import models


class TaskManager():
    def create_task(self, description):
        self.description    = description

class Task(models.Model):
    description = models.CharField(max_length=100)

    completed    = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.description
    
