from django.contrib import admin
from dashapp.models import Product,Category,Employee,Order

# Register your models here

class ProductAdmin(admin.ModelAdmin):
     pass
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, ProductAdmin)
admin.site.register(Employee, ProductAdmin)
admin.site.register(Order, ProductAdmin)
