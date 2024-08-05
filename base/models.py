from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Topic(models.Model):
	objects = None
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Room(models.Model):
	objects = None
	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	participants = models.ManyToManyField(User, related_name='participants', blank=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.name


class Message(models.Model):
	objects = None
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	body = models.TextField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated', '-created']

	def __str__(self):
		return self.body[0:50]
