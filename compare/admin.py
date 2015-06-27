from django.contrib import admin
from compare.models import Category, Mobile

class MobileAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'category', 'price')

#class CategoryAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('platform',)}

admin.site.register(Category)
admin.site.register(Mobile, MobileAdmin)
