from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(choices=[('admin' , 'Admin'),( 'user', 'User')])
    
    

    def __str__(self):
        return self.name

    def change_role(self,role_name):
        self.role = role_name
        self.save()

class Task(models.Model):

    class Status(models.TextChoices):
        In_progress = 'in_progress','в процесі'
        Completed = 'completed','виконано'
        Postponed = 'postponed','відкладено'

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=Status.choices)
    responsible = models.ManyToManyField('User',related_name='user')
    
    def change_Status(self,new_status):
            self.status = new_status
            self.save(update_fields=['status'])

    def change_responsible(self, users):
        if isinstance(users, User):
            users = [users]
        self.responsible.set(users)
