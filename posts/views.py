from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import quote_plus

# Create your views here.

from .models import Post 
from .forms import PostForm

def post_home(request):
    
    queryset_list = Post.objects.all().order_by("-updated")
    paginator = Paginator(queryset_list, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context= {

      "object_list" : queryset ,
      "title"       : "IT'S RUSSIA"
          }
    return render(request,'post_list.html',context)



def listing(request):
    queryset = Post.objects.all()

    return render(request, 'list.html', {'contacts': contacts})


def post_create(request):   # cant put another_url here as the arg "slug" isnt used in the func
	if not request.user.is_authenticated:
		raise Http404

	form = PostForm(request.POST or None , request.FILES or None) # so as to include image in database also
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


def post_detail(request,slug):

	instance= get_object_or_404(Post , slug=slug )
	share_string = quote_plus(instance.content)
	context = {
	"title"        : instance.title , 
	"instance"     : instance       ,
	"share_string" : share_string   ,
 	}
	return render(request , "post_detail.html",context)



def post_update(request,slug=None):
	if not request.user.is_authenticated:
		raise Http404
 
	instance =get_object_or_404(Post , slug=slug)  #needed cause we have to generate form
	form = PostForm(request.POST or None , request.FILES or None ,instance=instance , )
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


def post_delete(request,slug):
	instance= get_object_or_404(Post , slug=slug)
	instance.delete()
	messages.success(request , "Post deleted!")

	return HttpResponseRedirect(instance.get_another_url())

# def post_answer(request,slug):
# 	instance_ans =get_object_or_404(Post , slug=slug)  #needed cause we have to generate form
# 	form = AnswerForm(request.POST or None , request.FILES or None , instance= instance_ans) # so as to include image in database also
# 	if form.is_valid():
# 		instance = form.save(commit = False)
# 		instance.save()
# 		messages.success(request , "Answer Successful!")
# 		form = AnswerForm()
# 		return HttpResponseRedirect(instance.get_absolute_url())
	
# 	context = {
# 	"form" : form  ,
# 	"instance_ans" : instance_ans	
# 	}
# 	return render( request , 'post_answer.html' , context)	