from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

# Create your views here.

from .models import Post 
from .forms import PostForm

def post_home(request):
	queryset = Post.objects.all()
	context= {

      "object_list" : queryset ,
      "title"       : "IT'S RUSSIA"
          }
	return render(request,'post_list.html',context)


def post_create(request):   # cant put another_url here as the arg "id" isnt used in the func
	form = PostForm(request.POST or None)
	if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			messages.success(request , "Post Successful!")
			form = PostForm()
			return HttpResponseRedirect(instance.get_absolute_url())
	context = {
	  "form" : form
	}
	return render( request , 'post_form.html', context)	


def post_detail(request,id):
	instance= get_object_or_404(Post , id=id)
	
	context = {
	"title"    : instance.title , 
	"instance" : instance ,
	}
	return render(request , "post_detail.html",context)



def post_update(request,id=None):

	instance =get_object_or_404(Post , id=id)  #needed cause we have to generate form
	form = PostForm(request.POST or None , instance=instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request , "Post Updated!")
		return HttpResponseRedirect(instance.get_another_url())
	context = {
	 "title"    : instance.title , 
	 "instance" : instance       ,
	 "form"     : form 
	}	

	return render(request , "post_form.html" , context) # opens up post form 


def post_delete(request,id):
	instance= get_object_or_404(Post , id=id)
	instance.delete()
	messages.success(request , "Post deleted!")

	return HttpResponseRedirect(instance.get_another_url())
