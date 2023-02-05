from django.contrib import admin

from .models import coa, product, User

admin.site.register(coa)
admin.site.register(product)
admin.site.register(User)
