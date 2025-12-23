from django.contrib import admin

# Register your models here.

from .models import Author, Post, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_filter = ('date', 'author', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Post, PostAdmin)

admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
