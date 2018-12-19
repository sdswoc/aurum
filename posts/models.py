from __future__ import unicode_literals

from django.db import models

from django.urls import reverse

# Create your models here.

class Post(models.Model):
		title=models.CharField(max_length=120)
		content = models.TextField()
		timestamp = models.DateTimeField( auto_now = False ,auto_now_add = True)
		updated = models.DateTimeField( auto_now = True , auto_now_add = False)
	    
		# def __unicode__(self):
		# 	return self.title

		def __str__(self):
		    return self.title

		def get_absolute_url(self):
			return reverse("detail" , kwargs={"id": self.id})
		
		def get_another_url(self):
		    return reverse("list", )	

		def get_delete_url(self):
		    return reverse("delete" , kwargs={"id": self.id}) 
	   			    