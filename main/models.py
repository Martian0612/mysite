from django.db import models

# Create your models here.
# ToDoList -> Table
class ToDoList(models.Model):
	# name of the ToDoList
	name = models.CharField(max_length = 200)

	# to return the name of the todolist in readable format, when accessing it without object or instance.
	# or to not get address of the ToDoList object when trying to access
	def __str__(self):
		return self.name


# Items in a ToDoList
class Items(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete = models.CASCADE)
	# text = models.TextField() # in text field there is no max length
	text = models.CharField(max_length = 300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text