import json

from django.core.serializers import serialize
from django.db import models
from django.conf import settings

# Create your models here.

def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename = filename)

class UpdateQuerySet(models.QuerySet):

	# def serialize(self):
	# 	qs = self
	# 	return serialize('json', qs, fields=('user', 'content', 'image'))

	def serialize(self):
		list_values = list(self.values("user", "content", "image", "id"))
		print(list_values)

		return json.dumps(list_values)

class UpdateManager(models.Manager):
	def get_queryset(self):

		return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):

	user 		 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	content 	 = models.TextField(blank = True, null = True)
	image 		 = models.ImageField(upload_to='', blank = True, null = True)
	updated 	 = models.DateTimeField(auto_now=True)
	timestamp 	 = models.DateTimeField(auto_now_add=True)

	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	def serialize(self):

		try:
			image = self.image.url
		except:
			image = ""

		#json_data = serialize("json", [self], fields=('user', 'content', 'image'))
		data = {

			"id": self.id,
			"content": self.content,
			"user": self.user.id,
			"image": image
		}
		data = json.dumps(data)
		return data