from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = [ 'title' , 'content' , 'image' ]


# class AnswerForm(forms.ModelForm):

# 	class Meta:
# 		model  = Answer
# 		fields = ['answer'] 
