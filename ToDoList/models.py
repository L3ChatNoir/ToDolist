from django.db import models

class Task(models.Model):
    #primary key
    idtask = models.AutoField(primary_key=True)

    #description of the task
    name = models.CharField(max_length=100, blank=True, null=True)

    #date of creation
    createdate = models.DateField(auto_now_add=True)

    #date of deadline
    deadline = models.DateField(auto_now=False, null=True, blank=True, default= None)

    #boolean represente if task is over
    do = models.BooleanField(default=False)

    def __str__(self):
        return "name" + self.name
