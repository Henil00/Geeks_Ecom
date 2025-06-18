from django.contrib import admin

from .models import  Order, OrderItem

@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer','order_date','status','total_amount']
    list_filter = ['status','order_date']
    search_fields = ['customer__username','id']
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','price']
    


