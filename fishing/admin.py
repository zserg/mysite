from django.contrib import admin

# Register your models here.
from fishing.models import Catch,Lure

admin.site.register(Catch)
admin.site.register(Lure)


