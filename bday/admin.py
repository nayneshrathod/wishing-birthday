from django.contrib import admin
from .models import *


# Register your models here.


class wishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("toname","fromname")}


admin.site.register(wish, wishAdmin)

# admin.site.register(wish)
