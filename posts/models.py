from __future__ import unicode_literals

from django.db import models

from django.urls import reverse

from django.db.models.signals import pre_save

from django.utils.text import slugify

from django.conf import settings


# Create your models here.

def upload_location(instance , filename):
	return "%s/%s" %(instance.slug , filename)

class Post(models.Model):
	username = models.ForeignKey(settings.AUTH_USER_MODEL , default =1, on_delete=models.DO_NOTHING)
	title=models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	image=models.FileField(upload_to=upload_location,blank=True,null=True)
	content = models.TextField()
	timestamp = models.DateTimeField( auto_now = False ,auto_now_add = True)
	updated = models.DateTimeField( auto_now = True , auto_now_add = False)
	comment = models.TextField(default='hello')
	# comment_timestamp = models.DateTimeField(auto_now = True , auto_now_add = False)

	# def __unicode__(self):
	# 	return self.title

	def __str__(self):
	    return self.title

	def get_absolute_url(self):
		return reverse("detail" , kwargs={"slug": self.slug})

	def get_another_url(self):
		return reverse("list", )	

	def get_delete_url(self):
		return reverse("delete" , kwargs={"slug": self.slug}) 
	
	def get_update_url(self):
		return reverse("update" , kwargs={"slug":self.slug})		

	def get_create_url(self):
		return reverse("create",)		

	class Meta:
	    ordering = [  "-updated"]	    






def create_slug(instance , new_slug=None):
	slug = slugify(instance.title)

	if new_slug is not None:
		slug=new+slug

	queryset = Post.objects.filter(slug=slug).order_by("-id")
	exists = queryset.exists()
	
	if exists:
		new_slug = "%s-%s" %(slug , queryset.first().id)
		return create_slug(instance , new_slug=new_slug)

	return slug	


def pre_save_post_reciever(sender , instance , *args , **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)





pre_save.connect(pre_save_post_reciever,sender=Post)



# class Answer(models.Model):
# 	answer = models.TextField()
# 	timestamp=models.DateTimeField(auto_now = False ,auto_now_add = True)


# 	def get_answer_url(self):
# 		return reverse("answer" , kwargs={"slug": self.slug})