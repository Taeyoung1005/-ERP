from django.contrib import admin

from .models import coa, product, User, HR

admin.site.register(coa)
admin.site.register(product)
admin.site.register(User)
admin.site.register(HR)
