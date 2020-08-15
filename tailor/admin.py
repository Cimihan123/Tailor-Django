from django.contrib import admin
from .models import Contact ,Male ,Female

# Register your models here.
admin.site.register(Male)
admin.site.register(Female)
admin.site.register(Contact)