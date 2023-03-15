from django.db import models
from model_utils import Choices

GENDER = Choices(
	("Male", "Male"),
	("Female", "Female"),
)
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=64)
	gender = models.CharField(max_length=16, choices=GENDER, default="Male")
	age = models.CharField(max_length=3)

	def __str__(self):
		if self.name:
			return self.name
		else:
			return "Name"

	class Meta:
		db_table = "students"


class Marks(models.Model):
	student = models.ForeignKey(Student, related_name = "marks", on_delete=models.CASCADE)
	class_name = models.CharField(max_length=32)
	english = models.CharField(max_length=3)
	nepali = models.CharField(max_length=3)

	def __str__(self):
		if self.student:
			return self.class_name
		else:
			return "Class"
	class Meta:
		db_table = "marks"