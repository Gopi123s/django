from django.contrib import admin
from .models import Category,Post


# for   configratation of category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title','desc','url','add_date')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields=('title',)
    list_filter=('cat',)
    list_per_page=50


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)