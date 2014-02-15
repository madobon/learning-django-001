from django.contrib import admin
from post.models import Post

# Register your models here.

class PostAdmin (admin.ModelAdmin):
    readonly_fields = ['get_latest_keyword','get_previous_keyword','created_at']
    fieldsets = [
        (None, {'fields': ['created_at','get_latest_keyword','get_previous_keyword','keyword']}),
    ]
    list_display = ('created_at','get_previous_keyword','keyword')
    list_filter = ['created_at','keyword']

admin.site.register(Post, PostAdmin)