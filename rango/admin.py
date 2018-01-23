from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CatAdmin(admin.ModelAdmin):
	list_display = ('name', 'views', 'likes')

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CatAdmin)