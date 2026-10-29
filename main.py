import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskManager.settings")

django.setup()

from Task_Manager.models import User, Task


# User.objects.create(
#     name = "Alex",
#     email = "alex@example.com",
#     role = "user")

# User.objects.create(
#     name = "Sofa",
#     email = "sofa@example.com",
#     role = "user")

# User.objects.create(
#     name = "Iosip",
#     email = "iosip@example.com",
#     role = "user")


# Task.objects.create(
#     name = "Clean aquarium",
#     description = "Clean fish aquarium",
#     status = "completed")

# Task.objects.create(
#     name = "Do homework",
#     description = "Do homework math",
#     status = "in_progress")


user1 = User.objects.get(id = 1)
user2 = User.objects.get(id = 2)
user3 = User.objects.get(id = 3)

task1 = Task.objects.get(id = 1)
task2 = Task.objects.get(id = 2)

print(user1.name,
      user2.name,
      user3.name,
      task1.name,
      task2.name
      )

# task1.responsible.add(user1)
# task2.responsible.add(user2)

task2.change_Status('completed')
task1.change_Status('in_progress')

task1.change_responsible(user1)