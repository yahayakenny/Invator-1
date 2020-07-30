from django.db import models

class Emails(models.Model):
	name = models.CharField(max_length=254, blank=False)
	message = models.CharField(max_length=254, blank=False)
	recipient = models.EmailField()
	attach = models.FileField(upload_to='uploads/')

	def __str__(self):
		return self.recipient
