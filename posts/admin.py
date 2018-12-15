from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ( "__str__" , "timestamp" , "updated")
	list_display_links = ['timestamp']
	list_filter = ['updated']

	class Meta:
		model =  Post

admin.site.register(Post , PostModelAdmin)      # admin registers the Model Post on the website 