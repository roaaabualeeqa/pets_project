from django.contrib import admin

# Register your models here.

from .models import Pet

# Register the pet table
admin.site.register(Pet)