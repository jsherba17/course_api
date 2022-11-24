from django.db import models


class Branches(models.Model) :
	latitude = models.CharField(max_length=255)
	longitude = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	course = models.ForeignKey('Courses', related_name='branches', on_delete=models.PROTECT, null=True)

	def __str__(self) :
		return self.address


class Contacts(models.Model):
	type = models.IntegerField()
	value = models.CharField(max_length=255)
	course = models.ForeignKey('Courses', related_name='contacts' ,on_delete=models.PROTECT, null=True)

	def __str__(self) :
		return self.value


class Courses(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	logo = models.ImageField(blank=True, null=True)


	def __str__(self) :
		return self.name

