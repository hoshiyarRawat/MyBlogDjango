from django.contrib import admin
from .models import BookOutlet, Author, Address, Country

# Register your models here.

class BookOutletAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'rating', 'slug', 'author', 'get_countries', 'get_addresses')
    readonly_fields = ("slug",)
    search_fields = ('name', 'title', 'slug', 'author__first_name', 'author__last_name')
    #prepopulated_fields = {'slug': ('title', )}
    list_filter = ('rating','name', 'author__first_name')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zip_code', 'country')
    search_fields = ('street', 'city', 'state', 'zip_code', 'country')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')



admin.site.register(BookOutlet, BookOutletAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Address, AddressAdmin)

admin.site.register(Country, CountryAdmin)