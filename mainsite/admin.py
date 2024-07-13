from django.contrib import admin
from.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
    search_fields=('title',)
    ordering=('-slug',)

admin.site.register(Post, PostAdmin)