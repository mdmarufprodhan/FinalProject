from django.contrib import admin
from .models import buyer, flat, payment, seller, sold

# Register your models here.
admin.site.register(buyer)
admin.site.register(flat)
admin.site.register(payment)
admin.site.register(seller)
admin.site.register(sold)