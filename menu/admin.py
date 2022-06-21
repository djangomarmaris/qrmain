from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category,Product ,Restaurant
# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}






class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','slug','category','price','available']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}




class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Restaurant,RestaurantAdmin)


admin.site.site_header = 'Datça QR / Developer @ İhsan Gürol Demirtaş'